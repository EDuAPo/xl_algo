
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


def main():

    parser = argparse.ArgumentParser(
        description="批量将最接近的激光雷达点云投影到相机图片上，并保存结果。",
        epilog="确保 lidar_to_image.py 脚本位于同一目录或 PATH 中。"
    )
    
    # 1. 必需的输入参数
    parser.add_argument("--jpg", type=str, default=None, help="包含JPG/PNG文件的根目录。")

    args = parser.parse_args()

    if args.jpg is None:
        args.jpg = args.pcd  # 如果未指定，则使用相同目录

    # 获取输入jpg目录的父目录的父目录，生成输出视频路径
    parent_dir = os.path.dirname(os.path.dirname(args.jpg))

    video_path = os.path.join(parent_dir, "output_video.avi")

    create_video_from_images(args.jpg, output_video_path=video_path, fps=10)
    print(video_path)

if __name__ == "__main__":
    main()