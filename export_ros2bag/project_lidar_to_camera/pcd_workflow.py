import os
import argparse
import subprocess
import sys
from pathlib import Path

import os
import argparse
import subprocess
import sys
from pathlib import Path
# ... (其他导入保持不变)

def run_command(command, step_name):
    """
    执行命令行指令并检查其状态。
    
    【修复】：移除 text=True，并使用 errors='replace' 手动解码 stdout/stderr。
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
        
        # 使用更安全的解码方式处理输出，忽略或替换无法识别的字节
        # 重点：使用 errors='replace' 来避免 UnicodeDecodeError
        stdout_str = result.stdout.decode('utf-8', errors='replace')
        stderr_str = result.stderr.decode('utf-8', errors='replace')
        
        if stderr_str:
            print(f"⚠️ {step_name} 脚本有输出到 stderr，但执行成功。")
            print("--- 脚本 stderr 输出 ---")
            print(stderr_str)
            print("---------------------------")
            
        print(f"✅ {step_name} 成功完成。")
        # 调试时可以取消注释以下两行，查看 stdout 
        # print("--- 脚本 stdout 输出 ---")
        # print(stdout_str)
        # print("---------------------------")
        return True
        
    except subprocess.CalledProcessError as e:
        # 解码错误信息
        stderr_str = e.stderr.decode('utf-8', errors='replace')
        
        print(f"❌ {step_name} 执行失败，返回码: {e.returncode}")
        print("--- 错误详情 (stderr) ---")
        print(stderr_str)
        print("---------------------------")
        sys.exit(1)
        
    except FileNotFoundError:
        print(f"❌ 错误: 找不到脚本或命令 '{command[0]}'。请检查它是否在当前目录下。")
        sys.exit(1)


def process_pcd_workflow(bag_root_dir):
    """
    自动化点云处理工作流：导出 -> 转换到自车系 -> 合并。
    """
    # 确保 bag_root_dir 绝对路径和存在
    bag_root_path = Path(bag_root_dir).resolve()
    if not bag_root_path.is_dir():
        print(f"❌ 错误: 输入的 rosbag 根目录 '{bag_root_dir}' 不存在或不是一个目录。")
        sys.exit(1)
        
    print(f"🚀 开始点云自动化处理工作流，根目录: {bag_root_path}")
    
    # ----------------------------------------------------
    # 1. 定义和创建输出目录
    # ----------------------------------------------------
    
    # 步骤 1: 原始 PCD 输出目录
    pcd_output_dir = bag_root_path / "pcd"
    os.makedirs(pcd_output_dir, exist_ok=True)
    
    # 步骤 2: 自车坐标系 PCD 输出目录
    pcd_vehicle_dir = bag_root_path / "pcd_vehicle"
    os.makedirs(pcd_vehicle_dir, exist_ok=True)
    
    # 步骤 3: 合并后的 PCD 输出目录
    pcd_merged_dir = bag_root_path / "pcd_merged"
    os.makedirs(pcd_merged_dir, exist_ok=True)
    
    print(f"✅ 输出目录已准备就绪。")
    
    # ----------------------------------------------------
    # 2. 步骤一：从 ROS Bag 导出点云 (export_lidar.py)
    # ----------------------------------------------------
    
    # python3 ./export_lidar.py --bag <bag_root_path> --out <pcd_output_dir> --format pcd_binary
    cmd_export = [
        sys.executable,  # 确保使用正确的 Python 解释器
        "../export_lidar.py",
        "--bag", str(bag_root_path),
        "--out", str(pcd_output_dir),
        "--format", "pcd_binary"
    ]
    run_command(cmd_export, "1/3 导出点云 (export_lidar.py)")

    # ----------------------------------------------------
    # 3. 步骤二：转换为自车坐标系 (pcd_to_vehicle.py)
    # ----------------------------------------------------
    
    # 注意: 您的命令行中有一个 'cd project_lidar_to_camera'，
    # 但为了简化自动化脚本，我们假设 pcd_to_vehicle.py 在当前执行目录下，
    # 如果它在一个子目录中，您需要将路径调整为 './project_lidar_to_camera/pcd_to_vehicle.py'
    
    # python3 ./pcd_to_vehicle.py --pcd <pcd_output_dir> --out <pcd_vehicle_dir>
    cmd_to_vehicle = [
        sys.executable,
        "./pcd_to_vehicle.py",
        "--pcd", str(pcd_output_dir),
        "--out", str(pcd_vehicle_dir)
    ]
    run_command(cmd_to_vehicle, "2/3 转换到自车坐标系 (pcd_to_vehicle.py)")


    # ----------------------------------------------------
    # 4. 步骤三：合并点云 (pcd_merge.py)
    # ----------------------------------------------------
    
    # python3 ./pcd_merge.py --pcd <pcd_vehicle_dir> --out <pcd_merged_dir> --all
    cmd_merge = [
        sys.executable,
        "./pcd_merge.py",
        "--pcd", str(pcd_vehicle_dir),
        "--out", str(pcd_merged_dir),
        "--all"
    ]
    run_command(cmd_merge, "3/3 合并点云 (pcd_merge.py)")
    
    print("\n🎉 **点云处理工作流全部完成！**")
    print(f" - 原始 PCD 文件位于: {pcd_output_dir}")
    print(f" - 自车系 PCD 文件位于: {pcd_vehicle_dir}")
    print(f" - 合并后的文件位于: {pcd_merged_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="自动化点云处理工作流：ROS Bag 导出 -> 坐标系转换 -> 点云合并。",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    # 匹配用户要求的输入参数 --bag
    parser.add_argument("--bag", type=str, required=True, 
                        help="ROS Bag 文件的根目录，例如：/home/shucdong/Downloads/bag_data/")

    args = parser.parse_args()
    
    process_pcd_workflow(args.bag)