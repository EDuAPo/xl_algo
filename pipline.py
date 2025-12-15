import os
import sys
import subprocess
import yaml
import re
import shutil
from datetime import datetime
from typing import List, Tuple

# ===================== 配置区域（只需要填三个脚本路径！）=====================
# 1. 三个脚本的实际路径（必改！）
FILTER_SCRIPT_PATH = "./filter_by_time.py"  # 第一个代码路径
RUN_EXPORT_SCRIPT_PATH = "./run_export.py"  # 第二个代码路径
CHECK_COMPRESS_SCRIPT_PATH = "./zip_check.py"  # 新增：检查压缩脚本路径（如果不在同一目录，填绝对路径）

# 2. 预处理脚本的默认配置（可选改）
DEFAULT_VEHICLE = "vehicle_000"
DEFAULT_MAIN_OUT = "/media/xl/T7/zgw1201/out"  # 预处理的主输出目录

# 时间段yaml文件
TIME_PERIODS_YAML = "./time_peridos.yaml" 

# 新增配置：db3恢复相关（根据需求调整）
OVERWRITE_ORIGINAL = True  # 恢复时是否覆盖原始db3文件（False则备份原始文件）
BACKUP_SUFFIX = ".bak"     # 原始文件备份后缀（仅当OVERWRITE_ORIGINAL=False时生效）
DB3_FILE_PATTERN = "rosbag2_*.db3"  # 匹配filter_by_time.py生成的db3文件格式

# 新增：检查压缩相关控制参数（可选改）
SKIP_CHECK_COMPRESS = False  # 是否跳过检查压缩流程（默认不跳过）
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
        # 抛出异常，让上层处理（单个时间段失败不影响整体）
        raise RuntimeError(f"步骤 [{step_name}] 执行失败，错误码：{process.returncode}")
    
    print(f"\n✅ 步骤 [{step_name}] 执行完成！")

def get_filtered_folder_path(output_root: str, start_time: str, end_time: str) -> str:
    """
    完全匹配 filter_by_time.py 的输出目录逻辑：
    在 OUTPUT_ROOT_DIRECTORY 下创建 {start_time}_{end_time} 子目录
    """
    return os.path.join(output_root, f"{start_time}_{end_time}")

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

def get_filtered_db3_files(filtered_folder: str) -> List[str]:
    """获取筛选后的所有db3文件路径（匹配 filter_by_time.py 生成的格式）"""
    db3_files = []
    if not os.path.exists(filtered_folder):
        return db3_files
    
    # 关键修复：用 glob 按通配符匹配，完美适配 rosbag2_*.db3 格式
    import glob
    # 拼接完整的匹配路径：筛选目录 + 匹配规则
    pattern = os.path.join(filtered_folder, DB3_FILE_PATTERN)
    # 匹配所有符合规则的文件（自动忽略目录）
    db3_files = glob.glob(pattern)
    
    # 按文件名排序（保证恢复顺序一致，可选但推荐）
    return sorted(db3_files)

def restore_db3_files(filtered_db3_files: List[str], original_source_dir: str, start_time: str, end_time: str) -> None:
    """
    处理完成后，将筛选后的db3文件恢复到原始位置（filter_by_time.py的SOURCE_DIRECTORY）
    """
    print(f"\n🔄 开始恢复db3文件到原始位置（时间段：{start_time} → {end_time}）：")
    print(f"   原始位置：{original_source_dir}")
    
    if not filtered_db3_files:
        print(f"   ⚠️  未找到筛选后的db3文件，跳过恢复")
        return
    
    for filtered_file in filtered_db3_files:
        filename = os.path.basename(filtered_file)
        original_path = os.path.join(original_source_dir, filename)
        
        try:
            # 处理原始文件（备份或直接覆盖）
            if os.path.exists(original_path) and not OVERWRITE_ORIGINAL:
                # 备份原始文件（避免覆盖）
                backup_path = original_path + BACKUP_SUFFIX
                # 若备份文件已存在，添加时间戳避免冲突
                if os.path.exists(backup_path):
                    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                    backup_path = f"{original_path}_{timestamp}{BACKUP_SUFFIX}"
                shutil.copy2(original_path, backup_path)
                print(f"   📦 已备份原始文件：{filename} → {os.path.basename(backup_path)}")
            
            # 将筛选后的文件恢复到原始位置
            shutil.copy2(filtered_file, original_path)
            print(f"   ✅ 恢复完成：{filename} → {original_path}")
        
        except Exception as e:
            print(f"   ❌ 恢复文件 {filename} 失败：{str(e)}")
            continue
    
    print(f"✅ db3文件恢复操作完成！")

def clean_filtered_files(filtered_folder: str) -> None:
    """清理筛选后的临时目录（包含db3和metadata.yaml），节省空间"""
    if os.path.exists(filtered_folder):
        try:
            shutil.rmtree(filtered_folder)
            print(f"\n🗑️  已清理临时筛选目录：{filtered_folder}")
        except Exception as e:
            print(f"\n⚠️  清理临时目录失败：{str(e)}，请手动清理")

def find_undistorted_parent_folder(preprocess_out_dir: str) -> str:
    """
    查找包含 undistorted 文件夹的父目录（适配 run_export.py 的输出结构）
    通常结构：preprocess_out_dir / exported_raw_data / {time_folder} / undistorted
    或：preprocess_out_dir / {time_folder} / undistorted
    """
    # 递归查找 undistorted 文件夹
    for root, dirs, files in os.walk(preprocess_out_dir):
        if "undistorted" in dirs:
            # 返回 undistorted 的父目录（即需要检查压缩的目标文件夹）
            return os.path.join(root, "undistorted")
    
    # 如果直接在 preprocess_out_dir 下找到 undistorted
    undistorted_dir = os.path.join(preprocess_out_dir, "undistorted")
    if os.path.exists(undistorted_dir) and os.path.isdir(undistorted_dir):
        return undistorted_dir
    
    return None

def run_check_and_compress(target_folder: str, output_dir: str, period_idx: int, start_time: str, end_time: str) -> None:
    """调用外部检查压缩脚本"""
    # 验证外部脚本存在
    if not os.path.exists(CHECK_COMPRESS_SCRIPT_PATH):
        raise FileNotFoundError(f"未找到检查压缩脚本：{CHECK_COMPRESS_SCRIPT_PATH}")
    
    # 构建命令（路径加引号，避免空格问题）
    check_compress_cmd = (
        f"{sys.executable} \"{CHECK_COMPRESS_SCRIPT_PATH}\" "
        f"\"{target_folder}\" "
        f"\"{output_dir}\""
    )
    
    # 执行外部脚本
    run_shell_command(
        check_compress_cmd,
        f"第{period_idx}个时间段 - 步骤3/3：检查+清理+压缩流程"
    )

def process_single_period(
    period_idx: int,
    start_time: str,
    end_time: str,
    source_dir: str,  # filter_by_time.py的SOURCE_DIRECTORY（原始db3位置）
    output_root: str, # filter_by_time.py的OUTPUT_ROOT_DIRECTORY（筛选输出根目录）
    logtime: str,
    vehicle: str,
    main_out: str,
    no_restore: bool,
    no_clean: bool
) -> None:
    """
    处理单个时间段的全流程（适配 filter_by_time.py 逻辑）：
    1. 更新筛选脚本时间段 → 2. 执行筛选 → 3. 预处理 → 4. 检查+清理+压缩 → 5. 恢复db3 → 6. 清理临时文件
    """
    print(f"\n{'='*80}")
    print(f"📌 开始处理第 {period_idx}/{total_periods} 个时间段：{start_time} → {end_time}")
    print(f"{'='*80}")
    
    # 1. 计算筛选后的目标目录（完全匹配 filter_by_time.py 逻辑）
    filtered_folder = get_filtered_folder_path(output_root, start_time, end_time)
    
    # 2. 构建预处理输出路径
    preprocess_out_dir = os.path.join(main_out, f"{start_time}_{end_time}")
    os.makedirs(preprocess_out_dir, exist_ok=True)
    
    # 3. 打印当前时间段的配置信息
    print(f"\n📥 原始db3目录（来自filter脚本）：{source_dir}")
    print(f"📤 筛选输出目录（临时）：{filtered_folder}")
    print(f"⚙️  预处理输出目录：{preprocess_out_dir}")
    print(f"🚗 车辆型号：{vehicle}")
    print(f"⏰ 日志时间戳：{logtime}")
    print(f"🔧 处理模式：filter脚本自动拷贝db3 → 预处理 → {'检查+压缩' if not SKIP_CHECK_COMPRESS else '跳过检查压缩'} → {'恢复' if not no_restore else '不恢复'}db3")
    
    # 4. 更新筛选脚本的时间段配置
    modify_filter_script(start_time, end_time)
    
    # 5. 执行筛选（filter_by_time.py会自动完成：查找匹配db3 → 拷贝到filtered_folder → 生成metadata.yaml）
    filter_cmd = f"{sys.executable} {FILTER_SCRIPT_PATH}"
    run_shell_command(filter_cmd, f"第{period_idx}个时间段 - 步骤1/3：筛选db3文件（自动拷贝）")
    
    # 6. 检查筛选结果（必须包含db3文件）
    filtered_db3_files = get_filtered_db3_files(filtered_folder)
    for db3_file in filtered_db3_files:
        print(f"   - {os.path.basename(db3_file)}")
    
    # 7. 执行预处理（run_export.py）
    run_export_cmd = (
        f"{sys.executable} {RUN_EXPORT_SCRIPT_PATH} "
        f"--bag {filtered_folder} "  # 传入筛选后的目录（含db3和metadata.yaml）
        f"--out {preprocess_out_dir} "
        f"--vehicle {vehicle} "
        f"--logtime {logtime}"
    )
    run_shell_command(run_export_cmd, f"第{period_idx}个时间段 - 步骤2/3：预处理数据")
    
    # 8. 检查+清理+压缩（调用外部脚本）
    if not SKIP_CHECK_COMPRESS:
        print(f"\n{'='*60}")
        print(f"🔍 开始执行检查+清理+压缩流程（时间段：{start_time} → {end_time}）")
        print(f"{'='*60}")
        
        # 查找包含 undistorted 的目标文件夹
        target_folder = find_undistorted_parent_folder(preprocess_out_dir)
        if not target_folder:
            print(f"⚠️  未找到 undistorted 文件夹，跳过检查压缩流程")
        else:
            print(f"📁 待检查压缩的目标文件夹：{target_folder}")
            try:
                run_check_and_compress(
                    target_folder=target_folder,
                    output_dir=preprocess_out_dir,  # 压缩包保存在当前时间段的预处理目录下
                    period_idx=period_idx,
                    start_time=start_time,
                    end_time=end_time
                )
            except Exception as e:
                print(f"⚠️  检查压缩流程失败：{str(e)}")
                print(f"   继续执行后续步骤...")
    
    # 9. 恢复db3文件到原始位置（如果启用）
    if not no_restore:
        try:
            restore_db3_files(filtered_db3_files, source_dir, start_time, end_time)
        except Exception as e:
            print(f"\n⚠️ db3文件恢复过程中出现警告：{str(e)}")
    
    # 10. 清理临时筛选目录（如果启用）
    if not no_clean:
        clean_filtered_files(filtered_folder)
    
    # 11. 打印当前时间段完成信息
    print(f"\n✅ 第 {period_idx} 个时间段处理完成！")
    print(f"   预处理结果：{preprocess_out_dir}")
    if not SKIP_CHECK_COMPRESS and target_folder:
        zip_filename = f"{os.path.basename(os.path.dirname(target_folder))}.zip"
        zip_path = os.path.join(preprocess_out_dir, zip_filename)
        if os.path.exists(zip_path):
            print(f"   压缩包位置：{zip_path}")
    print(f"   原始db3位置：{source_dir}（{'已更新为筛选后的数据' if not no_restore else '未修改'}）")
    print(f"{'='*80}\n")

def main():
    global total_periods  # 全局变量，用于在子函数中显示总进度
    
    import argparse
    parser = argparse.ArgumentParser(description="ROS 2 Bag 批量时间筛选 + 预处理 + 外部检查压缩全流程脚本（支持db3恢复）")
    parser.add_argument("--logtime", type=str, required=True, help="日志时间戳（如：20251124_111515，用于 run_export.py）")
    parser.add_argument("--vehicle", type=str, default=DEFAULT_VEHICLE, help=f"车辆型号（默认：{DEFAULT_VEHICLE}）")
    parser.add_argument("--main-out", type=str, default=DEFAULT_MAIN_OUT, help=f"预处理主输出目录（默认：{DEFAULT_MAIN_OUT}）")
    parser.add_argument("--yaml-path", type=str, default=TIME_PERIODS_YAML, help=f"时间段配置YAML文件路径（默认：{TIME_PERIODS_YAML}）")
    parser.add_argument("--no-restore", action="store_true", help="禁用db3恢复（处理后不拷贝回原始位置，默认启用恢复）")
    parser.add_argument("--no-clean", action="store_true", help="禁用临时文件清理（保留筛选目录，默认启用清理）")
    parser.add_argument("--skip-check-compress", action="store_true", help="跳过检查+清理+压缩流程（默认不跳过）")
    args = parser.parse_args()
    
    # 更新全局变量
    global SKIP_CHECK_COMPRESS
    SKIP_CHECK_COMPRESS = args.skip_check_compress
    
    # 1. 加载时间段配置
    try:
        time_periods = load_time_periods(args.yaml_path)
        total_periods = len(time_periods)
        print(f"✅ 成功加载 {total_periods} 个时间段：")
        for i, (start, end) in enumerate(time_periods, 1):
            print(f"   {i}. {start} → {end}")
    except Exception as e:
        print(f"❌ 加载时间段配置失败：{str(e)}")
        sys.exit(1)
    
    # 2. 读取 filter_by_time.py 的真实配置（SOURCE和OUTPUT目录）
    try:
        SOURCE_DIRECTORY, OUTPUT_ROOT_DIRECTORY = get_filter_script_config()
    except Exception as e:
        print(f"❌ 读取筛选脚本配置失败：{str(e)}")
        sys.exit(1)
    
    # 3. 检查基础路径有效性
    if not os.path.exists(RUN_EXPORT_SCRIPT_PATH):
        print(f"❌ 未找到预处理脚本：{RUN_EXPORT_SCRIPT_PATH}")
        sys.exit(1)
    if not SKIP_CHECK_COMPRESS and not os.path.exists(CHECK_COMPRESS_SCRIPT_PATH):
        print(f"❌ 未找到检查压缩脚本：{CHECK_COMPRESS_SCRIPT_PATH}")
        print(f"   请确保脚本路径正确，或使用 --skip-check-compress 跳过该流程")
        sys.exit(1)
    if not os.path.exists(SOURCE_DIRECTORY):
        print(f"❌ 原始db3目录不存在：{SOURCE_DIRECTORY}")
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
    
    # 4. 创建预处理主输出目录（如果不存在）
    os.makedirs(args.main_out, exist_ok=True)
    
    # 5. 打印全局配置信息
    print("\n========================================")
    print("📋 全局配置信息")
    print("========================================")
    print(f"📥 原始db3目录（来自filter脚本）：{SOURCE_DIRECTORY}")
    print(f"📤 筛选输出根目录（临时）：{OUTPUT_ROOT_DIRECTORY}")
    print(f"⚙️  预处理主输出：{args.main_out}")
    print(f"🚗 车辆型号：{args.vehicle}")
    print(f"⏰ 日志时间戳：{args.logtime}")
    print(f"📄 YAML配置文件：{args.yaml_path}")
    print(f"🔧 DB3恢复模式：{'启用' if not args.no_restore else '禁用'}")
    print(f"🔧 临时文件清理：{'启用' if not args.no_clean else '禁用'}")
    print(f"🔧 检查压缩流程：{'启用' if not SKIP_CHECK_COMPRESS else '禁用'}")
    if not SKIP_CHECK_COMPRESS:
        print(f"🔧 检查压缩脚本：{CHECK_COMPRESS_SCRIPT_PATH}")
    print(f"🔧 原始文件覆盖：{'是' if OVERWRITE_ORIGINAL else '否（自动备份）'}")
    print("========================================\n")
    
    # 6. 批量处理每个时间段
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
                main_out=args.main_out,
                no_restore=args.no_restore,
                no_clean=args.no_clean
            )
            success_count += 1
        except Exception as e:
            print(f"\n❌ 第 {period_idx} 个时间段处理异常：{str(e)}")
            print(f"   跳过当前时间段，继续处理下一个...\n")
            fail_count += 1
            continue
    
    # 7. 输出总体统计结果
    print(f"\n{'='*80}")
    print("📊 批量处理完成！总体统计：")
    print(f"   总时间段数：{total_periods}")
    print(f"   成功处理：{success_count} 个")
    print(f"   失败/跳过：{fail_count} 个")
    print(f"📁 所有预处理结果均保存在：{args.main_out}")
    print(f"   （每个时间段对应一个 {start_time}_{end_time} 子目录）")
    if not SKIP_CHECK_COMPRESS:
        print(f"   （每个时间段的压缩包保存在对应子目录下）")
    print(f"💡 原始db3文件{'已恢复' if not args.no_restore else '未恢复'}到：{SOURCE_DIRECTORY}")
    print(f"{'='*80}")

if __name__ == "__main__":
    main()
