import os
import sys
import subprocess
import yaml
import re
from datetime import datetime
from typing import List, Tuple

# ===================== 配置区域（只需要填两个脚本路径！）=====================
# 1. 两个子脚本的实际路径
FILTER_SCRIPT_PATH = "/home/zgw/Desktop/export_ros2bag/filter_by_time.py"  # 第一个代码路径
RUN_EXPORT_SCRIPT_PATH = "/home/zgw/Desktop/export_ros2bag/run_export.py"  # 第二个代码路径

# 2. 预处理脚本的默认配置（可选改）
DEFAULT_VEHICLE = "vehicle_000"
DEFAULT_MAIN_OUT = "/media/zgw/T7/1124/cmy/bag/full_output/"  # 预处理的主输出目录

#时间段yaml文件
TIME_PERIODS_YAML = "./time_periods.yaml" 

# =======================================================================

def load_time_periods(yaml_path: str) -> List[Tuple[str, str]]:
    """从YAML文件加载时间段列表，格式要求：[[HHMMSS, HHMMSS], ...]"""
    if not os.path.exists(yaml_path):
        raise FileNotFoundError(f"未找到时间段配置文件：{yaml_path}")
    
    with open(yaml_path, 'r', encoding='utf-8') as f:
        try:
            data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            raise ValueError(f"YAML文件格式错误：{str(e)}")
    
    if not isinstance(data, list) or len(data) == 0:
        raise ValueError(f"YAML文件内容必须是非空列表，格式如：\n[113044,113045]\n[114533,123044]")
    
    periods = []
    for idx, period in enumerate(data, 1):
        if not isinstance(period, list) or len(period) != 2:
            raise ValueError(f"YAML第{idx}行格式错误：必须是包含2个元素的列表（如 [113044,113045]）")
        
        # 转换为字符串并补零（确保是6位）
        start = str(period[0]).zfill(6)
        end = str(period[1]).zfill(6)
        
        if not validate_time_format(start):
            raise ValueError(f"YAML第{idx}行开始时间错误：{period[0]} 不是有效的HHMMSS格式")
        if not validate_time_format(end):
            raise ValueError(f"YAML第{idx}行结束时间错误：{period[1]} 不是有效的HHMMSS格式")
        if start > end:
            raise ValueError(f"YAML第{idx}行时间错误：结束时间 {end} 早于开始时间 {start}")
        
        periods.append((start, end))
    
    return periods

def get_filter_script_config() -> tuple[str, str]:
    """从 filter_rosbag.py 中读取真实的 SOURCE_DIRECTORY 和 OUTPUT_ROOT_DIRECTORY"""
    if not os.path.exists(FILTER_SCRIPT_PATH):
        raise FileNotFoundError(f"未找到筛选脚本：{FILTER_SCRIPT_PATH}")
    
    with open(FILTER_SCRIPT_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 匹配 SOURCE_DIRECTORY（兼容空格、注释）
    source_match = re.search(r'SOURCE_DIRECTORY\s*=\s*"([^"]+)"', content)
    if not source_match:
        raise ValueError(f"未在 {FILTER_SCRIPT_PATH} 中找到 SOURCE_DIRECTORY 配置")
    
    # 匹配 OUTPUT_ROOT_DIRECTORY（兼容空格、注释）
    output_match = re.search(r'OUTPUT_ROOT_DIRECTORY\s*=\s*"([^"]+)"', content)
    if not output_match:
        raise ValueError(f"未在 {FILTER_SCRIPT_PATH} 中找到 OUTPUT_ROOT_DIRECTORY 配置")
    
    return source_match.group(1).strip(), output_match.group(1).strip()

def run_shell_command(command: str, step_name: str) -> None:
    """执行命令，实时打印日志"""
    print(f"\n{'='*60}")
    print(f"🚀 开始执行：{step_name}")
    print(f"命令：{command}")
    print(f"{'='*60}")
    
    process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        executable=os.environ.get('SHELL', '/bin/bash')
    )
        # 读取输出时处理编码问题
    if process.stdout:
        for line in process.stdout:
            try:
                # 尝试用UTF-8解码，无法解码的字符忽略
                print(line.decode('utf-8', errors='ignore').strip())
            except Exception:
                # 若仍失败，用系统默认编码解码
                print(line.decode(sys.getdefaultencoding(), errors='ignore').strip())
    
    process.wait()
    
    if process.returncode != 0:
        print(f"\n❌ 步骤 [{step_name}] 执行失败！错误码：{process.returncode}")
        sys.exit(1)
    
    if process.stdout:
        for line in process.stdout:
            print(line.strip())
    
    process.wait()
    
    if process.returncode != 0:
        print(f"\n❌ step [{step_name}] error! error code :{process.returncode}")
        sys.exit(1)
    print(f"\n✅ step [{step_name}] done！")

def get_filtered_folder_path(output_root: str, start_time: str, end_time: str) -> str:
    """根据 filter_rosbag.py 的逻辑，计算筛选后的目标文件夹路径"""
    return os.path.join(output_root)
    # return os.path.join(output_root, f"{start_time}_{end_time}")

def validate_time_format(time_str: str) -> bool:
    """验证时间格式是否为 HHMMSS（6位数字）"""
    if len(time_str) != 6 or not time_str.isdigit():
        return False
    hh = int(time_str[:2])
    mm = int(time_str[2:4])
    ss = int(time_str[4:6])
    return 0 <= hh < 24 and 0 <= mm < 60 and 0 <= ss < 60

def modify_filter_script(start_time: str, end_time: str) -> None:
    """修改第一个代码（filter_rosbag.py）的 TARGET_START_TIME 和 TARGET_END_TIME"""
    with open(FILTER_SCRIPT_PATH, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    updated_lines = []
    for line in lines:
        if line.strip().startswith("TARGET_START_TIME"):
            updated_lines.append(f'    TARGET_START_TIME = "{start_time}"  # 自动更新于 {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
        elif line.strip().startswith("TARGET_END_TIME"):
            updated_lines.append(f'    TARGET_END_TIME = "{end_time}"    # 自动更新于 {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
        else:
            updated_lines.append(line)
    
    with open(FILTER_SCRIPT_PATH, 'w', encoding='utf-8') as f:
        f.writelines(updated_lines)
    
    print(f"✅ 已更新筛选脚本的时间段配置：")
    print(f"   - 开始时间（TARGET_START_TIME）：{start_time}（HHMMSS）")
    print(f"   - 结束时间（TARGET_END_TIME）：{end_time}（HHMMSS）")

def main():
    import argparse
    parser = argparse.ArgumentParser(description="ROS 2 Bag 时间筛选 + 预处理全流程脚本（先筛选db3，再处理）")
    parser.add_argument("--logtime", type=str, required=True, help="日志时间戳（如：20251124_111515，用于 run_export.py）")
    parser.add_argument("--vehicle", type=str, default=DEFAULT_VEHICLE, help=f"车辆型号（默认：{DEFAULT_VEHICLE}）")
    parser.add_argument("--main-out", type=str, default=DEFAULT_MAIN_OUT, help=f"预处理主输出目录（默认：{DEFAULT_MAIN_OUT}）")
    args = parser.parse_args()
    
    # 1. 读取 filter_rosbag.py 的真实配置（关键修复！）
    try:
        SOURCE_DIRECTORY, OUTPUT_ROOT_DIRECTORY = get_filter_script_config()
    except Exception as e:
        print(f"❌ 读取筛选脚本配置失败：{str(e)}")
        sys.exit(1)
    
    # 2. 检查基础路径
    if not os.path.exists(RUN_EXPORT_SCRIPT_PATH):
        print(f"❌ 未找到预处理脚本：{RUN_EXPORT_SCRIPT_PATH}")
        sys.exit(1)
    if not os.path.exists(SOURCE_DIRECTORY):
        print(f"❌ 源db3目录不存在：{SOURCE_DIRECTORY}")
        sys.exit(1)
    if not os.path.exists(OUTPUT_ROOT_DIRECTORY):
        print(f"❌ 筛选输出根目录不存在：{OUTPUT_ROOT_DIRECTORY}")
        sys.exit(1)
    
    # 3. 终端输入时间段
    print("========================================")
    print("🎬 启动全流程：先筛选db3文件 → 再预处理")
    print("========================================")
    print("请输入筛选时间段（格式：HHMMSS，例如 111515 表示 11:15:15）")
    while True:
        start_time = input("开始时间（HHMMSS）：").strip()
        if validate_time_format(start_time):
            break
        print("❌ 格式错误！请输入6位数字（HH范围00-23，MM/SS范围00-59）")
    
    while True:
        end_time = input("结束时间（HHMMSS）：").strip()
        if validate_time_format(end_time):
            if start_time <= end_time:
                break
            print("❌ 结束时间不能早于开始时间！")
        else:
            print("❌ 格式错误！请输入6位数字（HH范围00-23，MM/SS范围00-59）")
    
    # 4. 计算真实的筛选输出目录（和 filter_rosbag.py 完全一致）
    filtered_folder = get_filtered_folder_path(OUTPUT_ROOT_DIRECTORY, start_time, end_time)
    
    # 5. 打印配置信息（显示真实路径）
    print("\n========================================")
    print(f"📥 源db3目录（来自filter脚本）：{SOURCE_DIRECTORY}")
    print(f"📤 筛选输出目录（自动计算）：{filtered_folder}")
    print(f"⚙️  预处理主输出：{args.main_out}")
    print(f"🚗 车辆型号：{args.vehicle}")
    print(f"⏰ 日志时间戳：{args.logtime}")
    print("========================================\n")
    
    # 6. 更新筛选脚本的时间段
    modify_filter_script(start_time, end_time)
    
    # 7. 执行筛选db3文件
    filter_cmd = f"{sys.executable} {FILTER_SCRIPT_PATH}"
    run_shell_command(filter_cmd, "步骤 1/2：筛选指定时间段的db3文件")
    NEW_PATH = f"{args.main_out}/{start_time}_{end_time}"
    
    # 8. 检查筛选结果（关键：用真实路径检查）
    if not os.path.exists(filtered_folder):
        print(f"❌ 筛选失败：未生成目标文件夹 {filtered_folder}")
        print(f"   请检查：1. filter_rosbag.py 的 _create_output_dir 函数是否正确 2. 源目录是否有符合时间段的db3文件")
        sys.exit(1)
    
    # 9. 执行预处理
    run_export_cmd = (
        f"{sys.executable} {RUN_EXPORT_SCRIPT_PATH} "
        f"--bag {filtered_folder} "
        f"--out {NEW_PATH} "
        f"--vehicle {args.vehicle} "
        f"--logtime {args.logtime}"
    )

    run_shell_command(run_export_cmd, "step 2/2：ROS 2 Bag")
    
    # 10. 输出最终结果
    final_undistorted_dir = os.path.join(NEW_PATH, "undistorted")
    print("\n" + "="*80)
    print("🎉 全流程执行完成！")
    print(f"📁 筛选后的db3文件：{filtered_folder}")
    print(f"📁 预处理最终结果：{final_undistorted_dir}")
    print("="*80)

if __name__ == "__main__":
    main()
