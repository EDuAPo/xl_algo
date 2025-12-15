#!/usr/bin/env python3

import cv2
import numpy as np
import os
import sys
import json
import uuid
import re
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor, as_completed
import multiprocessing
import argparse # 导入argparse模块
from pathlib import Path
current_dir = Path(__file__).resolve().parent
workspace_dir = current_dir.parent
if str(workspace_dir) not in sys.path:
    sys.path.append(str(workspace_dir))

# 从 lidar_to_image.py 及其依赖中导入所需的配置和映射   
from config.lidar_calibrator import LIDAR_CONFIGS, get_lidar_extrinsics_config_id
from config.camera_calibrator import get_camera_extrinsics

# 设置进程池的最大工作进程数（默认使用CPU核心数）
MAX_WORKERS = multiprocessing.cpu_count()
# 如果CPU核心数太多，可以手动限制，例如：MAX_WORKERS = 4

def undistort_fish_optimized(img_path, K, D, DIM, is_fish, scale=0.5):
    """鱼眼相机去畸变（保持原有实现）"""
    img = cv2.imread(img_path)
    if img is None:
        raise ValueError(f"无法读取图像: {img_path}")
    
    h, w = img.shape[:2]
    
    if abs(w/h - DIM[0]/DIM[1]) > 0.01:
        print(f"警告: 图像宽高比不匹配，将进行缩放")
        img = cv2.resize(img, DIM, interpolation=cv2.INTER_AREA)
    
    Knew = K.copy()

    if is_fish == 1:
            DIM = (2400, 1600)

            Knew[0, 0] = 0.5 * K[0, 0]
            Knew[1, 1] = 0.5 * K[1, 1]
            Knew[0, 2] = DIM[0]/2
            Knew[1, 2] = DIM[1]/2
            map1, map2 = cv2.fisheye.initUndistortRectifyMap(
        K, D, np.eye(3), Knew, DIM, cv2.CV_16SC2
    )
    
            undistorted_img = cv2.remap(
        img, map1, map2, 
        interpolation=cv2.INTER_CUBIC,
        borderMode=cv2.BORDER_CONSTANT, 
        borderValue=(0, 0, 0)
    )
    else:
            DIM = (5400, 2260)

            
        # 使用调整后的内参
            Knew = K.copy()
            Knew[0, 0] = 1 * K[0, 0]  # fx
            Knew[1, 1] = 1 * K[1, 1]  # fy  
            Knew[0, 2] = DIM[0]/2
            Knew[1, 2] = DIM[1]/2
            map1, map2 = cv2.initUndistortRectifyMap(
            K, D, np.eye(3), Knew, DIM, cv2.CV_16SC2
        )
            undistorted_img = cv2.remap(
            img, map1, map2, 
            interpolation=cv2.INTER_LINEAR,
            borderMode=cv2.BORDER_CONSTANT,
            borderValue=(0, 0, 0)
        )
            # undistorted_img = cv2.undistort(img, K, D, None, Knew)

    return undistorted_img, Knew

def crop_black_borders(
    img, 
    crop_factor=0.0, 
    non_black_thresh=1,
    return_borders=False
):
    """保持原有黑边裁剪功能"""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    height, width = gray.shape
    
    row_left_points = []
    row_right_points = []
    col_top_points = []
    col_bottom_points = []
    
    for y in range(height):
        left_x = None
        for x in range(width):
            if gray[y, x] > non_black_thresh:
                left_x = x
                break
        if left_x is not None:
            row_left_points.append((left_x, y))
        
        right_x = None
        for x in range(width-1, -1, -1):
            if gray[y, x] > non_black_thresh:
                right_x = x
                break
        if right_x is not None:
            row_right_points.append((right_x, y))
    
    for x in range(width):
        top_y = None
        for y in range(height):
            if gray[y, x] > non_black_thresh:
                top_y = y
                break
        if top_y is not None:
            col_top_points.append((x, top_y))
        
        bottom_y = None
        for y in range(height-1, -1, -1):
            if gray[y, x] > non_black_thresh:
                bottom_y = y
                break
        if bottom_y is not None:
            col_bottom_points.append((x, bottom_y))
    
    if (len(row_left_points) == 0 or len(row_right_points) == 0 or
        len(col_top_points) == 0 or len(col_bottom_points) == 0):
        print("警告：某组边界点为空，返回原图")
        if return_borders:
            return img, (0, 0, width-1, height-1)
        return img
    
    left_bound = max(row_left_points, key=lambda p: p[0])[0]
    right_bound = min(row_right_points, key=lambda p: p[0])[0]
    top_bound = max(col_top_points, key=lambda p: p[1])[1]
    bottom_bound = min(col_bottom_points, key=lambda p: p[1])[0]
    
    if (left_bound >= right_bound) or (top_bound >= bottom_bound):
        print("警告：筛选后边界无效，返回原图")
        if return_borders:
            return img, (0, 0, width-1, height-1)
        return img
    
    inner_width = right_bound - left_bound
    inner_height = bottom_bound - top_bound
    
    crop_x = int(inner_width * crop_factor)
    crop_y = int(inner_height * crop_factor)
    
    x_start = max(left_bound + crop_x, 0)
    y_start = max(top_bound + crop_y, 0)
    x_end = min(right_bound - crop_x, width - 1)
    y_end = min(bottom_bound - crop_y, height - 1)
    
    if x_end <= x_start:
        x_start, x_end = left_bound, right_bound
    if y_end <= y_start:
        y_start, y_end = top_bound, bottom_bound
    
    cropped_img = img[y_start:y_end+1, x_start:x_end+1]
    
    if return_borders:
        return cropped_img, (x_start, y_start, x_end, y_end)
    
    return cropped_img

def update_intrinsic_matrix_for_vertical_crop(K_cropped, vertical_crop_info):
    """保持原有纵向裁剪内参更新功能"""
    top_crop, _ = vertical_crop_info
    
    K_final = K_cropped.copy()
    K_final[1, 2] -= top_crop
    
    return K_final

def vertical_crop_image(img, vertical_crop_ratio):
    """保持原有纵向裁剪功能"""
    if vertical_crop_ratio == 0:
        return img, (0, 0)
    
    h, w = img.shape[:2]
    
    total_crop_pixels = int(h * vertical_crop_ratio)
    top_crop = total_crop_pixels // 2
    bottom_crop = total_crop_pixels - top_crop
    
    if top_crop + bottom_crop >= h:
        print(f"警告: 裁剪比例过大({vertical_crop_ratio})，将使用最大可用裁剪")
        top_crop = h // 4
        bottom_crop = h // 4
    
    cropped_img = img[top_crop:h-bottom_crop, :]
    
    return cropped_img, (top_crop, bottom_crop)

def update_intrinsic_matrix(K_undistort, crop_borders):
    """保持原有裁剪边界内参更新功能"""
    x_start, y_start, _, _ = crop_borders
    K_cropped = K_undistort.copy()
    
    K_cropped[0, 2] -= x_start
    K_cropped[1, 2] -= y_start
    
    return K_cropped

def undistort_stand(img_path, K, D, DIM, scale=0.5, imshow=False):
    """保持原有标准去畸变功能"""
    img = cv2.imread(img_path)
    dim1 = img.shape[:2][::-1]
    assert dim1[0]/dim1[1] == DIM[0]/DIM[1], "Image to undistort needs same aspect ratio as calibration"
    if dim1[0] != DIM[0]:
        img = cv2.resize(img, DIM, interpolation=cv2.INTER_AREA)
    Knew = K.copy()
    if scale:
        Knew[(0,1), (0,1)] = scale * Knew[(0,1), (0,1)]
    map1, map2 = cv2.initUndistortRectifyMap(K, D, np.eye(3), Knew, DIM, cv2.CV_16SC2)
    undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    if imshow:
        cv2.imshow("undistorted", undistorted_img)
    return undistorted_img, Knew

# **修改1：添加 vehicle_type 和 logtime 参数**
def generate_sensor_json_entry(folder_name, direction, K_matrix, translation, rotation, sensor_type="camera", vehicle_type="default", logtime="no_time"):
    """
    生成传感器配置JSON条目，并添加 vehicle_type 和 logtime 字段。
    """
    token = vehicle_type + '_' + logtime
    sensor_token = folder_name
    # token = f"/sensor/{sensor_type}/{direction}"
    # sensor_token = f"/sensor/{sensor_type}/{direction}/config"
    
    entry = {
        "token": f'{token}_{sensor_token}',
        "sensor_token": sensor_token,
        "translation": translation,
        "rotation": rotation,
        "camera_intrinsic": []
    }
    
    if sensor_type == "camera" and K_matrix is not None:
        entry["camera_intrinsic"] = K_matrix.tolist()
    
    return entry

# **修改2：添加 vehicle_type 和 logtime 参数**
def generate_lidar_placeholder_entries(count=5, vehicle_type="default", logtime="no_time"):
    """
    生成LiDAR占位符条目，并添加 vehicle_type 和 logtime 字段。
    """
    lidar_entries = []

    token = f'{vehicle_type}_{logtime}'

    for topic in LIDAR_CONFIGS.keys():
        lidar_extrinsic = get_lidar_extrinsics_config_id(topic)
        r = lidar_extrinsic["ext_quaternion_xyzw"]
        entry = {
            "token": f"{token}_{topic}",
            "sensor_token": f'{topic}_config',
            "translation": lidar_extrinsic["translation"],
            "rotation": [r[3], r[0], r[1], r[2]],  # 转换为 [w, x, y, z] 格式
            # "camera_intrinsic": [],
        }
        lidar_entries.append(entry)
    return lidar_entries

def center_crop_to_resolution(img, target_resolution):
    """
    按目标分辨率中心裁剪图像（无拉伸，仅裁剪）
    :param img: 输入图像（去畸变+黑边裁剪后）
    :param target_resolution: 目标分辨率 (width, height)
    :return: 裁剪后的图像, 裁剪边界 (x_start, y_start, x_end, y_end)
    """
    img_h, img_w = img.shape[:2]
    target_w, target_h = target_resolution
    
    # 检查目标分辨率是否大于原图，若大于则返回原图（不拉伸）
    if target_w >= img_w and target_h >= img_h:
        print(f"警告: 目标分辨率{target_resolution}大于原图分辨率({img_w}, {img_h})，返回原图")
        return img, (0, 0, img_w-1, img_h-1)
    
    # 计算中心裁剪偏移量
    x_offset = (img_w - target_w) // 2
    y_offset = (img_h - target_h) // 2
    
    # 计算裁剪边界
    x_start = x_offset
    y_start = y_offset
    x_end = x_offset + target_w - 1
    y_end = y_offset + target_h - 1
    
    # 裁剪图像
    cropped_img = img[y_start:y_end+1, x_start:x_end+1]
    
    return cropped_img, (x_start, y_start, x_end, y_end)

def find_direction_folders(base_path):
    """
    在基目录下查找所有包含方向标识的文件夹
    返回格式: [(文件夹路径, 方向名称, 是否为8M相机), ...]
    """
    direction_patterns = {
        'front': r'.*3M.*front.*',
        'left': r'.*3M.*left.*', 
        'right': r'.*3M.*right.*',
        'rear': r'.*3M.*rear.*',
        'front_8M': r'.*8M_wa.*front.*',
        'rear_8M': r'.*8M.*rear.*'
    }
    
    found_dirs = []
    
    # 遍历基目录下的所有子文件夹
    for root_dir in os.listdir(base_path):
        root_path = os.path.join(base_path, root_dir)
        if not os.path.isdir(root_path):
            continue
            
        print(f"正在扫描目录: {root_path}")
        
        # 在子文件夹中查找符合方向模式的文件夹
        for item in os.listdir(root_path):
            item_path = os.path.join(root_path, item)
            if not os.path.isdir(item_path):
                continue
                
            # 检查文件夹名称是否符合方向模式
            for direction, pattern in direction_patterns.items():
                if re.match(pattern, item, re.IGNORECASE):
                    is_8M = "8M" in direction
                    found_dirs.append((item_path, direction, is_8M))
                    print(f"  找到方向文件夹: {item} -> {direction} (8M: {is_8M})")
                    break
    if not found_dirs:
        print("警告: 未找到任何方向文件夹，请检查目录结构和命名, 尝试从输入目录中直接查找")
        # 尝试从输入目录中直接查找方向文件夹
        for item in os.listdir(base_path):
            item_path = os.path.join(base_path, item)
            if not os.path.isdir(item_path):
                continue
                
            for direction, pattern in direction_patterns.items():
                if re.match(pattern, item, re.IGNORECASE):
                    is_8M = "8M" in direction
                    found_dirs.append((item_path, direction, is_8M))
                    print(f"  找到方向文件夹: {item} -> {direction} (8M: {is_8M})")
                    break
    return found_dirs

# **修改3：添加 vehicle_type 和 logtime 参数**
def generate_scale_combined_json(output_dir, scale_value, all_camera_entries, vehicle_type, logtime):
    """
    为每个scale生成包含所有相机方向和雷达预留位置的总和JSON文件
    """
    if not all_camera_entries:
        print(f"警告: scale {scale_value} 没有相机条目，跳过生成总和JSON")
        return
    
    # 复制所有相机条目
    combined_entries = all_camera_entries.copy()
    
    # 添加雷达占位符
    # **传递 vehicle_type 和 logtime**
    lidar_entries = generate_lidar_placeholder_entries(
        count=5, 
        vehicle_type=vehicle_type, 
        logtime=logtime
    )
    combined_entries.extend(lidar_entries)
    
    # 保存总和JSON文件
    json_filename = f"sensor_config_combined_scale_{scale_value}.json"
    json_path = os.path.join(output_dir, json_filename)
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(combined_entries, f, indent=4, ensure_ascii=False)
    
    print(f"已生成scale {scale_value} 总和传感器配置JSON: {json_path}")
    print(f"  - 包含 {len(all_camera_entries)} 个相机和 5 个LiDAR")

# **修改4：添加 logtime 参数**
def process_single_direction(
    direction_info, params_dir, output_base, scales, 
    crop_factor, target_resolutions, enable_resolution_crop,
    vehicle_type, # 车辆类型参数
    logtime # 新增 logtime 参数
):
    """
    处理单个方向文件夹的函数（用于并行执行）
    :param direction_info: 单个方向的信息 tuple (folder_path, direction, is_8M_camera)
    :return: 该方向的相机条目字典 {scale: [camera_entry]}
    """
    folder_path, direction, is_8M_camera = direction_info
    direction_camera_entries = defaultdict(list)
    
    try:
        # 判断是否为鱼眼相机
        is_fisheye = not is_8M_camera
        
        print(f"\n{'='*50}")
        print(f"[进程 {os.getpid()}] 处理方向: {direction}")
        print(f"  - 车辆类型: {vehicle_type}") 
        print(f"  - LogTime: {logtime}") # 打印新增参数
        print(f"  - 文件夹路径: {folder_path}")
        print(f"  - 是否为8M相机: {is_8M_camera} (使用针孔去畸变)")
        print(f"  - 是否为鱼眼相机: {is_fisheye} (使用鱼眼去畸变)")
        
        # 加载对应的内参文件（参数读取方式不变）
        if is_8M_camera:
            k_path = os.path.join(params_dir, f"camera_8M_front_K.npy")
            d_path = os.path.join(params_dir, f"camera_8M_front_D.npy")
        else:
            # 对于3M相机，去掉_8M后缀
            base_direction = direction.replace('_8M', '') if direction.endswith('_8M') else direction
            k_path = os.path.join(params_dir, f"camera_{base_direction}_3M_K.npy")
            d_path = os.path.join(params_dir, f"camera_{base_direction}_3M_D.npy")
        
        if not os.path.exists(k_path) or not os.path.exists(d_path):
            print(f"警告: {direction} 方向的参数文件不存在，跳过")
            print(f"  K文件路径: {k_path}")
            print(f"  D文件路径: {d_path}")
            return direction_camera_entries
        
        K_original = np.load(k_path)
        D = np.load(d_path)
        print(f"成功加载 {direction} 方向的参数: K.shape={K_original.shape}, D.shape={D.shape}")
        
        # 获取文件夹名称用于构建输出路径
        folder_name = os.path.basename(folder_path)
        parent_folder = os.path.basename(os.path.dirname(folder_path))
        
        # 图像目录就是找到的文件夹路径
        img_dir = folder_path
        img_extensions = ('.jpg', '.jpeg', '.png', '.bmp')
        img_files = [f for f in os.listdir(img_dir) if f.lower().endswith(img_extensions)]
        
        if not img_files:
            print(f"警告: {img_dir} 目录下未找到图片文件")
            return direction_camera_entries
        
        # 获取外参
        extrinsics = get_camera_extrinsics(direction)
        translation = extrinsics["translation"]
        r = extrinsics["rotation"] # xyzw
        rotation = [r[3], r[0], r[1], r[2]] # 转换为 wxyz
        
        for scale in scales:
            print(f"\n--- [进程 {os.getpid()}] 正在处理 scale = {scale} ---")
            
            # 构建输出目录
            # output_dir = os.path.join(output_base, parent_folder, folder_name, f"scale_{scale:.2f}")
            output_dir = os.path.join(output_base, folder_name, f"scale_{scale:.2f}")
            res_crop_dir = os.path.join(output_dir, "resolution_crops")
            os.makedirs(output_dir, exist_ok=True)
            if enable_resolution_crop:
                os.makedirs(res_crop_dir, exist_ok=True)
            
            K_cropped = None
            crop_borders = None
            K_undistort = None
            
            # 处理图像文件
            for idx, img_file in enumerate(img_files):
                img_path = os.path.join(img_dir, img_file)
                
                sample_img = cv2.imread(img_path)
                if sample_img is None:
                    print(f"跳过无法读取的图像: {img_path}")
                    continue
                h, w = sample_img.shape[:2]
                DIM = (w, h)
                
                # 根据相机类型选择去畸变方法（保持原有逻辑）
                if is_8M_camera:
                    undistorted_img, K_undistort = undistort_fish_optimized(
                        img_path, K_original, D, DIM, 2, scale=scale
                    )
                else:
                    undistorted_img, K_undistort = undistort_fish_optimized(
                        img_path, K_original, D, DIM, 1, scale=scale
                    )
                
                # 黑边裁剪（可选）
                if crop_factor > 0:
                    undistorted_img, crop_borders = crop_black_borders(
                        undistorted_img, crop_factor=crop_factor, return_borders=True
                    )
                    # 更新黑边裁剪后的内参
                    if K_undistort is not None and crop_borders is not None:
                        K_cropped = update_intrinsic_matrix(K_undistort, crop_borders)
                else:
                    crop_borders = (0, 0, undistorted_img.shape[1]-1, undistorted_img.shape[0]-1)
                    K_cropped = K_undistort.copy()
                
                # 保存去畸变原图（黑边裁剪后）
                filename, ext = os.path.splitext(img_file)
                original_output_name = f"{filename}_scale_{scale:.2f}_undistorted{ext}"
                original_output_path = os.path.join(output_dir, original_output_name)
                cv2.imwrite(original_output_path, undistorted_img)
                # print(f"[进程 {os.getpid()}] 已保存去畸变原图: {original_output_path}")
                
                # 分辨率裁剪（如果启用）
                if enable_resolution_crop:
                    for target_res in target_resolutions:
                        target_w, target_h = target_res
                        res_name = f"{target_w}x{target_h}"
                        
                        # 每个分辨率单独建文件夹
                        res_dir = os.path.join(res_crop_dir, res_name)
                        os.makedirs(res_dir, exist_ok=True)
                        
                        # 中心裁剪到目标分辨率
                        res_cropped_img, res_crop_borders = center_crop_to_resolution(
                            undistorted_img, target_res
                        )
                        
                        # 更新分辨率裁剪后的内参
                        x_start_res, y_start_res, _, _ = res_crop_borders
                        K_res_cropped = K_cropped.copy()
                        K_res_cropped[0, 2] -= x_start_res
                        K_res_cropped[1, 2] -= y_start_res
                        
                        # 保存分辨率裁剪后的图像
                        res_output_name = f"{filename}_scale_{scale:.2f}_crop_{res_name}{ext}"
                        res_output_path = os.path.join(res_dir, res_output_name)
                        cv2.imwrite(res_output_path, res_cropped_img)
                        print(f"[进程 {os.getpid()}]   - 已保存{res_name}裁剪图: {res_output_path}")
                        
                        # 保存分辨率裁剪后的内参
                        res_k_suffix = "_8M_K_res_cropped.npy" if is_8M_camera else "_3M_K_res_cropped.npy"
                        res_k_path = os.path.join(res_dir, f"camera_{direction}_scale_{scale:.2f}_{res_name}{res_k_suffix}")
                        np.save(res_k_path, K_res_cropped)
                        print(f"[进程 {os.getpid()}]   - 已保存{res_name}内参: {res_k_path}")
            
            # 保存基础内参文件
            if K_undistort is not None:
                # 原始内参
                k_original_suffix = "_8M_K_original.npy" if is_8M_camera else "_3M_K_original.npy"
                k_original_path = os.path.join(output_dir, f"camera_{direction}_scale_{scale:.2f}{k_original_suffix}")
                np.save(k_original_path, K_original)
                
                # 去畸变后内参
                k_undistort_suffix = "_8M_K_undistort.npy" if is_8M_camera else "_3M_K_undistort.npy"
                k_undistort_path = os.path.join(output_dir, f"camera_{direction}_scale_{scale:.2f}{k_undistort_suffix}")
                np.save(k_undistort_path, K_undistort)
                
                # 黑边裁剪后内参
                if K_cropped is not None:
                    k_cropped_suffix = "_8M_K_cropped.npy" if is_8M_camera else "_3M_K_cropped.npy"
                    k_cropped_path = os.path.join(output_dir, f"camera_{direction}_scale_{scale:.2f}{k_cropped_suffix}")
                    np.save(k_cropped_path, K_cropped)
                
                print(f"[进程 {os.getpid()}] 已保存原始内参: {k_original_path}")
                print(f"[进程 {os.getpid()}] 已保存去畸变后内参: {k_undistort_path}")
                if K_cropped is not None:
                    print(f"[进程 {os.getpid()}] 已保存黑边裁剪后内参: {k_cropped_path}")
            
            # 保存畸变系数
            d_suffix = "_8M_D.npy" if is_8M_camera else "_3M_D.npy"
            d_save_path = os.path.join(output_dir, f"camera_{direction}_scale_{scale:.2f}{d_suffix}")
            np.save(d_save_path, D)
            print(f"[进程 {os.getpid()}] 已保存畸变系数: {d_save_path}")
            
            # 生成基础JSON配置文件（单个方向的）
            json_entries = []
            use_K = K_cropped if K_cropped is not None else (K_undistort if K_undistort is not None else K_original)
            
            # **传递 vehicle_type 和 logtime**
            camera_entry = generate_sensor_json_entry(
                folder_name=folder_name,
                direction=direction,
                K_matrix=use_K,
                translation=translation,
                rotation=rotation,
                sensor_type="camera",
                vehicle_type=vehicle_type,
                logtime=logtime
            )
            json_entries.append(camera_entry)
            
            # **传递 vehicle_type 和 logtime**
            json_entries.extend(generate_lidar_placeholder_entries(
                count=5, 
                vehicle_type=vehicle_type, 
                logtime=logtime
            ))
            
            json_filename = f"sensor_config_{direction}_scale_{scale:.2f}.json"
            json_path = os.path.join(output_dir, json_filename)
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(json_entries, f, indent=4, ensure_ascii=False)
            
            print(f"[进程 {os.getpid()}] 已生成基础传感器配置JSON: {json_path}")
            
            # 收集这个方向的相机条目，用于后面的总和JSON
            # **传递 vehicle_type 和 logtime**
            single_camera_entry = generate_sensor_json_entry(
                folder_name=folder_name,
                direction=direction,
                K_matrix=use_K,
                translation=translation,
                rotation=rotation,
                sensor_type="camera",
                vehicle_type=vehicle_type,
                logtime=logtime
            )
            direction_camera_entries[scale].append(single_camera_entry)
            
            # 生成各分辨率的JSON配置
            if enable_resolution_crop:
                for target_res in target_resolutions:
                    target_w, target_h = target_res
                    res_name = f"{target_w}x{target_h}"
                    res_dir = os.path.join(res_crop_dir, res_name)
                    
                    # 加载该分辨率的内参
                    res_k_suffix = "_8M_K_res_cropped.npy" if is_8M_camera else "_3M_K_res_cropped.npy"
                    res_k_path = os.path.join(res_dir, f"camera_{direction}_scale_{scale:.2f}_{res_name}{res_k_suffix}")
                    if os.path.exists(res_k_path):
                        K_res = np.load(res_k_path)
                        
                        # 生成该分辨率的JSON
                        # **传递 vehicle_type 和 logtime**
                        res_json_entry = generate_sensor_json_entry(
                            folder_name=folder_name,
                            direction=f"{direction}_{res_name}",
                            K_matrix=K_res,
                            translation=translation,
                            rotation=rotation,
                            sensor_type="camera",
                            vehicle_type=vehicle_type,
                            logtime=logtime
                        )
                        # **传递 vehicle_type 和 logtime**
                        res_json_entries = [res_json_entry] + generate_lidar_placeholder_entries(
                            count=5, 
                            vehicle_type=vehicle_type, 
                            logtime=logtime
                        )
                        
                        res_json_path = os.path.join(res_dir, f"sensor_config_{direction}_scale_{scale:.2f}_{res_name}.json")
                        with open(res_json_path, 'w', encoding='utf-8') as f:
                            json.dump(res_json_entries, f, indent=4, ensure_ascii=False)
                        print(f"[进程 {os.getpid()}]   - 已生成{res_name}传感器配置JSON: {res_json_path}")
            
            print(f"--- [进程 {os.getpid()}] scale = {scale} 处理完成 ---")
            
    except Exception as e:
        print(f"[进程 {os.getpid()}] 处理 {direction} 方向时出错: {str(e)}")
        import traceback
        traceback.print_exc()
    
    return direction_camera_entries

# **修改5：添加 logtime 参数**
def process_all_directions(
    base_path, params_dir, output_base, 
    scale_min=0.3, scale_max=0.8, scale_step=0.1, 
    crop_factor=0.02, 
    target_resolutions=None,
    enable_resolution_crop=True,
    vehicle_type="default", # 车辆类型参数
    logtime="no_time" # 新增 logtime 参数
):
    """
    并行处理所有方向文件夹
    """
    # 初始化默认分辨率列表
    if target_resolutions is None:
        target_resolutions = [(1920, 1080), (1280, 720), (800, 600)]
    print(f"目标分辨率列表: {target_resolutions}")
    print(f"是否启用分辨率裁剪: {enable_resolution_crop}")
    print(f"车辆类型: {vehicle_type}")
    print(f"LogTime: {logtime}") # 打印新增参数
    
    scales = np.arange(scale_min, scale_max + scale_step/2, scale_step)
    scales = [round(scale, 2) for scale in scales]
    print(f"将使用以下scale值进行处理: {scales}")
    print(f"并行进程数: {MAX_WORKERS}")
    
    # 查找所有包含方向标识的文件夹
    direction_folders = find_direction_folders(base_path)
    if not direction_folders:
        print("未找到任何包含方向标识的文件夹！")
        return
    
    print(f"\n总共找到 {len(direction_folders)} 个方向文件夹")
    
    # 用于存储所有方向的相机条目
    scale_camera_entries = defaultdict(list)
    
    # 使用进程池并行处理每个方向文件夹
    with ProcessPoolExecutor(max_workers=MAX_WORKERS) as executor:
        # 提交所有任务
        future_to_direction = {}
        for direction_info in direction_folders:
            future = executor.submit(
                process_single_direction,
                direction_info=direction_info,
                params_dir=params_dir,
                output_base=output_base,
                scales=scales,
                crop_factor=crop_factor,
                target_resolutions=target_resolutions,
                enable_resolution_crop=enable_resolution_crop,
                vehicle_type=vehicle_type, # 传递 vehicle_type 参数
                logtime=logtime # 传递 logtime 参数
            )
            future_to_direction[future] = direction_info[1]  # 存储方向名称
        
        # 处理完成的任务
        for future in as_completed(future_to_direction):
            direction_name = future_to_direction[future]
            try:
                # 获取该方向的处理结果（相机条目字典）
                direction_entries = future.result()
                # 合并到全局的相机条目字典中
                for scale, entries in direction_entries.items():
                    scale_camera_entries[scale].extend(entries)
                print(f"\n{'='*50}")
                print(f"方向 {direction_name} 并行处理完成！")
                print(f"{'='*50}")
            except Exception as e:
                print(f"\n{'='*50}")
                print(f"方向 {direction_name} 并行处理失败: {str(e)}")
                print(f"{'='*50}")
    
    # 为每个scale生成总和JSON文件
    print(f"\n{'='*50}")
    print("开始生成每个scale的总和JSON文件")
    print(f"{'='*50}")
    
    for scale in scales:
        if scale in scale_camera_entries and scale_camera_entries[scale]:
            # 创建总和JSON的输出目录（放在输出根目录下）
            combined_output_dir = os.path.join(output_base, f"combined_scales")
            os.makedirs(combined_output_dir, exist_ok=True)
            
            # **传递 vehicle_type 和 logtime**
            generate_scale_combined_json(
                combined_output_dir, 
                f"{scale:.2f}", 
                scale_camera_entries[scale],
                vehicle_type=vehicle_type,
                logtime=logtime
            )
        else:
            print(f"警告: scale {scale} 没有找到任何相机条目，跳过生成总和JSON")

def generate_combined_json(
    output_base, 
    include_resolution_crops=False
):
    """
    生成综合JSON文件 - 根据新的目录结构调整
    """
    print("注意：由于目录结构变化，需要重新实现generate_combined_json函数")
    print("当前版本使用新的总和JSON生成方式")
    
    # 查找所有combined_scales目录下的JSON文件
    combined_dir = os.path.join(output_base, "combined_scales")
    if not os.path.exists(combined_dir):
        print(f"未找到combined_scales目录: {combined_dir}")
        return
    
    json_files = [f for f in os.listdir(combined_dir) if f.startswith("sensor_config_combined_scale_") and f.endswith(".json")]
    
    if not json_files:
        print("在combined_scales目录下未找到任何总和JSON文件")
        return
    
    # 找到最新的scale文件
    # 提取scale值进行比较
    def extract_scale(filename):
        match = re.search(r'_scale_(\d+\.\d+)\.json$', filename)
        return float(match.group(1)) if match else -1

    json_files.sort(key=extract_scale, reverse=True)
    latest_json = json_files[0]
    latest_json_path = os.path.join(combined_dir, latest_json)
    
    # 复制最新的总和JSON作为主配置文件
    main_config_path = os.path.join(output_base, "sensor_config_combined_latest.json")
    
    with open(latest_json_path, 'r', encoding='utf-8') as f:
        config_data = json.load(f)
    
    with open(main_config_path, 'w', encoding='utf-8') as f:
        json.dump(config_data, f, indent=4, ensure_ascii=False)
    
    print(f"已生成主配置文件: {main_config_path} (基于 {latest_json})")

def main():
    parser = argparse.ArgumentParser(description="图像去畸变批量处理程序（并行版 + 总和JSON）")
    
    # 1. 路径参数 (已修改)
    parser.add_argument(
        '--images', 
        type=str, 
        required=True, 
        help="图像根目录 (对应原 base_images_path)"
    )
    parser.add_argument(
        '--params', 
        type=str, 
        required=True, 
        help="相机内参文件路径 (对应原 base_params_path)"
    )
    parser.add_argument(
        '--out', 
        type=str, 
        required=True, 
        help="输出文件根目录 (对应原 output_path)"
    )
    
    # 2. 新增的参数 (已修改)
    parser.add_argument(
        '--vehicle',
        type=str,
        default="default",
        help="车辆类型标识，可用于区分不同车型的内参配置（可选，默认为'default'）"
    )
    # **新增的 logtime 参数**
    parser.add_argument(
        '--logtime',
        type=str,
        default="no_time",
        help="用于标识日志文件或批次的唯一时间戳/ID（可选，默认为'no_time'）"
    )
    
    # 原始代码中的固定/可配置参数（可以考虑也改为命令行参数）
    # 这里保持为固定值，但使用新的变量名
    parser.add_argument('--scale_min', type=float, default=0.2, help="Scale最小值")
    parser.add_argument('--scale_max', type=float, default=0.2, help="Scale最大值")
    parser.add_argument('--scale_step', type=float, default=0.1, help="Scale步长")
    parser.add_argument('--crop_factor', type=float, default=0.0, help="黑边裁剪比例 (0表示不裁剪)")
    parser.add_argument('--enable_res_crop', type=bool, default=False, help="是否启用分辨率裁剪")

    args = parser.parse_args()

    # 从命令行参数读取路径
    base_images_path = args.images
    base_params_path = args.params
    output_path = args.out
    vehicle_type = args.vehicle # 车辆类型参数
    logtime = args.logtime # 新增 LogTime 参数

    # 其他固定配置
    SCALE_MIN = args.scale_min
    SCALE_MAX = args.scale_max
    SCALE_STEP = args.scale_step
    CROP_FACTOR = args.crop_factor
    ENABLE_RESOLUTION_CROP = args.enable_res_crop
    
    TARGET_RESOLUTIONS = [
        (1920, 1080),   # 1080P
        (2112, 768),    # 720P
    ]
    INCLUDE_RES_IN_COMBINED_JSON = True # 保持原样，但实际逻辑中没有使用这个变量
    
    print("="*60)
    print("图像去畸变批量处理程序（并行版 + 总和JSON）")
    print("="*60)
    print(f"车辆类型: {vehicle_type}") 
    print(f"LogTime: {logtime}") # 打印新增参数
    print(f"Scale设置: 最小值={SCALE_MIN}, 最大值={SCALE_MAX}, 步长={SCALE_STEP}")
    print(f"黑边裁剪设置: 比例={CROP_FACTOR}")
    print(f"分辨率裁剪设置: {'启用' if ENABLE_RESOLUTION_CROP else '禁用'}")
    print(f"目标分辨率: {TARGET_RESOLUTIONS}")
    print(f"图像根目录: {base_images_path}")
    print(f"参数路径: {base_params_path}")
    print(f"输出路径: {output_path}")
    print(f"并行进程数: {MAX_WORKERS}")
    print("="*60)
    print("新的文件处理逻辑：")
    print("1. 自动扫描根目录下的所有子文件夹")
    print("2. 在子文件夹中查找包含方向标识的文件夹")
    print("3. 并行处理各个方向文件夹（不修改核心处理逻辑）")
    print("4. 按照原始文件夹结构保存结果")
    print("5. 为每个scale生成总和JSON文件（包含所有相机方向和雷达）")
    print("="*60)
    
    # 批量处理
    process_all_directions(
        base_path=base_images_path, 
        params_dir=base_params_path, 
        output_base=output_path,
        scale_min=SCALE_MIN,
        scale_max=SCALE_MAX,
        scale_step=SCALE_STEP,
        crop_factor=CROP_FACTOR,
        target_resolutions=TARGET_RESOLUTIONS,
        enable_resolution_crop=ENABLE_RESOLUTION_CROP,
        vehicle_type=vehicle_type, # 传递新增参数
        logtime=logtime # 传递新增参数
    )
    
    # 生成主配置文件
    generate_combined_json(output_base=output_path)
    
    print("\n" + "="*60)
    print("所有处理已完成！")
    print("输出目录结构：")
    print("save/")
    print("  ├─ combined_scales/")
    print("  │  ├─ sensor_config_combined_scale_0.10.json  # 每个scale的总和JSON")
    print("  │  ├─ sensor_config_combined_scale_0.20.json")
    print("  │  └─ ...")
    print("  ├─ sensor_config_combined_latest.json  # 主配置文件")
    print("  ├─ [父文件夹1]/")
    print("  │  ├─ [原始方向文件夹1]/")
    print("  │  │  ├─ [方向]/")
    print("  │  │  │  ├─ scale_xx/")
    print("  │  │  │  │  ├─ [图像]_undistorted.xxx")
    print("  │  │  │  │  ├─ camera_xxx_K_*.npy")
    print("  │  │  │  │  ├─ sensor_config_[方向]_scale_xx.json  # 单个方向JSON")
    print("  │  │  │  │  └─ resolution_crops/")
    print("  │  ├─ [原始方向文件夹2]/")
    print("  │  │  └─ ...")
    print("  ├─ [父文件夹2]/")
    print("  │  └─ ...")
    print("="*60)

if __name__ == '__main__':
    # Windows系统需要添加这行代码（可选）
    # multiprocessing.freeze_support()
    
    main()