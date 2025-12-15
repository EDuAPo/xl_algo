#!/usr/bin/env python3

import os
import argparse
import sys
import numpy as np
import open3d as o3d 
import re
from concurrent.futures import ProcessPoolExecutor, as_completed
import multiprocessing

# 从 lidar_to_image.py 导入 LIDAR_MAP
try:
    from lidar_to_image import LIDAR_MAP 
except ImportError:
    print("❌ 致命错误: 无法导入 lidar_to_image.py 中的 LIDAR_MAP。请检查路径。")
    sys.exit(1)

# 创建一个反向映射表：Config ID (长名称) -> Short Name (短名称)
REVERSE_LIDAR_MAP = {v: k for k, v in LIDAR_MAP.items()}

# 设置进程池的最大工作进程数
MAX_WORKERS = multiprocessing.cpu_count()

# ======================================================================
# 【新增】颜色配置: 用于区分合并后的点云来源
# 颜色值为 RGB (0.0 - 1.0)。请根据您的 Lidar ID 调整颜色。
# ======================================================================
LIDAR_COLOR_MAP = {
    # 示例 Lidar ID (Config ID) 及其颜色
    "iv_points_front_left":  [1.0, 0.0, 0.0],  # 红色 (Red)
    "iv_points_front_right": [0.0, 1.0, 0.0],  # 绿色 (Green)
    "iv_points_rear_left":   [0.0, 0.0, 1.0],  # 蓝色 (Blue)
    "iv_points_rear_right":  [1.0, 0.0, 1.0],  # 黄色 (Yellow)
    "iv_points_front_mid":   [0.0, 1.0, 1.0],  # 青色 (Cyan)
    # 确保您的所有 Lidar ID 都在这里有对应的颜色
}

# ======================================================================
# 辅助函数
# ======================================================================

def extract_time_id(filename: str) -> int:
    """
    从文件名中提取完整的数字串作为时间ID。
    """
    base_name = os.path.splitext(filename)[0]
    time_id_str = re.sub(r'[^0-9]', '', base_name)
    
    if time_id_str:
        # 使用完整的数字串作为时间 ID
        return int(time_id_str)
    return -1

# 【修改】函数签名和返回值，以包含颜色逻辑
def load_pcd_points(file_path: str, config_id: str) -> tuple[np.ndarray, np.ndarray]:
    """
    加载 PCD 或 BIN 文件中的点云数据，并根据 config_id 为所有点分配颜色。
    
    返回: (点坐标 [N, 3], 点颜色 [N, 3])
    """
    ext = os.path.splitext(file_path)[1].lower()
    points = None

    if ext == '.pcd':
        pcd = o3d.io.read_point_cloud(file_path)
        if not pcd.has_points():
             return np.array([]), np.array([])
        # 假设 PCD 文件中没有自带颜色，只提取坐标
        points = np.asarray(pcd.points) 

    elif ext == '.bin':
        data = np.fromfile(file_path, dtype=np.float32)
        K = 4 
        if data.size % K != 0:
            K = 5
            if data.size % K != 0:
                raise ValueError(f"二进制文件大小不符合常见格式 (K=4 或 K=5)。")
            
        points_reshaped = data.reshape((-1, K))
        points = points_reshaped[:, :3].astype(np.float64) 

    else:
        raise ValueError(f"不支持的点云文件扩展名: {ext}。仅支持 .pcd 或 .bin。")
    
    if points is None or points.size == 0:
        return np.array([]), np.array([])

    # 清理 NaNs 和 Infs
    points = points[~np.isnan(points).any(axis=1)]
    points = points[~np.isinf(points).any(axis=1)]
    
    if points.size == 0:
        return np.array([]), np.array([])

    num_points = points.shape[0]
    
    # 【新增颜色逻辑】
    # 查找对应的颜色，如果未找到，使用默认的灰色 [0.5, 0.5, 0.5]
    color_rgb = np.array(LIDAR_COLOR_MAP.get(config_id, [0.5, 0.5, 0.5]))
    
    # 为所有点生成相同的颜色数组 [N, 3]
    colors = np.tile(color_rgb, (num_points, 1))

    return points, colors


# ======================================================================
# 核心合并函数 (单个任务) 
# ======================================================================

# 【修改】函数内部逻辑，以处理颜色
def merge_and_save_frame(matched_files: list, output_path: str, base_filename: str):
    """
    合并一组匹配到的点云文件并保存，同时添加颜色信息进行区分。
    """
    all_points = []
    all_colors = [] # 【新增】用于存储所有传感器的颜色
    
    try:
        if not matched_files:
            raise ValueError("没有文件需要合并。")

        for pcd_path, lidar_id in matched_files:
            # 【修改点 A】调用 load_pcd_points 时传入 lidar_id，并接收 points 和 colors
            points, colors = load_pcd_points(pcd_path, lidar_id) 
            
            if points.size == 0:
                print(f"⚠️ 警告: 文件 {os.path.basename(pcd_path)} 为空或清理后为空，跳过。")
                continue
                
            all_points.append(points)
            all_colors.append(colors) # 【修改点 B】添加颜色数据到列表
        
        if not all_points:
            raise ValueError("所有点云文件均为空或加载失败。")

        merged_points = np.concatenate(all_points, axis=0)
        merged_colors = np.concatenate(all_colors, axis=0) # 【修改点 C】合并颜色
        
        pcd_merged = o3d.geometry.PointCloud()
        pcd_merged.points = o3d.utility.Vector3dVector(merged_points)
        
        # 【修改点 D】设置点云颜色
        pcd_merged.colors = o3d.utility.Vector3dVector(merged_colors)
        
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        # 默认保存为二进制格式，如果需要 ASCII，可以添加 write_ascii=True
        o3d.io.write_point_cloud(output_path, pcd_merged, write_ascii=False) 
        
        file_count = len(matched_files)
        point_count = merged_points.shape[0]
        
        return f"✅ 成功合并 {file_count} 个文件 ({point_count} 个点, 包含颜色)，保存为 {os.path.basename(output_path)}"

    except Exception as e:
        return f"❌ 合并帧 {base_filename} 失败: {str(e)}"

# ======================================================================
# 主控制函数 (保持不变)
# ======================================================================

def main():
    parser = argparse.ArgumentParser(
        description="批量合并自车坐标系下的点云文件。",
        epilog="请确保输入目录包含以 Lidar 配置ID命名的子目录。"
    )
    
    # 1. 输入和输出目录
    parser.add_argument("--pcd", type=str, required=True, help="包含自车坐标系点云文件的根目录 (pcd_to_vehicle_converter.py 的输出目录)。")
    parser.add_argument("--out", type=str, required=True, help="合并后的点云文件保存的根目录。")
    
    # 2. 合并模式 (互斥组)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--all", action="store_true", help="合并所有找到的激光雷达的点云文件。")
    group.add_argument("--two", nargs=2, type=str, choices=list(LIDAR_MAP.keys()), 
                        help="指定要合并的两个激光雷达的简称 (例如 front_left rear_right)。")
    
    parser.add_argument("--workers", type=int, default=MAX_WORKERS, help="并行处理任务的进程数（默认CPU核心数）。")

    args = parser.parse_args()
    
    input_base_dir = os.path.abspath(args.pcd)
    output_root_dir = os.path.abspath(args.out)
    
    if not os.path.isdir(input_base_dir):
        print(f"❌ 错误: 输入目录 '{input_base_dir}' 不存在。")
        sys.exit(1)

    print("="*60)
    print("🚀 点云合并处理启动 (使用多进程)...")
    print(f"输入目录: {input_base_dir}")

    # 1. 确定初始目标 Lidar 集合和输出子目录
    initial_target_ids = []
    output_subdir_name = ""
    
    if args.all:
        initial_target_ids = list(LIDAR_MAP.values())
        output_subdir_name = "all"
        print("模式: 合并所有激光雷达。")
    
    elif args.two:
        lidar_short_names = sorted(args.two)
        
        if not all(name in LIDAR_MAP for name in lidar_short_names):
            print(f"❌ 错误: 指定的激光雷达简称 {args.two} 中有无效名称。")
            sys.exit(1)
            
        initial_target_ids = [LIDAR_MAP[name] for name in lidar_short_names]
        output_subdir_name = "_".join(lidar_short_names)
        print(f"模式: 合并指定的两个激光雷达: {output_subdir_name}。")
    
    output_final_dir = os.path.join(output_root_dir, output_subdir_name)
    
    # 2. 收集所有目标文件及其时间戳
    all_files_data = [] # 格式: (time_id, pcd_path, config_id)
    found_config_ids = set() # 【新增】跟踪实际找到文件的 Lidar ID
    
    for config_id in initial_target_ids:
        lidar_dir = os.path.join(input_base_dir, config_id)
        
        # 打印警告，但继续尝试查找其他目录
        if not os.path.isdir(lidar_dir):
            print(f"⚠️ 警告: 找不到 Lidar ID 目录 '{lidar_dir}'，跳过。")
            continue
            
        for filename in os.listdir(lidar_dir):
            if filename.lower().endswith(('.pcd', '.bin')):
                pcd_path = os.path.join(lidar_dir, filename)
                time_id = extract_time_id(filename)
                if time_id > 0:
                    all_files_data.append((time_id, pcd_path, config_id))
                    found_config_ids.add(config_id) # 记录成功找到文件的 Lidar ID

    if not all_files_data:
        print("❌ 错误: 在指定的输入目录下未找到任何点云文件进行合并。")
        sys.exit(1)
        
    all_files_data.sort(key=lambda x: x[0]) # 按时间 ID 排序
    print(f"找到 {len(all_files_data)} 个点云文件。")
    
    # 3. 更新目标 Lidar ID 列表
    # 只有找到了文件的传感器才需要进行同步匹配
    target_config_ids = sorted(list(found_config_ids)) 
    required_sensor_ids = set(target_config_ids)
    
    if args.all and len(target_config_ids) < len(initial_target_ids):
        print(f"⚠️ 警告: 在 `--all` 模式下，实际仅找到 {len(target_config_ids)}/{len(initial_target_ids)} 个激光雷达的有效数据。")
        print(f"实际合并的传感器ID: {target_config_ids}")
    
    if not target_config_ids:
        print("❌ 错误: 未找到任何有效的激光雷达数据进行合并。")
        sys.exit(1)
        
    print(f"结果将保存到: {output_final_dir}")
    print("="*60)

    # 4. 同步匹配 (核心逻辑)
    TIME_TOLERANCE_ID = 20 # 20毫秒容忍度
    
    frames_to_merge = [] # 格式: [(pcd_path, config_id), ...]
    current_frame = []
    
    for time_id, pcd_path, config_id in all_files_data:
        if not current_frame:
            current_frame.append((pcd_path, config_id))
            continue
        
        earliest_time_id = extract_time_id(os.path.basename(current_frame[0][0]))
        
        # 检查时间是否在容忍范围内
        if abs(time_id - earliest_time_id) < TIME_TOLERANCE_ID:
            current_sensor_ids = {item[1] for item in current_frame}
            # 如果当前帧中已包含该传感器的点云，则跳过（避免重复）
            if config_id not in current_sensor_ids:
                current_frame.append((pcd_path, config_id))
            else:
                print(f"⚠️ 警告: 在时间ID {time_id} 处，传感器 {config_id} 的点云已存在于当前帧，跳过重复文件。")
        else:
            # 时间差太大，当前帧结束
            current_sensor_ids = {item[1] for item in current_frame}
            
            # 检查当前帧是否包含了所有【实际找到的】目标传感器
            if current_sensor_ids == required_sensor_ids: 
                frames_to_merge.append(current_frame)
            else:
                print(f"⚠️ 警告: 时间ID {earliest_time_id} 处的帧缺少部分传感器，跳过。包含传感器: {sorted(list(current_sensor_ids))}。")
            
            # 开启新的一帧，并加入当前文件
            current_frame = [(pcd_path, config_id)]

    # 处理最后一个帧
    if current_frame:
        current_sensor_ids = {item[1] for item in current_frame}
        if current_sensor_ids == required_sensor_ids:
             frames_to_merge.append(current_frame)


    print(f"✅ 找到 {len(frames_to_merge)} 组同步帧进行合并。")
    
    if not frames_to_merge:
        print("⚠️ 警告: 找不到满足所有目标 Lidar (必须全部同步) 的同步帧。")
        sys.exit(0)

    # 5. 并行执行合并任务
    tasks = []
    for frame in frames_to_merge:
        # 使用帧中最早的文件名作为输出文件名
        base_filename = os.path.basename(frame[0][0]) 
        output_pcd_path = os.path.join(output_final_dir, base_filename)
        tasks.append((frame, output_pcd_path, base_filename))
        
    with ProcessPoolExecutor(max_workers=args.workers) as executor:
        future_to_frame = {
            executor.submit(merge_and_save_frame, matched_files, out_path, base_name): base_name
            for matched_files, out_path, base_name in tasks
        }
        
        for i, future in enumerate(as_completed(future_to_frame)):
            base_name = future_to_frame[future]
            try:
                result = future.result()
                print(f"[{i+1}/{len(tasks)}] {result}")
            except Exception as e:
                print(f"[{i+1}/{len(tasks)}] ❌ 合并 {base_name} 时发生未预期的错误: {e}")
                
    print("\n" + "="*60)
    print("🎉 所有点云合并处理完成！")
    print(f"合并后的点云保存在: {output_final_dir}")
    print("="*60)

if __name__ == '__main__':
    main()