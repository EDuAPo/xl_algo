#!/usr/bin/env python3

import os
import argparse
import subprocess
import sys
import glob
import cv2
from pathlib import Path
from typing import Dict, List

current_dir = Path(__file__).resolve().parent
workspace_dir = current_dir.parent
if str(workspace_dir) not in sys.path:
    sys.path.append(str(workspace_dir))

# 导入全局映射表
from config.global_mapping import LIDAR_MAP, CAMERA_MAP, LIDAR_CAMERA_MAP

# --- 脚本路径配置 ---
# 假设这些脚本都在相对于当前执行目录的正确位置
SCRIPT_EXPORT_CAMERA = "../export_camera.py" 
SCRIPT_EXPORT_LIDAR = "../export_lidar.py"
SCRIPT_PROJECT = "./project.py"

# --- 辅助函数 ---

def run_command(command, step_name):
    """
    执行命令行指令并检查其状态。
    使用 errors='replace' 修复 UnicodeDecodeError。
    """
    print(f"\n======== 🛠️ 步骤: {step_name} ========")
    print(f"执行命令: {' '.join(command)}")
    
    try:
        # 移除 text=True，让 stdout/stderr 保持为 bytes
        result = subprocess.run(
            command,
            check=True,  
            capture_output=True # output/error 现在是 bytes
        )
        
        # 使用更安全的解码方式处理输出
        stderr_str = result.stderr.decode('utf-8', errors='replace')
        
        if stderr_str:
            print(f"⚠️ {step_name} 脚本有输出到 stderr，但执行成功。")
            print("--- 脚本 stderr 输出 ---")
            print(stderr_str)
            print("---------------------------")
            
        print(f"✅ {step_name} 成功完成。")
        return True
        
    except subprocess.CalledProcessError as e:
        stderr_str = e.stderr.decode('utf-8', errors='replace')
        
        print(f"❌ {step_name} 执行失败，返回码: {e.returncode}")
        print("--- 错误详情 (stderr) ---")
        print(stderr_str)
        print("---------------------------")
        sys.exit(1)
        
    except FileNotFoundError:
        print(f"❌ 错误: 找不到脚本或命令 '{command[0]}'。请检查它是否在当前目录下。")
        sys.exit(1)

def create_video_from_images(image_dir, output_video_path, fps=10):
    """
    将目录下的 JPG 文件按时间顺序组合成 AVI 视频。
    """
    print(f"\n======== 🎬 步骤: 组合视频文件: {Path(output_video_path).name} ========")
    
    # 1. 查找并排序图像文件（假设文件是 JPG 格式）
    image_files = sorted(glob.glob(os.path.join(image_dir, '*.jpg')))
    
    if not image_files:
        print(f"⚠️ 警告: 在目录 '{image_dir}' 中未找到任何 JPG 图像文件，跳过视频生成。")
        return

    # 2. 获取第一张图的尺寸来初始化 VideoWriter
    first_frame = cv2.imread(image_files[0])
    if first_frame is None:
        print(f"❌ 错误: 无法读取第一张图像 '{image_files[0]}'，请检查 OpenCV 安装或文件损坏。")
        return
        
    height, width, _ = first_frame.shape
    
    # 3. 初始化 VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*'MJPG') # Motion-JPEG 编码，兼容性好
    video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))
    
    if not video_writer.isOpened():
        print(f"❌ 错误: 无法打开 VideoWriter 或指定编码 ('MJPG') 不受支持。")
        return

    # 4. 写入帧
    for i, image_file in enumerate(image_files):
        frame = cv2.imread(image_file)
        if frame is not None:
            video_writer.write(frame)
        
        if (i + 1) % 100 == 0:
            print(f"   已处理 {i + 1}/{len(image_files)} 帧...")

    # 5. 释放资源
    video_writer.release()
    print(f"✅ 视频生成成功！已保存到: {output_video_path}")


def main_workflow(bag_root_dir):
    """
    主工作流逻辑。
    """
    bag_root_path = Path(bag_root_dir).resolve()
    
    if not bag_root_path.is_dir():
        print(f"❌ 错误: 输入的 rosbag 根目录 '{bag_root_dir}' 不存在或不是一个目录。")
        sys.exit(1)
        
    print(f"🚀 开始 Lidar-Camera 投影自动化工作流，根目录: {bag_root_path}")
    
    # ----------------------------------------------------
    # 1. 定义和创建基础输出目录
    # ----------------------------------------------------
    # 这里的目录是导出脚本的 --out 参数
    BASE_IMAGE_DIR = bag_root_path / "camera_images"
    BASE_LIDAR_DIR = bag_root_path / "lidar_pcds"
    
    # 所有投影结果的根目录
    PROJECT_RESULTS_ROOT = bag_root_path / "projection_results"
    
    os.makedirs(BASE_IMAGE_DIR, exist_ok=True)
    os.makedirs(BASE_LIDAR_DIR, exist_ok=True)
    os.makedirs(PROJECT_RESULTS_ROOT, exist_ok=True)
    
    print(f"✅ 输出目录已准备就绪。")
    
    # ----------------------------------------------------
    # 2. 步骤一：从 ROS Bag 导出数据 (export_camera.py & export_lidar.py)
    # ----------------------------------------------------
    
    # 导出所有相机图像
    cmd_export_cam = [
        sys.executable,
        SCRIPT_EXPORT_CAMERA,
        "--bag", str(bag_root_path),
        "--out", str(BASE_IMAGE_DIR)
    ]
    # 假设 export_camera.py 会在 BASE_IMAGE_DIR 下创建如 'camera_cam_8M_wa_front' 这样的子目录
    run_command(cmd_export_cam, "1/3 导出所有相机图像 (export_camera.py)")

    # 导出所有 Lidar 点云
    cmd_export_lidar = [
        sys.executable,
        SCRIPT_EXPORT_LIDAR,
        "--bag", str(bag_root_path),
        "--out", str(BASE_LIDAR_DIR),
        "--format", "pcd_binary" 
    ]
    # 假设 export_lidar.py 会在 BASE_LIDAR_DIR 下创建如 'iv_points_front_left' 这样的子目录
    run_command(cmd_export_lidar, "2/3 导出所有 Lidar 点云 (export_lidar.py)")

    # ----------------------------------------------------
    # 3. 步骤三：批量点云到图像投影 (project.py) 和视频生成
    # ----------------------------------------------------
    
    print("\n======== 🔄 批量投影和视频生成开始... ========")
    total_pairs = sum(len(cameras) for cameras in LIDAR_CAMERA_MAP.values())
    pair_count = 0
    
    # 迭代 Lidar-Camera 映射表中的所有有效组合
    for lidar_short_sn, camera_short_sns in LIDAR_CAMERA_MAP.items():
        
        # 获取 Lidar 的长名称 (Config ID)，用于构建输入路径
        lidar_long_id = LIDAR_MAP.get(lidar_short_sn)
        if not lidar_long_id:
            print(f"⚠️ 警告: Lidar 短名称 '{lidar_short_sn}' 无法映射到长名称，跳过。")
            continue
            
        # Lidar 输入目录 (使用长名称)
        pcd_input_dir = BASE_LIDAR_DIR / lidar_long_id / "pcd_binary"

        for camera_short_sn in camera_short_sns:
            pair_count += 1
            
            # 获取 Camera 的长名称 (Config ID)，用于构建输入路径
            camera_long_id = CAMERA_MAP.get(camera_short_sn)
            if not camera_long_id:
                print(f"⚠️ 警告: Camera 短名称 '{camera_short_sn}' 无法映射到长名称，跳过。")
                continue
                
            # Camera 输入目录 (使用长名称)
            jpg_input_dir = BASE_IMAGE_DIR / camera_long_id
            
            # 投影结果的专属输出目录（使用短名称组合）
            pair_name = f"{lidar_short_sn}_{camera_short_sn}"
            pair_output_dir = PROJECT_RESULTS_ROOT / pair_name
            os.makedirs(pair_output_dir, exist_ok=True)

            print(f"\n--- 🚀 开始处理组合 ({pair_count}/{total_pairs}): {lidar_short_sn} -> {camera_short_sn} ---")

            # 检查输入目录是否存在，防止 project.py 失败
            if not pcd_input_dir.is_dir():
                 print(f"⚠️ 警告: Lidar 目录缺失 ({pcd_input_dir})，跳过此组合。")
                 continue
            if not jpg_input_dir.is_dir():
                 print(f"⚠️ 警告: Camera 目录缺失 ({jpg_input_dir})，跳过此组合。")
                 continue

            # 运行 project.py
            # project.py 接收 short name 作为 --lidar/--camera 参数
            cmd_project = [
                sys.executable,
                SCRIPT_PROJECT,
                # --pcd 和 --jpg 路径使用长名称的子目录
                "--pcd", str(pcd_input_dir),
                "--jpg", str(jpg_input_dir),
                "--out", str(pair_output_dir),
                # --lidar 和 --camera 参数使用短名称
                "--lidar", lidar_short_sn,
                "--camera", camera_short_sn,
                # "--save" # 确保 project.py 是保存文件
            ]
            run_command(cmd_project, f"3/3.{pair_count} 投影: {lidar_short_sn} -> {camera_short_sn}")
            
            # 组合视频文件
            # output_video_path = str(pair_output_dir / f"{pair_name}_projection_result.avi")
            # create_video_from_images(str(pair_output_dir), output_video_path, fps=10)
    
    print("\n🎉 **Lidar-Camera 投影工作流全部完成！**")
    print(f"所有投影结果和视频已保存到根目录: {PROJECT_RESULTS_ROOT}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="自动化 Lidar-Camera 投影工作流：导出数据 -> 批量投影 -> 生成视频。",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument("--bag", type=str, required=True, 
                        help="ROS Bag 文件的根目录。")

    args = parser.parse_args()
    
    main_workflow(args.bag)