#!/usr/bin/env python3

import os
import argparse
import sys
import numpy as np
# 确保您的环境中安装了 open3d (pip install open3d)
import open3d as o3d 
from scipy.spatial.transform import Rotation as R
from concurrent.futures import ProcessPoolExecutor, as_completed
import multiprocessing
from pathlib import Path
current_dir = Path(__file__).resolve().parent
workspace_dir = current_dir.parent
if str(workspace_dir) not in sys.path:
    sys.path.append(str(workspace_dir))

# 从 lidar_to_image.py 及其依赖中导入所需的配置和映射
try:
    # 尝试从 lidar_to_image 导入 LIDAR_MAP (包含 short_name -> config_id 映射)
    from lidar_to_image import LIDAR_MAP 
except ImportError:
    print("❌ 致命错误: 无法导入 lidar_to_image.py 中的 LIDAR_MAP。请检查路径。")
    sys.exit(1)

try:
    # 从 lidar_calibrator.py 导入配置，这是必需的
    from config.lidar_calibrator import LIDAR_CONFIGS, ANGLES_IN_DEGREES, get_lidar_to_vehicle_transform
except ImportError:
    print("❌ 致命错误: 无法导入 lidar_calibrator.py 中的 LIDAR_CONFIGS 和 ANGLES_IN_DEGREES。请检查路径。")
    sys.exit(1)

# 获取所有有效的 Lidar 配置 ID (即 LIDAR_MAP 的值集合)
LIDAR_IDS = set(LIDAR_MAP.values())

# 固定的内部子目录名称
PCD_SUBDIR_NAME = "pcd_binary"

# 设置进程池的最大工作进程数
MAX_WORKERS = multiprocessing.cpu_count()

def read_lidar_points(file_path: str) -> np.ndarray:
    """
    根据文件扩展名自动读取点云数据 (.pcd 或 .bin)。
    """
    ext = os.path.splitext(file_path)[1].lower()
    points = None

    if ext == '.pcd':
        pcd = o3d.io.read_point_cloud(file_path)
        if not pcd.has_points():
             raise ValueError("PCD 文件中没有点数据。")
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
        raise ValueError("读取的点云数据为空。")

    points = points[~np.isnan(points).any(axis=1)]
    points = points[~np.isinf(points).any(axis=1)]

    return points

# ======================================================================
# 核心转换函数 (单个任务)
# (保持不变)
# ======================================================================

def transform_and_save_pcd(pcd_path: str, lidar_id: str, output_subdir: str):
    """
    单个任务：转换单个点云文件从 Lidar 坐标系到自车坐标系，并保存。
    :param lidar_id: 激光雷达的配置ID（如 "iv_points_front_left"）。
    """
    try:
        # 1. 获取变换矩阵 T_L_V
        T_L_V = get_lidar_to_vehicle_transform(lidar_id)
        
        # 2. 读取点云
        points_lidar = read_lidar_points(pcd_path)
        
        # 3. 转换到自车坐标系 (Vehicle Coordinate System, VCS)
        points_homogeneous_lidar = np.hstack((points_lidar, np.ones((points_lidar.shape[0], 1))))
        points_vehicle = (T_L_V @ points_homogeneous_lidar.T).T[:, :3] 
        
        # 4. 构造输出路径
        filename = os.path.basename(pcd_path)
        output_pcd_path = os.path.join(output_subdir, filename)
        
        # 5. 保存为 PCD 文件
        pcd_vehicle = o3d.geometry.PointCloud()
        pcd_vehicle.points = o3d.utility.Vector3dVector(points_vehicle)
        
        os.makedirs(output_subdir, exist_ok=True)
        o3d.io.write_point_cloud(output_pcd_path, pcd_vehicle)
        
        return f"✅ 成功转换并保存 {filename} ({points_vehicle.shape[0]} 个点) 到 {output_pcd_path}"

    except Exception as e:
        return f"❌ 转换 {os.path.basename(pcd_path)} 失败 (Lidar ID: {lidar_id}): {str(e)}"

# ======================================================================
# 主控制函数
# ======================================================================

def main():
    parser = argparse.ArgumentParser(
        description="批量将激光雷达坐标系下的点云转换为自车坐标系下的点云。",
        epilog=f"点云数据必须位于以 Lidar 配置ID命名的子目录中，且每个子目录下需包含一个 '{PCD_SUBDIR_NAME}' 目录。"
    )
    
    parser.add_argument("--pcd", type=str, required=True, help="包含激光雷达子目录（以配置ID命名）的根目录。")
    parser.add_argument("--out", type=str, default=None, help="输出文件根目录。如果未指定，默认为 --pcd/vehicle_pcd。")
    parser.add_argument("--workers", type=int, default=MAX_WORKERS, help="并行处理任务的进程数（默认CPU核心数）。")

    args = parser.parse_args()
    
    # 1. 确定输入和输出目录
    input_pcd_dir = os.path.abspath(args.pcd)
    if args.out is None:
        output_base_dir = os.path.join(input_pcd_dir, "vehicle_pcd")
    else:
        output_base_dir = os.path.abspath(args.out)
    
    if not os.path.isdir(input_pcd_dir):
        print(f"❌ 错误: 输入目录 '{input_pcd_dir}' 不存在。")
        sys.exit(1)

    print("="*60)
    print("🚀 点云坐标系批量转换启动 (使用多进程)...")
    print(f"输入目录: {input_pcd_dir}")
    print(f"输出目录: {output_base_dir}")
    print(f"并行进程数: {args.workers}")
    print(f"子目录结构: [Lidar ID]/-> {PCD_SUBDIR_NAME}/-> [PCD文件]")
    print("="*60)

    # 2. 查找任务
    tasks = []
    
    # 遍历输入目录下的所有子目录 (Lidar ID 目录)
    for subdir_name in os.listdir(input_pcd_dir):
        if subdir_name in LIDAR_IDS:
            lidar_id = subdir_name # Lidar ID，例如 'iv_points_front_left'
            
            # 构造实际的点云文件所在目录路径
            input_subdir = os.path.join(input_pcd_dir, lidar_id, PCD_SUBDIR_NAME)
            
            # 构造输出目录路径，输出仍保持 Lidar ID 目录结构，不需要 pcd_binary 这一层
            output_subdir = os.path.join(output_base_dir, lidar_id) 
            
            if not os.path.isdir(input_subdir):
                print(f"⚠️ 警告: 找不到路径 '{input_subdir}'，跳过 Lidar ID: {lidar_id}。")
                continue
                
            # 查找点云文件
            for filename in os.listdir(input_subdir):
                if filename.lower().endswith(('.pcd', '.bin')):
                    pcd_path = os.path.join(input_subdir, filename)
                    # 任务： (pcd_path, lidar_id, output_subdir)
                    tasks.append((pcd_path, lidar_id, output_subdir))

    if not tasks:
        print(f"⚠️ 警告: 未在指定结构 '{input_pcd_dir}/[Lidar ID]/{PCD_SUBDIR_NAME}/' 中找到任何点云文件。")
        sys.exit(0)

    print(f"✅ 找到 {len(tasks)} 个转换任务。开始并行处理...")

    # 3. 并行处理 (使用 ProcessPoolExecutor)
    with ProcessPoolExecutor(max_workers=args.workers) as executor:
        # 提交所有任务
        future_to_pcd = {
            executor.submit(transform_and_save_pcd, pcd, lidar_id, out_dir): pcd
            for pcd, lidar_id, out_dir in tasks
        }
        
        # 收集结果并实时打印
        for i, future in enumerate(as_completed(future_to_pcd)):
            pcd_path = future_to_pcd[future]
            try:
                result = future.result()
                print(f"[{i+1}/{len(tasks)}] {result}")
            except Exception as e:
                print(f"[{i+1}/{len(tasks)}] ❌ 处理 {os.path.basename(pcd_path)} 时发生未预期的错误: {e}")
                
    print("\n" + "="*60)
    print("🎉 所有点云转换处理完成！")
    print(f"转换后的点云保存在: {output_base_dir}")
    print("="*60)

if __name__ == '__main__':
    main()