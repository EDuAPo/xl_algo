import os
import sys
import subprocess
import yaml
import re
import shutil
import json  # 新增：用于解析sample.json
from datetime import datetime
from typing import List, Tuple, Optional, Set

# ===================== 配置区域（只需要填两个脚本路径！）=====================
# 1. 核心脚本路径（你的正确配置）
FILTER_SCRIPT_PATH = "./filter_by_time.py"  # 筛选脚本
RUN_EXPORT_SCRIPT_PATH = "./run_export.py"  # 预处理脚本
CHECK_COMPRESS_SCRIPT_PATH = "./check_and_compress.py"  # 检查压缩脚本（需确保存在）

# 2. 基础配置（你的正确配置）
DEFAULT_VEHICLE = "vehicle_000"
DEFAULT_MAIN_OUT = "/media/xl/MyPass/zgw1201/140356_140541/out1"  # 预处理主输出目录
TIME_PERIODS_YAML = "./time_peridos.yaml"  # 时间段配置文件

# 3. 新增：检查压缩功能配置
SKIP_CHECK_COMPRESS = False  # 是否跳过压缩流程（默认不跳过）
COMPRESS_FORMAT = "zip"  # 压缩格式（支持 zip/tar/gz，需与压缩脚本适配）
DELETE_RAW_UNDISTORTED = False  # 压缩后是否删除原始 undistorted 目录（节省空间，默认True）
# 新增：需要清理的文件后缀（只清理这两种）
CLEAN_SUFFIXES = (".pcd", ".jpg")
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
    """从 filter_by_time.py 中读取真实的 SOURCE_DIRECTORY 和 OUTPUT_ROOT_DIRECTORY"""
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
    """执行命令，实时打印日志（保留你的原有逻辑，修复重复打印问题）"""
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
    
    # 读取输出时处理编码问题（修复原有重复读取stdout的bug）
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
    
    print(f"\n✅ 步骤 [{step_name}] 执行完成！")

def get_filtered_folder_path(output_root: str, start_time: str, end_time: str) -> str:
    """根据你的原有逻辑，计算筛选后的目标文件夹路径（不额外创建子目录）"""
    return os.path.join(output_root)

def validate_time_format(time_str: str) -> bool:
    """验证时间格式是否为 HHMMSS（6位数字）"""
    if len(time_str) != 6 or not time_str.isdigit():
        return False
    hh = int(time_str[:2])
    mm = int(time_str[2:4])
    ss = int(time_str[4:6])
    return 0 <= hh < 24 and 0 <= mm < 60 and 0 <= ss < 60

def modify_filter_script(start_time: str, end_time: str) -> None:
    """修改 filter_by_time.py 的 TARGET_START_TIME 和 TARGET_END_TIME"""
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

# ===================== 新增/修改：文件清理相关函数 =====================
def parse_sample_json(sample_json_path: str) -> Set[str]:
    """解析sample.json，提取所有有效的.pcd和.jpg文件名（排除NOT_FOUND）"""
    valid_filenames = set()
    
    if not os.path.exists(sample_json_path):
        raise FileNotFoundError(f"未找到sample.json文件：{sample_json_path}")
    
    with open(sample_json_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"sample.json格式错误：{str(e)}")
    
    if not isinstance(data, list):
        raise ValueError(f"sample.json内容必须是列表格式")
    
    for item in data:
        if not isinstance(item, dict):
            continue  # 跳过非字典项
        
        # 遍历每个字段的值，提取有效的文件名
        for value in item.values():
            if not isinstance(value, str) or value == "NOT_FOUND":
                continue  # 跳过非字符串或NOT_FOUND
            
            # 只保留指定后缀的文件
            if value.lower().endswith(CLEAN_SUFFIXES):
                valid_filenames.add(value)
    
    print(f"✅ 从sample.json中提取到 {len(valid_filenames)} 个有效文件（.pcd/.jpg）")
    return valid_filenames

def clean_invalid_files(undistorted_path: str, valid_filenames: Set[str]) -> None:
    """递归遍历undistorted目录，删除不在valid_filenames中的.pcd和.jpg文件"""
    deleted_count = 0
    skipped_count = 0
    
    print(f"\n🔍 开始清理无效文件（仅删除.pcd和.jpg，且不在sample.json中）")
    print(f"清理目录：{undistorted_path}")
    print(f"需保留的有效文件数：{len(valid_filenames)}")
    
    # 递归遍历所有子目录
    for root, dirs, files in os.walk(undistorted_path):
        for filename in files:
            # 只处理指定后缀的文件
            if filename.lower().endswith(CLEAN_SUFFIXES):
                # 检查文件名是否在有效列表中
                if filename not in valid_filenames:
                    file_path = os.path.join(root, filename)
                    try:
                        os.remove(file_path)
                        print(f"🗑️ 删除无效文件：{file_path}")
                        deleted_count += 1
                    except Exception as e:
                        print(f"⚠️ 删除文件失败：{file_path} → {str(e)}")
                        skipped_count += 1
                else:
                    skipped_count += 1  # 有效文件，跳过
    
    print(f"\n📊 清理完成：")
    print(f"   - 已删除无效文件：{deleted_count} 个")
    print(f"   - 保留有效文件：{skipped_count - deleted_count} 个")
    print(f"   - 跳过文件（其他后缀/删除失败）：{deleted_count if skipped_count == 0 else skipped_count - (deleted_count + (skipped_count - deleted_count))} 个")

def pre_compress_cleanup(undistorted_path: str) -> None:
    """压缩前的清理流程：解析sample.json → 清理无效文件"""
    # 1. 找到sample.json路径
    sample_json_path = os.path.join(undistorted_path, "sample.json")
    
    # 2. 解析sample.json获取有效文件列表
    valid_filenames = parse_sample_json(sample_json_path)
    
    # 3. 清理无效文件
    clean_invalid_files(undistorted_path, valid_filenames)

# ===================== 新增：检查压缩相关函数 =====================
def find_undistorted_folder(preprocess_out_dir: str) -> Optional[str]:
    """在预处理输出目录下查找 undistorted 文件夹（递归查找，适配不同目录结构）"""
    for root, dirs, files in os.walk(preprocess_out_dir):
        if "undistorted" in dirs:
            return os.path.join(root, "undistorted")  # 返回 undistorted 文件夹的完整路径
    return None

def run_check_and_compress(
    undistorted_path: str,
    compress_output_dir: str,
    period_idx: int,
    start_time: str,
    end_time: str
) -> str:
    """调用外部检查压缩脚本，执行压缩流程，返回压缩包路径"""
    # 构建压缩包名称（包含时间段，便于识别）
    compress_filename = f"undistorted_{start_time}_{end_time}.{COMPRESS_FORMAT}"
    compress_path = os.path.join(compress_output_dir, compress_filename)
    
    # 构建压缩命令（参数与外部脚本适配）
    check_compress_cmd = (
        f"{sys.executable} {CHECK_COMPRESS_SCRIPT_PATH} "
        f"--undistorted-path {undistorted_path} "  # undistorted 文件夹路径
        f"--compress-path {compress_path} "        # 压缩包输出路径
        f"--compress-format {COMPRESS_FORMAT} "    # 压缩格式
        f"--period {start_time}_{end_time}"        # 时间段标识（日志用）
    )
    
    # 执行压缩脚本
    run_shell_command(
        check_compress_cmd,
        f"第{period_idx}个时间段 - 步骤3/3：检查+压缩"
    )
    
    return compress_path

def delete_raw_undistorted(undistorted_path: str) -> None:
    """压缩完成后，删除原始 undistorted 目录（节省空间）"""
    if DELETE_RAW_UNDISTORTED and os.path.exists(undistorted_path):
        try:
            shutil.rmtree(undistorted_path)
            print(f"✅ 已删除原始 undistorted 目录：{undistorted_path}")
        except Exception as e:
            print(f"⚠️  删除原始 undistorted 目录失败：{str(e)}，请手动清理")

# =======================================================================

def process_single_period(
    period_idx: int,
    start_time: str,
    end_time: str,
    source_dir: str,
    output_root: str,
    logtime: str,
    vehicle: str,
    main_out: str
) -> None:
    """处理单个时间段的全流程（筛选+预处理+清理无效文件+检查压缩）- 基于你的原有逻辑扩展"""
    print(f"\n{'='*80}")
    print(f"📌 开始处理第 {period_idx}/{total_periods} 个时间段：{start_time} → {end_time}")
    print(f"{'='*80}")
    
    # 1. 计算真实的筛选输出目录（你的原有逻辑）
    filtered_folder = get_filtered_folder_path(output_root, start_time, end_time)
    
    # 2. 构建预处理输出路径（你的原有逻辑）
    preprocess_out_dir = os.path.join(main_out, f"{start_time}_{end_time}")
    
    # 3. 打印当前时间段的配置信息（新增压缩相关显示）
    print(f"\n📥 源db3目录：{source_dir}")
    print(f"📤 筛选输出目录：{filtered_folder}")
    print(f"⚙️  预处理输出目录：{preprocess_out_dir}")
    print(f"🗜️  压缩包输出目录：{preprocess_out_dir}（与预处理目录相同）")
    print(f"🚗 车辆型号：{vehicle}")
    print(f"⏰ 日志时间戳：{logtime}")
    print(f"🔧 压缩配置：格式={COMPRESS_FORMAT} | 压缩后{'删除' if DELETE_RAW_UNDISTORTED else '保留'}原始目录")
    print(f"🧹 清理配置：仅删除不在sample.json中的.pcd和.jpg文件")
    
    # 4. 更新筛选脚本的时间段（你的原有逻辑）
    modify_filter_script(start_time, end_time)
    
    # 5. 执行筛选db3文件（你的原有逻辑）
    filter_cmd = f"{sys.executable} {FILTER_SCRIPT_PATH}"
    run_shell_command(filter_cmd, f"第{period_idx}个时间段 - 步骤1/4：筛选db3文件")
    
    # 6. 检查筛选结果（你的原有逻辑）
    if not os.path.exists(filtered_folder):
        print(f"❌ 筛选失败：未生成目标文件夹 {filtered_folder}")
        print(f"   跳过当前时间段，继续处理下一个...")
        return
    
    # 7. 执行预处理（你的原有逻辑）
    run_export_cmd = (
        f"{sys.executable} {RUN_EXPORT_SCRIPT_PATH} "
        f"--bag {filtered_folder} "
        f"--out {preprocess_out_dir} "
        f"--vehicle {vehicle} "
        f"--logtime {logtime}"
    )
    run_shell_command(run_export_cmd, f"第{period_idx}个时间段 - 步骤2/4：预处理")
    
    # 8. 新增：检查+压缩流程（默认启用）- 插入清理步骤
    compress_path = None
    if not SKIP_CHECK_COMPRESS:
        print(f"\n{'='*60}")
        print(f"🔍 开始执行检查+清理+压缩流程（时间段：{start_time} → {end_time}）")
        print(f"{'='*60}")
        
        # 检查压缩脚本是否存在
        if not os.path.exists(CHECK_COMPRESS_SCRIPT_PATH):
            raise FileNotFoundError(f"未找到检查压缩脚本：{CHECK_COMPRESS_SCRIPT_PATH}")
        
        # 查找 undistorted 文件夹
        undistorted_path = find_undistorted_folder(preprocess_out_dir)
        if not undistorted_path:
            print(f"⚠️  未在 {preprocess_out_dir} 下找到 undistorted 文件夹，跳过压缩流程")
        else:
            print(f"📁 待处理的 undistorted 目录：{undistorted_path}")
            try:
                # 新增步骤：压缩前清理无效文件（步骤2.5/4）
                pre_compress_cleanup(undistorted_path)
                
                # 执行压缩
                compress_path = run_check_and_compress(
                    undistorted_path=undistorted_path,
                    compress_output_dir=preprocess_out_dir,
                    period_idx=period_idx,
                    start_time=start_time,
                    end_time=end_time
                )
                # 压缩后删除原始目录（可选）
                delete_raw_undistorted(undistorted_path)
            except Exception as e:
                print(f"⚠️  清理/压缩流程失败：{str(e)}，继续执行后续步骤")
    
    # 9. 打印当前时间段完成信息（新增压缩结果显示）
    print(f"\n✅ 第 {period_idx} 个时间段处理完成！")
    print(f"   筛选结果：{filtered_folder}")
    print(f"   预处理结果：{preprocess_out_dir}")
    if compress_path and os.path.exists(compress_path):
        print(f"   压缩包生成：{compress_path}")
    else:
        print(f"   压缩状态：{'未生成' if not SKIP_CHECK_COMPRESS else '已跳过'}")
    print(f"{'='*80}\n")

def main():
    global total_periods  # 全局变量，用于在子函数中显示总进度
    
    import argparse
    parser = argparse.ArgumentParser(description="ROS 2 Bag 批量时间筛选 + 预处理 + 清理无效文件 + 检查压缩全流程脚本")
    parser.add_argument("--logtime", type=str, required=True, help="日志时间戳（如：20251124_111515，用于 run_export.py）")
    parser.add_argument("--vehicle", type=str, default=DEFAULT_VEHICLE, help=f"车辆型号（默认：{DEFAULT_VEHICLE}）")
    parser.add_argument("--main-out", type=str, default=DEFAULT_MAIN_OUT, help=f"预处理主输出目录（默认：{DEFAULT_MAIN_OUT}）")
    parser.add_argument("--yaml-path", type=str, default=TIME_PERIODS_YAML, help=f"时间段配置YAML文件路径（默认：{TIME_PERIODS_YAML}）")
    parser.add_argument("--skip-check-compress", action="store_true", help=f"跳过检查压缩流程（默认不跳过，优先级高于配置文件）")
    args = parser.parse_args()
    
    # 覆盖配置：命令行参数优先于配置文件
    global SKIP_CHECK_COMPRESS
    if args.skip_check_compress:
        SKIP_CHECK_COMPRESS = True
    
    # 1. 加载时间段配置（你的原有逻辑）
    try:
        time_periods = load_time_periods(args.yaml_path)
        total_periods = len(time_periods)
        print(f"✅ 成功加载 {total_periods} 个时间段：")
        for i, (start, end) in enumerate(time_periods, 1):
            print(f"   {i}. {start} → {end}")
    except Exception as e:
        print(f"❌ 加载时间段配置失败：{str(e)}")
        sys.exit(1)
    
    # 2. 读取 filter_by_time.py 的真实配置（你的原有逻辑）
    try:
        SOURCE_DIRECTORY, OUTPUT_ROOT_DIRECTORY = get_filter_script_config()
    except Exception as e:
        print(f"❌ 读取筛选脚本配置失败：{str(e)}")
        sys.exit(1)
    
    # 3. 检查基础路径（新增压缩脚本检查）
    required_scripts = [
        (FILTER_SCRIPT_PATH, "筛选脚本"),
        (RUN_EXPORT_SCRIPT_PATH, "预处理脚本"),
    ]
    if not SKIP_CHECK_COMPRESS:
        required_scripts.append((CHECK_COMPRESS_SCRIPT_PATH, "检查压缩脚本"))
    
    for script_path, script_name in required_scripts:
        if not os.path.exists(script_path):
            print(f"❌ 未找到{script_name}：{script_path}")
            sys.exit(1)
    
    if not os.path.exists(SOURCE_DIRECTORY):
        print(f"❌ 源db3目录不存在：{SOURCE_DIRECTORY}")
        sys.exit(1)
    if not os.path.exists(OUTPUT_ROOT_DIRECTORY):
        print(f"⚠️  筛选输出根目录不存在：{OUTPUT_ROOT_DIRECTORY}")
        print(f"   正在自动创建该目录...")
        try:
            os.makedirs(OUTPUT_ROOT_DIRECTORY, exist_ok=True)
            print(f"✅ 成功创建筛选输出根目录：{OUTPUT_ROOT_DIRECTORY}")
        except Exception as e:
            print(f"❌ 创建筛选输出根目录失败：{str(e)}")
            sys.exit(1)
    
    # 4. 创建主输出目录（你的原有逻辑）
    os.makedirs(args.main_out, exist_ok=True)
    
    # 5. 打印全局配置信息（新增清理和压缩相关配置）
    print("\n========================================")
    print("📋 全局配置信息")
    print("========================================")
    print(f"📥 源db3目录（来自filter脚本）：{SOURCE_DIRECTORY}")
    print(f"📤 筛选输出根目录：{OUTPUT_ROOT_DIRECTORY}")
    print(f"⚙️  预处理主输出：{args.main_out}")
    print(f"🚗 车辆型号：{args.vehicle}")
    print(f"⏰ 日志时间戳：{args.logtime}")
    print(f"📄 YAML配置文件：{args.yaml_path}")
    print(f"🗜️  检查压缩流程：{'启用' if not SKIP_CHECK_COMPRESS else '禁用'}")
    if not SKIP_CHECK_COMPRESS:
        print(f"🗜️  压缩格式：{COMPRESS_FORMAT}")
        print(f"🗜️  压缩后删除原始目录：{'是' if DELETE_RAW_UNDISTORTED else '否'}")
        print(f"🗜️  检查压缩脚本：{CHECK_COMPRESS_SCRIPT_PATH}")
        print(f"🧹 清理配置：仅删除不在sample.json中的.pcd和.jpg文件")
    print("========================================\n")
    
    # 6. 批量处理每个时间段（你的原有逻辑）
    success_count = 0
    fail_count = 0
    
    for period_idx, (start_time, end_time) in enumerate(time_periods, 1):
        try:
            process_single_period(
                period_idx=period_idx,
                start_time=start_time,
                end_time=end_time,
                source_dir=SOURCE_DIRECTORY,
                output_root=OUTPUT_ROOT_DIRECTORY,
                logtime=args.logtime,
                vehicle=args.vehicle,
                main_out=args.main_out
            )
            success_count += 1
        except Exception as e:
            print(f"\n❌ 第 {period_idx} 个时间段处理异常：{str(e)}")
            print(f"   跳过当前时间段，继续处理下一个...\n")
            fail_count += 1
            continue
    
    # 7. 输出总体统计结果（新增压缩相关统计）
    print(f"\n{'='*80}")
    print("📊 批量处理完成！总体统计：")
    print(f"   总时间段数：{total_periods}")
    print(f"   成功处理：{success_count} 个")
    print(f"   失败/跳过：{fail_count} 个")
    print(f"📁 所有预处理结果均保存在：{args.main_out}")
    print(f"   （每个时间段对应一个 {start_time}_{end_time} 子目录，压缩包在该目录下）")
    print(f"🧹 已自动清理每个undistorted目录中不在sample.json的.pcd和.jpg文件")
    print(f"{'='*80}")

if __name__ == "__main__":
    main()
