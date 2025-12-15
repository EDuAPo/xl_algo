#!/usr/bin/env python3

import os
import argparse
import subprocess
from collections import defaultdict
import re
import cv2
import numpy as np
import sys
from concurrent.futures import ThreadPoolExecutor
import glob

# --- 配置 ---
# 假设 lidar_to_image.py 脚本位于当前目录或 PATH 中
LIDAR_TO_IMAGE_SCRIPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lidar_to_image.py')
# 如果你的 Python 解释器是 python3，请确保 subprocess 中也是
PYTHON_EXECUTABLE = 'python3' 

# 正则表达式用于匹配文件名中的时间戳，例如: 20251104_152100_912.pcd
# 匹配 '年-月-日_时-分-秒_毫秒'
# 我们只需要最后的三位毫秒数作为核心同步依据
TIMESTAMP_PATTERN = re.compile(r'_(\d{3})\.(pcd|jpg|jpeg|png)$', re.IGNORECASE)

# --- 辅助函数 ---

def extract_timestamp_ms(filename: str) -> int:
    """
    从文件名中提取毫秒时间戳 (最后三位数字)。
    例如: '20251104_152100_912.pcd' -> 912
    """
    match = TIMESTAMP_PATTERN.search(filename)
    if match:
        # 提取最后的三位数字（毫秒部分）
        ms_str = match.group(1)
        # 假设文件名中靠前的部分 (如 20251104_152100) 已经保证了大致的时间同步，
        # 我们的目标是微调到最接近的帧。
        # 这里只返回最后三位毫秒。
        return int(ms_str)
    
    # 如果格式不匹配，返回一个极小的数，确保它不会被错误匹配
    return -1


def find_closest_pair(lidar_files: list, camera_files: list) -> list:
    """
    找到时间戳最接近的 (lidar_file, camera_file) 文件对。
    
    :param lidar_files: PCD/BIN 文件路径列表
    :param camera_files: JPG/PNG 文件路径列表
    :return: 包含 (lidar_path, camera_path) 对的列表
    """
    print("⏳ 正在计算最接近的时间戳文件对...")
    
    # 1. 提取所有文件的时间戳（以毫秒为单位）
    lidar_stamps = []
    for f in lidar_files:
        ms = extract_timestamp_ms(os.path.basename(f))
        # 假设文件名格式是 'YYYYMMDD_HHMMSS_XXX.pcd'，我们关注的是最后的 XXX
        # 为了保证时间戳的唯一性，我们将时间信息组合成一个大的整数
        # 这里的 XXX 是毫秒，而前面的 YYMMDD_HHMMSS 代表的是秒级时间
        
        # 改进：直接使用 os.path.getctime 或 os.path.getmtime 获取系统时间戳
        # 但由于您的需求是基于文件名中的时间，我们继续使用文件名解析
        
        # 为了精确同步，我们应该使用文件名中完整的微秒级时间。
        # 简化处理：由于文件来自同一个log，我们只同步最后三位毫秒。
        # 这是一个简化且高效的方法。
        full_name = os.path.basename(f).split('.')[0]
        # 使用完整的数字串作为时间 ID
        time_id = int(re.sub(r'[^0-9]', '', full_name))
        lidar_stamps.append({'id': time_id, 'path': f})

    camera_stamps = []
    for f in camera_files:
        full_name = os.path.basename(f).split('.')[0]
        time_id = int(re.sub(r'[^0-9]', '', full_name))
        camera_stamps.append({'id': time_id, 'path': f})
        
    if not lidar_stamps or not camera_stamps:
        print("⚠️ 警告: 缺少点云或图像文件，无法配对。")
        return []

    # 2. 排序 (按时间 ID)
    lidar_stamps.sort(key=lambda x: x['id'])
    camera_stamps.sort(key=lambda x: x['id'])

    # 3. 寻找最接近的配对 (使用双指针或最近邻搜索)
    paired_files = []
    lidar_idx = 0
    camera_idx = 0

    while lidar_idx < len(lidar_stamps) and camera_idx < len(camera_stamps):
        lidar_time = lidar_stamps[lidar_idx]['id']
        camera_time = camera_stamps[camera_idx]['id']
        
        # 计算时间差
        time_diff = lidar_time - camera_time
        
        if abs(time_diff) < 30: # 假设 20ms 的时间差是可接受的阈值，根据您的数据可能需要调整
            # 找到最接近的配对，将其添加到结果列表
            paired_files.append((
                lidar_stamps[lidar_idx]['path'], 
                camera_stamps[camera_idx]['path']
            ))
            
            # 找到配对后，两个指针都向前移动（避免重复使用）
            lidar_idx += 1
            camera_idx += 1
        elif time_diff > 0:
            # Lidar 时间 > Camera 时间，移动 Camera 指针以追上 Lidar 时间
            camera_idx += 1
        else: # time_diff < 0
            # Lidar 时间 < Camera 时间，移动 Lidar 指针以追上 Camera 时间
            lidar_idx += 1
    
    print(f"✅ 成功配对 {len(paired_files)} 组文件。")
    return paired_files

def run_projection(pcd_path: str, img_path: str, lidar_name: str, camera_name: str, output_dir: str):
    """
    执行 lidar_to_image.py 脚本的子进程。
    """
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)
    
    # 构造命令
    # 注意：我们传递 --save 和 --out_dir 参数给 lidar_to_image.py
    command = [
        PYTHON_EXECUTABLE,
        LIDAR_TO_IMAGE_SCRIPT,
        pcd_path,
        img_path,
        '--lidar', lidar_name,
        '--camera', camera_name,
        '--save',  # 启用保存模式
        '--out_dir', output_dir
    ]
    
    # 格式化输出信息
    pcd_base = os.path.basename(pcd_path)
    img_base = os.path.basename(img_path)
    
    try:
        print(f"--- ⚙️ 正在处理: {pcd_base} -> {img_base} ---")
        
        # 执行子进程
        result = subprocess.run(
            command,
            check=True,  # 确保子进程成功运行
            capture_output=True, # 捕获输出
            text=True
        )
        
        print(f"--- ✅ 成功处理: {pcd_base} ---")
        # 打印子进程的输出，帮助调试
        # print("Stdout:\n" + result.stdout) 
        
    except subprocess.CalledProcessError as e:
        print(f"--- ❌ 投影失败: {pcd_base} (Exit Code: {e.returncode}) ---")
        print(f"Stderr:\n{e.stderr}")
    except FileNotFoundError:
        print(f"--- ❌ 错误: 找不到Python解释器 ({PYTHON_EXECUTABLE}) 或脚本 ({LIDAR_TO_IMAGE_SCRIPT}) ---")
        sys.exit(1)

def create_video_from_images(image_dir, output_video_path, fps=10):
    """
    将目录下的 JPG 文件按时间顺序组合成 AVI 视频。
    """
    print(f"\n======== 🎬 步骤: 组合视频文件 ========")
    
    # 1. 查找并排序图像文件
    image_files = sorted(glob.glob(os.path.join(image_dir, '*.jpg')))
    
    if not image_files:
        print(f"⚠️ 警告: 在目录 '{image_dir}' 中未找到任何 JPG 图像文件，跳过视频生成。")
        return

    # 2. 获取第一张图的尺寸来初始化 VideoWriter
    first_frame = cv2.imread(image_files[0])
    if first_frame is None:
        print(f"❌ 错误: 无法读取第一张图像 '{image_files[0]}'，无法创建视频。")
        return
        
    height, width, _ = first_frame.shape
    
    # 3. 初始化 VideoWriter
    # 使用 Motion-JPEG 编码 (.avi 容器)
    fourcc = cv2.VideoWriter_fourcc(*'MJPG') 
    video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))
    
    if not video_writer.isOpened():
        print(f"❌ 错误: 无法打开 VideoWriter 或指定编码 ('MJPG') 不受支持。")
        # 尝试使用 XVID 作为备选
        print("尝试使用 XVID 编码...")
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        video_writer = cv2.VideoWriter(output_video_path.replace(".avi", "_xvid.avi"), fourcc, fps, (width, height))
        if not video_writer.isOpened():
            print("❌ 错误: XVID 编码也失败，无法生成视频。")
            return

    # 4. 写入帧
    for i, image_file in enumerate(image_files):
        frame = cv2.imread(image_file)
        if frame is not None:
            video_writer.write(frame)
        else:
            print(f"⚠️ 警告: 无法读取文件 {os.path.basename(image_file)}，跳过该帧。")
        
        if (i + 1) % 100 == 0:
            print(f"   已处理 {i + 1}/{len(image_files)} 帧...")

    # 5. 释放资源
    video_writer.release()
    print(f"✅ 视频生成成功！已保存到: {output_video_path}")


# --- 主逻辑 ---

def main():
    parser = argparse.ArgumentParser(
        description="批量将最接近的激光雷达点云投影到相机图片上，并保存结果。",
        epilog="确保 lidar_to_image.py 脚本位于同一目录或 PATH 中。"
    )
    
    # 1. 必需的输入参数
    parser.add_argument("--pcd", type=str, required=True, help="包含PCD/BIN文件的根目录。")
    parser.add_argument("--jpg", type=str, default=None, help="包含JPG/PNG文件的根目录。")
    
    # 2. 传递给 lidar_to_image.py 的参数
    parser.add_argument("--lidar", type=str, required=True, help="传递给 lidar_to_image.py 的 --lidar 参数 (如: front_left)。")
    parser.add_argument("--camera", type=str, required=True, help="传递给 lidar_to_image.py 的 --camera 参数 (如: 3m_left)。")
    
    # 3. 输出参数
    parser.add_argument("--out", type=str, default="batch_project_output", help="保存投影结果的输出目录。")
    
    # 4. 线程/进程参数
    parser.add_argument("--workers", type=int, default=os.cpu_count(), help="并行处理任务的线程数（默认CPU核心数）。")

    args = parser.parse_args()

    if args.jpg is None:
        args.jpg = args.pcd  # 如果未指定，则使用相同目录
    
    # 检查 lidar_to_image.py 脚本是否存在
    if not os.path.exists(LIDAR_TO_IMAGE_SCRIPT):
        print(f"❌ 错误: 找不到 lidar_to_image.py 脚本文件于: {LIDAR_TO_IMAGE_SCRIPT}")
        print("请将此批量脚本放在 lidar_to_image.py 的同级目录下，或修改脚本中的 LIDAR_TO_IMAGE_SCRIPT 路径。")
        sys.exit(1)

    print("="*60)
    print("🚀 激光雷达点云批量投影启动...")
    print(f"Lidar目录: {args.pcd}")
    print(f"Camera目录: {args.jpg}")
    print(f"输出目录: {args.out}")
    print(f"Lidar ID: {args.lidar}, Camera ID: {args.camera}")
    print(f"并行线程数: {args.workers}")
    print("="*60)

    # 1. 递归查找文件
    lidar_files = []
    for root, _, files in os.walk(args.pcd):
        for f in files:
            if f.lower().endswith(('.pcd', '.bin')): # 支持 pcd 和 bin
                lidar_files.append(os.path.join(root, f))

    camera_files = []
    for root, _, files in os.walk(args.jpg):
        for f in files:
            if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')): # 支持多种图像格式
                camera_files.append(os.path.join(root, f))
    
    if not lidar_files:
        print(f"❌ 错误: 在目录 '{args.pcd}' 中未找到 PCD/BIN 文件。")
        sys.exit(1)
    if not camera_files:
        print(f"❌ 错误: 在目录 '{args.jpg}' 中未找到 JPG/PNG 文件。")
        sys.exit(1)

    print(f"找到 {len(lidar_files)} 个点云文件和 {len(camera_files)} 个图像文件。")

    # 2. 配对文件
    paired_files = find_closest_pair(lidar_files, camera_files)
    
    if not paired_files:
        print("⚠️ 警告: 未找到任何有效的点云-图像配对。请检查文件命名格式和时间同步。")
        sys.exit(0)

    # 3. 批量执行投影（使用线程池加速 I/O 密集型操作，或进程池如果 CPU 密集）
    # 由于投影是 CPU 密集型的 (OpenCV/Numpy)，我们使用 ProcessPoolExecutor 或 ThreadPoolExecutor。
    # 为了简化，我们先使用 ThreadPoolExecutor，如果遇到 CPU 瓶颈，再换成 ProcessPoolExecutor。
    
    # 使用 ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = [
            executor.submit(
                run_projection, pcd_path, img_path, 
                args.lidar, args.camera, args.out
            )
            for pcd_path, img_path in paired_files
        ]
        
        # 可选：等待所有任务完成
        for i, future in enumerate(futures):
            future.result() # 这会阻塞直到任务完成或抛出异常
            # print(f"[{i+1}/{len(paired_files)}] 任务完成。")


    print("\n" + "="*60)
    print(f"🎉 批量投影处理完成! 结果保存在: {args.out}")
    print("="*60)

    # ----------------------------------------------------
    # 5. 步骤四：组合视频文件 (新功能)
    # ----------------------------------------------------
    output_video_path = os.path.join(args.out, "projection_result.avi")
    create_video_from_images(args.out, output_video_path, fps=10)


if __name__ == '__main__':
    # 为了避免在 Windows/某些环境下出现问题，建议加上这句
    # multiprocessing.freeze_support() 
    main()