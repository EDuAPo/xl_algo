import argparse
import subprocess
import os
import sys
import shutil
from typing import List

# --- 配置常量 (基于您提供的目录结构进行修正) ---
# 假设主脚本位于 ~/workspace/xl/bag_parser/export_ros2bag/
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

EXPORT_CAMERA_SCRIPT = os.path.join(CURRENT_DIR, "export_camera.py")
EXPORT_LIDAR_SCRIPT = os.path.join(CURRENT_DIR, "export_lidar.py")
EXPORT_IMU_SCRIPT = os.path.join(CURRENT_DIR, "export_imu", "export_imu.py")
UNDISTORTION_SCRIPT = os.path.join(CURRENT_DIR, "undistortion", "undistortion.py")
EXTRACT_SAMPLE_SCRIPT = os.path.join(CURRENT_DIR, "extract_sample_undistorted.py")

# ROS 2 自定义消息的安装路径 (用于 source)
IMU_MSGS_INSTALL_PATH = os.path.join(CURRENT_DIR, "export_imu", "imu_msgs", "install")

# 第4步 (undistortion) 所需的特定参数
UNDISTORTION_PARAMS_DIR = os.path.join(CURRENT_DIR, "undistortion", "intrinsic_param")
VEHICLE_MODEL = "vehicle_000"
SCALE_MIN = "0.2"
LOGTIME = "20251219" 

def get_shell_setup_command() -> str:
    """
    检测当前运行的 shell 类型 (bash/zsh) 并返回 ROS 2 setup 命令。
    """
    current_shell = os.environ.get('SHELL', 'bash').split('/')[-1]
    
    if 'zsh' in current_shell:
        setup_file = "setup.zsh"
        # print(f"检测到当前 Shell 为 ZSH，将使用 {setup_file}。")
    elif 'bash' in current_shell:
        setup_file = "setup.bash"
        # print(f"检测到当前 Shell 为 BASH，将使用 {setup_file}。")
    else:
        setup_file = "setup.bash"
        # print(f"检测到未知 Shell ({current_shell})，默认使用 setup.bash。")
        
    return f"source {os.path.join(IMU_MSGS_INSTALL_PATH, setup_file)}"


def run_command(command: List[str], step_name: str, use_shell: bool = False):
    """
    执行一个外部命令，并在失败时退出。
    """
    print(f"\n--- 🚀 开始执行步骤: {step_name} ---")
    
    if use_shell:
        full_command = command[0]
        print(f"命令: {full_command}")
    else:
        # Note: 此时我们只在 shell=True 时使用此函数，因此此分支可能很少被执行。
        full_command = command
        print(f"命令: {' '.join(full_command)}")

    try:
        # 在 shell=True 模式下，我们必须指定 executable 为当前 shell，以确保 source 命令生效
        subprocess.run(full_command, check=True, text=True, shell=use_shell, executable=os.environ.get('SHELL', '/bin/bash'))
        print(f"--- ✅ 步骤 {step_name} 执行成功。 ---")
    except subprocess.CalledProcessError as e:
        print(f"--- ❌ 步骤 {step_name} 执行失败！ ---", file=sys.stderr)
        print(f"错误码: {e.returncode}", file=sys.stderr)
        print(f"Stdout:\n{e.stdout}", file=sys.stderr)
        print(f"Stderr:\n{e.stderr}", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print(f"--- ❌ 步骤 {step_name} 执行失败！ ---", file=sys.stderr)
        print(f"错误: 找不到脚本或命令。请检查路径。", file=sys.stderr)
        sys.exit(1)


def adjust_directories(export_dir: str, undistorted_dir: str):
    """
    步骤 5: 调整目录结构，将 iv_points* 和 ins.json 移动到最终的 undistorted 目录。
    """
    print("\n--- 🚀 开始执行步骤: [Export Step 5/6] 调整目录结构 (移动文件) ---")
    
    files_to_move = []
    try:
        # 查找 iv_points* 和 ins.json
        for item in os.listdir(export_dir):
            if item.startswith("iv_points") or item == "ins.json":
                files_to_move.append(item)
                
        if not files_to_move:
            print("警告: 未找到 iv_points* 或 ins.json 文件进行移动。")
            
        for filename in files_to_move:
            src = os.path.join(export_dir, filename)
            dst = os.path.join(undistorted_dir, filename)
            shutil.move(src, dst)
            print(f"  移动: {filename}")
            
        print("--- ✅ 步骤 [Export Step 5/6] 目录调整执行成功。 ---")

    except Exception as e:
        print(f"--- ❌ 步骤 [Export Step 5/6] 目录调整执行失败！ ---", file=sys.stderr)
        print(f"错误: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="ROS 2 Bag 数据导出与预处理流程调度脚本。"
    )
    parser.add_argument(
        "--bag",
        type=str,
        required=True,
        help="输入 ROS 2 Bag 目录的路径 (如: /home/user/data/bags/)"
    )
    parser.add_argument(
        "--out",
        type=str,
        required=True,
        help="主输出目录的路径 (所有中间和最终文件都将放在其子目录中)"
    )
    # 【新增必需参数】
    parser.add_argument("--vehicle", 
                        type=str, 
                        required=True, 
                        help="指定车辆型号/配置，用于去畸变参数查找 (例如: vehicle_000)。")

    # 【新增必需参数】
    parser.add_argument("--logtime", 
                        type=str, 
                        required=True, 
                        help="指定日志时间戳，作为输出目录名的一部分 (例如: 20251104_160012)。")
    
    args = parser.parse_args()

    # --- 目录变量定义 ---
    INPUT_BAG_DIR = args.bag
    MAIN_OUTPUT_DIR = args.out
    
    # EXPORT_DIR = os.path.join(MAIN_OUTPUT_DIR, "exported_raw_data")
    EXPORT_DIR = os.path.join(MAIN_OUTPUT_DIR)
    UNDISTORTED_DIR = os.path.join(EXPORT_DIR, "undistorted")
    IMU_JSON_PATH = os.path.join(EXPORT_DIR, "ins.json")
    
    # 确保输出目录存在
    os.makedirs(EXPORT_DIR, exist_ok=True)
    os.makedirs(UNDISTORTED_DIR, exist_ok=True)

    print(f"🎬 流程开始。输入 Bag 目录: {INPUT_BAG_DIR}, 主输出目录: {MAIN_OUTPUT_DIR}")
    
    # 获取 shell setup 命令
    SHELL_SETUP_COMMAND = get_shell_setup_command()
    print(f"检测到 Shell 环境，IMU Setup 命令: {SHELL_SETUP_COMMAND.split(' ')[1]}") # 打印 setup 文件名


    # =================================================================
    # 流程主线开始
    # =================================================================
    
    # --- 1. 导出 Camera 图像 ---
    camera_command_string = (
        f"{sys.executable} {EXPORT_CAMERA_SCRIPT} "
        f"--bag {INPUT_BAG_DIR} "
        f"--out {EXPORT_DIR}"
    )
    run_command([camera_command_string], "[Export Step 1/6] 导出 Camera 图像", use_shell=True)

    # --- 2. 导出 Lidar 点云 ---
    lidar_command_string = (
        f"{sys.executable} {EXPORT_LIDAR_SCRIPT} "
        f"--bag {INPUT_BAG_DIR} "
        f"--out {EXPORT_DIR} "
        f"--format pcd_binary"
    )
    run_command([lidar_command_string], "[Export Step 2/6] 导出 Lidar 点云", use_shell=True)
    
    # --- 3. 导出 IMU/INS 数据 (需要 source) ---
    imu_command_string = (
        f"{SHELL_SETUP_COMMAND} && "
        f"{sys.executable} {EXPORT_IMU_SCRIPT} "
        f"--bag {INPUT_BAG_DIR} "
        f"--out {IMU_JSON_PATH}"
    )
    run_command([imu_command_string], "[Export Step 3/6] 导出 IMU/INS 数据 (需 Shell Setup)", use_shell=True)
    
    # --- 4. 图像去畸变 ---
    VEHICLE_MODEL = args.vehicle
    LOGTIME = args.logtime
    undistort_command_string = (
        f"{sys.executable} {UNDISTORTION_SCRIPT} "
        f"--images {EXPORT_DIR} "
        f"--params {UNDISTORTION_PARAMS_DIR} "
        f"--vehicle {VEHICLE_MODEL} "
        f"--out {UNDISTORTED_DIR} "
        f"--scale_min {SCALE_MIN} "
        f"--logtime {LOGTIME}"
    )
    run_command([undistort_command_string], "[Export Step 4/6] 图像去畸变", use_shell=True)
    
    # --- 5. 调整目录结构 (调用单独的函数) ---
    adjust_directories(EXPORT_DIR, UNDISTORTED_DIR)
    
    # --- 6. 提取样本 ---
    extract_command_string = (
        f"{sys.executable} {EXTRACT_SAMPLE_SCRIPT} "
        f"{UNDISTORTED_DIR}"
    )
    run_command([extract_command_string], "[Export Step 6/6] 提取样本", use_shell=True)

    print("\n\n🎉🎉🎉 预处理导出阶段完成 (6个内部步骤已执行) 🎉🎉🎉")
    print(f"最终数据位于: {UNDISTORTED_DIR}")


if __name__ == "__main__":
    # 建议将此脚本保存为 run_export.py 或 run_export_optimized.py
    main()