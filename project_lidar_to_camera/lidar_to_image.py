import numpy as np
import open3d as o3d # 用于读取PCD文件
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import argparse
import sys
import os
import cv2 # 导入 OpenCV 库
from scipy.spatial.transform import Rotation as R
from typing import Dict, List, Tuple

from pathlib import Path
current_dir = Path(__file__).resolve().parent
workspace_dir = current_dir.parent
print(f"🔧 正在将配置目录添加到 sys.path: {workspace_dir}")
if str(workspace_dir) not in sys.path:
    sys.path.append(str(workspace_dir))

# 导入自定义的标定模块 (假设这些文件存在于您的环境中)
from config.lidar_calibrator import LIDAR_CONFIGS, ANGLES_IN_DEGREES, get_lidar_to_vehicle_transform
from config.camera_calibrator import CAMERA_CONFIGS, CAMERA_ANGLES_IN_DEGREES, STANDARD_CAMERAS_IDS, \
                               get_camera_extrinsics_matrix, get_camera_intrinsics_matrix, \
                               get_camera_distortion_coefficients, is_fisheye_camera
from config.global_mapping import LIDAR_MAP, CAMERA_MAP, LIDAR_CAMERA_MAP

# 选择要使用的激光雷达ID。将在 main 函数中根据 --lidar 参数动态设置。
LIDAR_ID_TO_USE = None 

# 选择要使用的相机ID (从 camera_calibrator.py 中获取)
CAMERA_ID_TO_USE = None

# 可视化参数
POINT_SIZE = 0.5      # 投影点的大小
POINT_ALPHA = 0.3   # 投影点的透明度
COLOR_MAP = 'viridis' # 用于点云深度的颜色映射


# ======================================================================
# 新增函数：根据文件扩展名读取点云数据
# ======================================================================

def read_lidar_points(file_path: str) -> np.ndarray:
    """
    根据文件扩展名自动读取点云数据 (.pcd 或 .bin)。
    """
    ext = os.path.splitext(file_path)[1].lower()
    points = None

    print(f"📖 正在读取 {ext} 文件: {file_path}")

    if ext == '.pcd':
        try:
            pcd = o3d.io.read_point_cloud(file_path)
            if not pcd.has_points():
                 raise ValueError("PCD 文件中没有点数据。")
            points = np.asarray(pcd.points)
        except Exception as e:
            raise Exception(f"读取 PCD 文件失败: {e}")

    elif ext == '.bin':
        try:
            data = np.fromfile(file_path, dtype=np.float32)
            # K=5 已经确认是您的导出格式：[x, y, z, intensity, timestamp]
            # 注意：这里的 K 必须与您导出时的字段数 K 严格匹配！
            K = 5 
            if data.size % K != 0:
                print(f"⚠️ 警告: 二进制文件大小 ({data.size}) 不是 {K} 的倍数。可能 K 值需要调整。")
            
            points_reshaped = data.reshape((-1, K))
            points = points_reshaped[:, :3].astype(np.float64) # 只取 x, y, z
        except Exception as e:
            raise Exception(f"读取 BIN 文件失败: {e}")

    else:
        raise ValueError(f"不支持的点云文件扩展名: {ext}。仅支持 .pcd 或 .bin。")
    
    if points is None or points.size == 0:
        raise ValueError("读取的点云数据为空。")

    points = points[~np.isnan(points).any(axis=1)]
    points = points[~np.isinf(points).any(axis=1)]

    print(f"✅ 成功读取 {points.shape[0]} 个点。")
    return points

# ======================================================================
# 核心投影函数
# ======================================================================

def project_lidar_to_image(pcd_file_path: str, image_file_path: str, lidar_id: str, camera_id: str, save_mode: bool, output_dir: str = None):
    """
    主函数：读取 PCD/BIN 文件和图像，将点云投影到图像上并可视化/保存。
    """
    # 检查 lidar_id 是否已设置
    LIDAR_ID_TO_USE = LIDAR_MAP[lidar_id]
    if LIDAR_ID_TO_USE is None:
         raise RuntimeError("LIDAR_ID_TO_USE 尚未设置。请使用 --lidar 参数指定激光雷达。")
    
    # 检查 camera_id 是否已设置
    CAMERA_ID_TO_USE = CAMERA_MAP[camera_id]
    if CAMERA_ID_TO_USE is None:
         raise RuntimeError("CAMERA_ID_TO_USE 尚未设置。请使用 --camera 参数指定相机。")

    print(f"--- 🚀 开始处理点云 ({LIDAR_ID_TO_USE}) 到图像投影 ---")

    try:
        points = read_lidar_points(pcd_file_path)
        
        # 2. 获取所有必要的变换矩阵和内参
        T_L_V = get_lidar_to_vehicle_transform(LIDAR_ID_TO_USE)
        T_V_C = get_camera_extrinsics_matrix(CAMERA_ID_TO_USE)
        K_matrix = get_camera_intrinsics_matrix(CAMERA_ID_TO_USE)
        dist_coeffs = get_camera_distortion_coefficients(CAMERA_ID_TO_USE)
    except Exception as e:
        print(f"❌ 初始化失败: {e}")
        return

    # 3. 激光雷达点云到自车坐标系
    points_homogeneous_lidar = np.hstack((points, np.ones((points.shape[0], 1))))
    points_vehicle = (T_L_V @ points_homogeneous_lidar.T).T[:, :3]

    # 4. 自车坐标系到相机坐标系
    points_homogeneous_vehicle = np.hstack((points_vehicle, np.ones((points_vehicle.shape[0], 1))))
    points_camera = (T_V_C @ points_homogeneous_vehicle.T).T[:, :3]

    # 5. 过滤掉相机视锥体外的点
    valid_indices = points_camera[:, 2] > 0.1 

    # 新增过滤条件：过滤掉深度大于 50 的点
    # depth_filter = (2 <= points[:, 0]) & (points[:, 0] <= 50) 
    depth_filter = (1 <= points[:, 0])

    # 将两个条件合并
    valid_indices = valid_indices & depth_filter


    points_camera_valid = points_camera[valid_indices]
    original_depths = points[valid_indices, 0] 

    if points_camera_valid.shape[0] == 0:
        print("⚠️ 警告: 没有点在相机前方，无法投影。")
        return

    # 6. 相机坐标系到 2D 图像平面 (带畸变投影)
    rvec = np.zeros((3, 1), dtype=np.float64)
    tvec = np.zeros((3, 1), dtype=np.float64)
    points_3d_input = points_camera_valid.astype(np.float64).reshape(-1, 1, 3)

    projected_points_undistorted = None
    a = 1

    if a==2:
        print("🔍 检测到鱼眼相机，使用鱼眼投影模型。")
        projected_points_undistorted, _ = cv2.projectPoints(
            objectPoints=points_3d_input,
            rvec=rvec,
            tvec=tvec,
            K=K_matrix,
            D=dist_coeffs,
        )
    else:
        print("🔍 使用标准针孔相机投影模型。")
        projected_points_undistorted, _ = cv2.projectPoints(
        objectPoints=points_3d_input,
        rvec=rvec,
        tvec=tvec,
        cameraMatrix=K_matrix,
        distCoeffs=dist_coeffs,
    )

    projected_points = projected_points_undistorted.reshape(-1, 2)
    
    # 7. 读取图像
    try:
        img = mpimg.imread(image_file_path)
        img_height, img_width, _ = img.shape
    except Exception as e:
        print(f"❌ 读取图像文件失败: {e}")
        return

    # 8. 过滤掉超出图像边界的点
    valid_proj_indices = np.where(
        (projected_points[:, 0] >= 0) & (projected_points[:, 0] < img_width) &
        (projected_points[:, 1] >= 0) & (projected_points[:, 1] < img_height)
    )
    
    final_projected_points = projected_points[valid_proj_indices]
    final_depths = original_depths[valid_proj_indices]

    if final_projected_points.shape[0] == 0:
        print("⚠️ 警告: 没有点落在图像区域内。")
        return

    # 9. 可视化或保存
    plt.figure(figsize=(16, 9))
    plt.imshow(img)
    
    scatter = plt.scatter(final_projected_points[:, 0], final_projected_points[:, 1],
                          c=final_depths, cmap=COLOR_MAP, s=POINT_SIZE, alpha=POINT_ALPHA)
    
    plt.colorbar(scatter, label='Lidar Depth (m)')
    plt.title(f"LiDAR {LIDAR_ID_TO_USE} to {CAMERA_ID_TO_USE} {os.path.basename(image_file_path)}_{os.path.basename(pcd_file_path)}")
    plt.axis('off')
    plt.tight_layout()
    
    if save_mode:
        print(f"📈 正在保存投影结果到: {output_dir}")
        # 获取原始文件名作为输出文件名的一部分
        base_name = os.path.splitext(os.path.basename(image_file_path))[0]
        output_filename = f"{base_name}_projected_{os.path.basename(pcd_file_path)}.jpg"
        
        # 确保输出目录存在
        os.makedirs(output_dir, exist_ok=True)
        output_file_path = os.path.join(output_dir, output_filename)
        
        plt.savefig(output_file_path, bbox_inches='tight', pad_inches=0.1)
        plt.close() # 必须关闭，否则会占用内存
        print(f"--- ✅ 投影结果已保存至: {output_file_path} ---")
    else:
        print("📈 生成可视化结果...")
        plt.show()
        print("--- ✅ 投影可视化完成！ ---")


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="将激光雷达点云投影到图像上并可视化或保存。")
    parser.add_argument("pcd_file", type=str, help="输入PCD或BIN文件的路径。")
    parser.add_argument("image_file", type=str, help="输入图像JPG文件的路径。")
    
    # 1. 添加 --lidar 参数
    parser.add_argument("--lidar", 
                        type=str, 
                        required=True, 
                        choices=list(LIDAR_MAP.keys()),
                        help="选择要使用的激光雷达位置。选项: " + ", ".join(LIDAR_MAP.keys()))
    
    # 2. 添加 --camera 参数
    parser.add_argument("--camera", 
                        type=str, 
                        required=True, 
                        choices=list(CAMERA_MAP.keys()),
                        help="选择要使用的相机位置。选项: " + ", ".join(CAMERA_MAP.keys()))
    
    # 【新增参数】
    parser.add_argument("--save", action="store_true", 
                        help="如果设置，则保存结果到文件而不是显示窗口。")
    parser.add_argument("--out_dir", type=str, default="projected_output",
                        help="保存模式下，指定输出目录。")
    
    args = parser.parse_args()
    
    # 检查文件是否存在
    if not os.path.exists(args.pcd_file):
        print(f"❌ 错误: 点云文件 '{args.pcd_file}' 不存在。")
        sys.exit(1)
    if not os.path.exists(args.image_file):
        print(f"❌ 错误: 图像文件 '{args.image_file}' 不存在。")
        sys.exit(1)

    project_lidar_to_image(args.pcd_file, args.image_file, args.lidar, args.camera, args.save, args.out_dir)