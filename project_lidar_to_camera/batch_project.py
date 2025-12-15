import argparse
import json
import os
import subprocess
import sys

# ==============================================================================
# 配置信息
# ==============================================================================

# 脚本名称
LIDAR_TO_IMAGE_SCRIPT = "./lidar_to_image.py"
# JSON 配置文件名
SAMPLE_JSON_FILE = "sample.json"

# 需要匹配的 Lidar 和 Camera 键名
LIDAR_KEY = "iv_points_front_left"
CAMERA_KEY = "camera_cam_8M_wa_front"

# 图像文件名中需要移除的尾缀 (来自 sample.json)
IMAGE_SUFFIX_TO_STRIP = "_scale_0.20_undistorted"

# ==============================================================================
# 批量处理逻辑
# ==============================================================================

def batch_project(pcd_dir_base: str, jpg_dir_base: str, output_dir: str):
    """
    加载 sample.json，批量执行点云到图像的投影。
    """
    
    # 1. 检查投影脚本是否存在
    if not os.path.exists(LIDAR_TO_IMAGE_SCRIPT):
        print(f"❌ 错误: 找不到投影脚本 '{LIDAR_TO_IMAGE_SCRIPT}'。请确保文件存在于当前目录。")
        sys.exit(1)

    # 2. 检查 JSON 文件是否存在并加载
    if not os.path.exists(SAMPLE_JSON_FILE):
        print(f"❌ 错误: 找不到配置文件 '{SAMPLE_JSON_FILE}'。")
        sys.exit(1)
        
    try:
        with open(SAMPLE_JSON_FILE, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ 错误: 解析 {SAMPLE_JSON_FILE} 失败: {e}")
        sys.exit(1)

    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)

    print(f"--- 🚀 开始批量投影 (共 {len(data)} 组数据) ---")
    print(f"Lidar Key: {LIDAR_KEY}, Camera Key: {CAMERA_KEY}")
    print(f"投影结果将保存至: {output_dir}")
    
    success_count = 0
    
    # 3. 循环遍历数据并执行投影
    for idx, item in enumerate(data):
        
        # 获取文件名
        lidar_filename = item.get(LIDAR_KEY)
        camera_filename = item.get(CAMERA_KEY)
        
        # 检查字段是否存在或是否为 'NOT_FOUND'
        if not lidar_filename or not camera_filename or camera_filename == "NOT_FOUND":
            print(f"⚠️ 警告: 数据 ID {item.get('id', 'N/A')} 缺少 '{LIDAR_KEY}' 或 '{CAMERA_KEY}' 字段，或图像标记为 'NOT_FOUND'，跳过。")
            continue

        # --- Lidar 文件路径处理：兼容 .pcd 和 .bin ---
        lidar_file_path_pcd = os.path.join(pcd_dir_base, lidar_filename)
        base_name, _ = os.path.splitext(lidar_filename)
        lidar_file_path_bin = os.path.join(pcd_dir_base, f"{base_name}.bin")
        
        if os.path.exists(lidar_file_path_pcd):
            lidar_file_path = lidar_file_path_pcd
        elif os.path.exists(lidar_file_path_bin):
            lidar_file_path = lidar_file_path_bin
        else:
            print(f"❌ 错误: 点云文件不存在: {lidar_file_path_pcd} 或 {lidar_file_path_bin}。跳过 ID {item.get('id', 'N/A')}。")
            continue
        
        # --- 图像文件路径处理：移除 JSON 中冗余的尾缀 ---
        actual_camera_filename = camera_filename
        
        if IMAGE_SUFFIX_TO_STRIP in camera_filename:
            base_name, ext = os.path.splitext(camera_filename)
            if base_name.endswith(IMAGE_SUFFIX_TO_STRIP):
                base_name_stripped = base_name[:-len(IMAGE_SUFFIX_TO_STRIP)]
                actual_camera_filename = base_name_stripped + ext
        
        camera_file_path = os.path.join(jpg_dir_base, actual_camera_filename)

        if not os.path.exists(camera_file_path):
            print(f"❌ 错误: 图像文件不存在: {camera_file_path} (从JSON文件名 '{camera_filename}' 修正而来)。跳过 ID {item.get('id', 'N/A')}。")
            continue

        print(f"\n--- ⚙️ [{idx+1}/{len(data)}] 处理 ID {item.get('id', 'N/A')} ---")
        
        # 4. 执行投影脚本 (默认使用保存模式)
        try:
            # 构建命令行参数
            command = [
                sys.executable,
                LIDAR_TO_IMAGE_SCRIPT,
                lidar_file_path,
                camera_file_path,
                # 【新增参数】：开启保存模式并指定输出目录
                "--save", 
                "--out_dir", output_dir
            ]
            
            # 执行命令，不阻塞，将输出打印到控制台
            result = subprocess.run(command, check=True) 
            
            success_count += 1
            
        except subprocess.CalledProcessError as e:
            print(f"❌ 投影脚本执行失败，ID {item.get('id', 'N/A')}。错误码: {e.returncode}")
        except FileNotFoundError:
            print(f"❌ 无法执行 {LIDAR_TO_IMAGE_SCRIPT}，请确保其权限和路径正确。")
            break

    print(f"\n--- ✅ 批量投影完成！成功处理 {success_count} 组数据。 ---")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="批量执行点云到图像的投影脚本。")
    parser.add_argument("pcd_dir", help="包含点云/BIN文件的根目录。")
    parser.add_argument("jpg_dir", help="包含图像文件的根目录。")
    # 【新增参数】
    parser.add_argument("--out", type=str, default="batch_projected_output",
                        help="指定投影结果文件的存储目录 (默认: batch_projected_output)。")
    
    args = parser.parse_args()
    
    pcd_dir = args.pcd_dir.rstrip(os.path.sep)
    jpg_dir = args.jpg_dir.rstrip(os.path.sep)
    out_dir = args.out.rstrip(os.path.sep)
    
    batch_project(pcd_dir, jpg_dir, out_dir)