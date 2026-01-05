import os
import sys
import subprocess
import yaml
import re
import shutil
import json
import tempfile
import time
from datetime import datetime
from typing import List, Tuple, Optional, Dict, Set

# ===================== 配置区域 =====================
# 1. 核心脚本路径
FILTER_SCRIPT_PATH = "./move_file.py"  # 筛选脚本
RUN_EXPORT_SCRIPT_PATH = "./run_export.py"  # 预处理脚本
CHECK_COMPRESS_SCRIPT_PATH = "./check_and_compress.py"  # 检查压缩脚本

# 2. 基础配置
DEFAULT_VEHICLE = "vehicle_000"
DEFAULT_MAIN_OUT = "/media/zgw/5211BF7864DFC4FA/1230out/"  # 预处理主输出目录
TIME_PERIODS_YAML = "./time_peridos.yaml"  # 时间段配置文件

# 3. 新增：移动模式配置
MOVE_MODE = True  # 是否使用移动模式（默认True，最节省空间）
MOVE_RECORD_DIR = "/media/zgw/5211BF7864DFC4FA/1230out/"  # 移动记录保存目录

# 4. 新增：检查压缩功能配置
SKIP_CHECK_COMPRESS = False  # 是否跳过压缩流程（默认不跳过）
COMPRESS_FORMAT = "zip"  # 压缩格式
DELETE_RAW_UNDISTORTED = False  # 压缩后是否删除原始 undistorted 目录

# 5. 新增：simple.json 清理配置
CLEAN_BY_SIMPLE_JSON = True  # 是否根据simple.json清理文件
SIMPLE_JSON_NAME = "sample.json"  # simple.json文件名

# 6. 全局日志数据结构
PIPELINE_LOG = {
    "session_info": {},
    "periods_processed": [],
    "summary": {}
}
SESSION_START_TIME = 0  # 会话开始时间
# ===================================================

def save_pipeline_log(output_dir: str) -> None:
    """保存流程日志到JSON文件"""
    log_filename = "pipeline_log.json"
    log_path = os.path.join(output_dir, log_filename)
    try:
        with open(log_path, 'w', encoding='utf-8') as f:
            json.dump(PIPELINE_LOG, f, ensure_ascii=False, indent=2)
        print(f"\n📝 流程日志已保存: {log_filename}")
        return log_path
    except Exception as e:
        print(f"\n⚠️  保存流程日志失败: {e}")
        return None


def load_time_periods(yaml_path: str) -> List[Tuple[str, str]]:
    """从YAML文件加载时间段列表"""
    if not os.path.exists(yaml_path):
        raise FileNotFoundError(f"未找到时间段配置文件：{yaml_path}")
    
    with open(yaml_path, 'r', encoding='utf-8') as f:
        try:
            data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            raise ValueError(f"YAML文件格式错误：{str(e)}")
    
    if not isinstance(data, list) or len(data) == 0:
        raise ValueError(f"YAML文件内容必须是非空列表")
    
    periods = []
    for idx, period in enumerate(data, 1):
        if not isinstance(period, list) or len(period) != 2:
            raise ValueError(f"YAML第{idx}行格式错误：必须是包含2个元素的列表")
        
        # 转换为字符串并补零
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
    """从 filter_by_time.py 中读取真实的默认配置"""
    if not os.path.exists(FILTER_SCRIPT_PATH):
        raise FileNotFoundError(f"未找到筛选脚本：{FILTER_SCRIPT_PATH}")
    
    with open(FILTER_SCRIPT_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 匹配默认配置（修改后的模式）
    source_match = re.search(r'DEFAULT_SOURCE_DIRECTORY\s*=\s*"([^"]+)"', content)
    if not source_match:
        # 回退到旧模式
        source_match = re.search(r'SOURCE_DIRECTORY\s*=\s*"([^"]+)"', content)
        if not source_match:
            raise ValueError(f"未在 {FILTER_SCRIPT_PATH} 中找到源目录配置")
    
    output_match = re.search(r'DEFAULT_OUTPUT_ROOT_DIRECTORY\s*=\s*"([^"]+)"', content)
    if not output_match:
        # 回退到旧模式
        output_match = re.search(r'OUTPUT_ROOT_DIRECTORY\s*=\s*"([^"]+)"', content)
        if not output_match:
            raise ValueError(f"未在 {FILTER_SCRIPT_PATH} 中找到输出目录配置")
    
    return source_match.group(1).strip(), output_match.group(1).strip()


def run_shell_command(command: str, step_name: str) -> dict:
    """执行命令，实时打印日志，返回执行信息"""
    start_time = time.time()
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
    
    if process.stdout:
        for line in process.stdout:
            try:
                print(line.decode('utf-8', errors='ignore').strip())
            except Exception:
                print(line.decode(sys.getdefaultencoding(), errors='ignore').strip())
    
    process.wait()
    duration = time.time() - start_time
    
    result = {
        "step_name": step_name,
        "command": command,
        "return_code": process.returncode,
        "duration_seconds": round(duration, 2),
        "status": "success" if process.returncode == 0 else "failed"
    }
    
    if process.returncode != 0:
        print(f"\n❌ 步骤 [{step_name}] 执行失败！错误码：{process.returncode}")
        raise RuntimeError(f"步骤 [{step_name}] 执行失败！错误码：{process.returncode}")
    
    # 优化：强制同步磁盘，防止IO积压导致后续步骤变慢
    subprocess.run("sync", shell=True)
    
    print(f"\n✅ 步骤 [{step_name}] 执行完成！（耗时: {duration:.2f}秒）")
    return result


def get_filtered_folder_path(output_root: str, start_time: str, end_time: str) -> str:
    """根据你的原有逻辑，计算筛选后的目标文件夹路径"""
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
    """修改 filter_by_time.py 的默认时间配置"""
    with open(FILTER_SCRIPT_PATH, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    updated_lines = []
    for line in lines:
        if line.strip().startswith("DEFAULT_TARGET_START_TIME"):
            updated_lines.append(f'DEFAULT_TARGET_START_TIME = "{start_time}"  # 自动更新于 {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
        elif line.strip().startswith("DEFAULT_TARGET_END_TIME"):
            updated_lines.append(f'DEFAULT_TARGET_END_TIME = "{end_time}"    # 自动更新于 {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
        # 也处理旧的配置名称
        elif line.strip().startswith("TARGET_START_TIME") and not line.strip().startswith("DEFAULT_"):
            updated_lines.append(f'TARGET_START_TIME = "{start_time}"  # 自动更新于 {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
        elif line.strip().startswith("TARGET_END_TIME") and not line.strip().startswith("DEFAULT_"):
            updated_lines.append(f'TARGET_END_TIME = "{end_time}"    # 自动更新于 {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
        else:
            updated_lines.append(line)
    
    with open(FILTER_SCRIPT_PATH, 'w', encoding='utf-8') as f:
        f.writelines(updated_lines)
    
    print(f"✅ 已更新筛选脚本的时间段配置：")
    print(f"   - 开始时间：{start_time}（HHMMSS）")
    print(f"   - 结束时间：{end_time}（HHMMSS）")


def save_move_record(period_idx: int, start_time: str, end_time: str, moved_files: Dict[str, str]) -> str:
    """保存移动文件记录到JSON文件"""
    os.makedirs(MOVE_RECORD_DIR, exist_ok=True)
    
    record_filename = f"move_record_{period_idx:03d}_{start_time}_{end_time}.json"
    record_path = os.path.join(MOVE_RECORD_DIR, record_filename)
    
    with open(record_path, 'w', encoding='utf-8') as f:
        json.dump({
            'period_idx': period_idx,
            'start_time': start_time,
            'end_time': end_time,
            'moved_files': moved_files,
            'timestamp': datetime.now().isoformat()
        }, f, indent=2, ensure_ascii=False)
    
    print(f"📝 已保存移动记录到：{record_path}")
    return record_path


def restore_moved_files(record_path: str) -> Tuple[int, int]:
    """根据记录文件恢复移动的文件，返回（成功数，总数）"""
    if not os.path.exists(record_path):
        print(f"⚠️  记录文件不存在：{record_path}")
        return 0, 0
    
    try:
        with open(record_path, 'r', encoding='utf-8') as f:
            record_data = json.load(f)
        
        moved_files = record_data['moved_files']
        total_files = len(moved_files)
        success_count = 0
        
        print(f"🔄 正在恢复 {total_files} 个db3文件...")
        
        for dest_path, src_path in moved_files.items():
            try:
                # 检查目标文件是否存在（即移动后的位置）
                if os.path.exists(dest_path):
                    # 确保源目录存在
                    src_dir = os.path.dirname(src_path)
                    os.makedirs(src_dir, exist_ok=True)
                    
                    # 移动文件回原始位置
                    shutil.move(dest_path, src_path)
                    # 检查是否成功移回
                    if os.path.exists(src_path):
                        success_count += 1
                        print(f"   ✅ 已恢复：{os.path.basename(dest_path)} -> {src_path}")
                    else:
                        print(f"   ❌ 恢复失败：移动操作后源文件不存在 {src_path}")
                else:
                    print(f"   ⚠️  跳过：文件不存在于目标位置 {dest_path}")
            except Exception as e:
                print(f"   ❌ 恢复失败：{os.path.basename(dest_path)} - {str(e)}")
        
        # 删除记录文件
        os.remove(record_path)
        print(f"\n✅ 文件恢复完成：成功 {success_count}/{total_files}")
        
        return success_count, total_files
        
    except Exception as e:
        print(f"❌ 读取记录文件失败：{str(e)}")
        return 0, 0


def cleanup_move_records():
    """清理所有移动记录文件"""
    if os.path.exists(MOVE_RECORD_DIR):
        try:
            shutil.rmtree(MOVE_RECORD_DIR)
            print(f"🗑️  已清理移动记录目录：{MOVE_RECORD_DIR}")
        except Exception as e:
            print(f"⚠️  清理移动记录目录失败：{str(e)}")


def find_undistorted_folder(preprocess_out_dir: str) -> Optional[str]:
    """在预处理输出目录下查找 undistorted 文件夹"""
    for root, dirs, files in os.walk(preprocess_out_dir):
        if "undistorted" in dirs:
            return os.path.join(root, "undistorted")
    return None


def run_check_and_compress(
    undistorted_path: str,
    compress_output_dir: str,
    period_idx: int,
    start_time: str,
    end_time: str
) -> str:
    """调用外部检查压缩脚本，执行压缩流程，返回压缩包路径"""
    # 修改文件名格式：YYYYMMDD_HHMMSS-HHMMSS.zip
    current_date = datetime.now().strftime('%Y%m%d')
    compress_filename = f"{current_date}_{start_time}-{end_time}.{COMPRESS_FORMAT}"
    compress_path = os.path.join(compress_output_dir, compress_filename)
    
    check_compress_cmd = (
        f"{sys.executable} {CHECK_COMPRESS_SCRIPT_PATH} "
        f"--undistorted-path {undistorted_path} "
        f"--compress-path {compress_path} "
        f"--compress-format {COMPRESS_FORMAT} "
        f"--period {start_time}_{end_time}"
    )
    
    run_shell_command(
        check_compress_cmd,
        f"第{period_idx}个时间段 - 步骤4/4：检查+压缩"
    )
    
    return compress_path


def delete_raw_undistorted(undistorted_path: str) -> None:
    """压缩完成后，删除原始 undistorted 目录"""
    if DELETE_RAW_UNDISTORTED and os.path.exists(undistorted_path):
        try:
            shutil.rmtree(undistorted_path)
            print(f"✅ 已删除原始 undistorted 目录：{undistorted_path}")
        except Exception as e:
            print(f"⚠️  删除原始 undistorted 目录失败：{str(e)}")


def cleanup_by_simple_json(preprocess_out_dir: str, period_idx: int) -> dict:
    """根据simple.json清理文件，返回清理信息"""
    start_time = time.time()
    print(f"\n{'='*60}")
    print(f"🧹 开始根据 simple.json 清理文件（时间段：{period_idx}）")
    print(f"{'='*60}")
    
    undistorted_path = find_undistorted_folder(preprocess_out_dir)
    if not undistorted_path:
        print(f"⚠️  未找到 undistorted 文件夹，跳过清理步骤")
        return {"status": "skipped", "reason": "undistorted folder not found", "duration_seconds": round(time.time() - start_time, 2)}
    
    json_path = os.path.join(undistorted_path, SIMPLE_JSON_NAME)
    if not os.path.exists(json_path):
        print(f"⚠️  未找到 {SIMPLE_JSON_NAME}，跳过清理步骤")
        return {"status": "skipped", "reason": "simple.json not found", "duration_seconds": round(time.time() - start_time, 2)}
    
    print(f"📁 undistorted 目录：{undistorted_path}")
    print(f"📄 找到 simple.json：{json_path}")
    
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        
        if not isinstance(json_data, list):
            print(f"⚠️  simple.json 格式错误：根元素必须是列表")
            return {"status": "failed", "reason": "invalid json format", "duration_seconds": round(time.time() - start_time, 2)}
        
        required_files = {}
        deleted_count = 0
        
        for item in json_data:
            for key, value in item.items():
                if (key.startswith("camera_") or key.startswith("iv_points_")) and value != "NOT_FOUND":
                    folder_name = key
                    if folder_name not in required_files:
                        required_files[folder_name] = set()
                    required_files[folder_name].add(value)
        
        if not required_files:
            print(f"⚠️  simple.json 中没有找到有效的字段，跳过清理")
            return {"status": "skipped", "reason": "no valid fields in json", "duration_seconds": round(time.time() - start_time, 2)}
        
        print(f"🔍 识别出 {len(required_files)} 个需要清理的文件夹")
        
        for folder_name, files_to_keep in required_files.items():
            folder_path = os.path.join(undistorted_path, folder_name)
            if not os.path.exists(folder_path):
                continue
            
            for root, dirs, filenames in os.walk(folder_path):
                for filename in filenames:
                    if filename.endswith('.npy'):
                        continue
                    
                    file_path = os.path.join(root, filename)
                    basename = os.path.basename(filename)
                    
                    should_delete = True
                    for required_file in files_to_keep:
                        if basename == required_file or basename in required_file or required_file in basename:
                            should_delete = False
                            break
                    
                    if should_delete:
                        try:
                            os.remove(file_path)
                            deleted_count += 1
                        except Exception:
                            pass
        
        print(f"\n✅ 清理完成！总共删除了 {deleted_count} 个文件")
        return {
            "status": "success",
            "folders_cleaned": len(required_files),
            "files_deleted": deleted_count,
            "duration_seconds": round(time.time() - start_time, 2)
        }
        
    except Exception as e:
        print(f"❌ 清理过程发生错误：{str(e)}")
        return {
            "status": "failed",
            "error": str(e),
            "duration_seconds": round(time.time() - start_time, 2)
        }


def process_single_period(
    period_idx: int,
    start_time: str,
    end_time: str,
    source_dir: str,
    output_root: str,
    logtime: str,
    vehicle: str,
    main_out: str
) -> dict:
    """处理单个时间段的全流程（筛选+预处理+清理+检查压缩）"""
    period_start_time = time.time()
    print(f"\n{'='*80}")
    print(f"📌 开始处理第 {period_idx}/{total_periods} 个时间段：{start_time} → {end_time}")
    print(f"📦 文件模式：{'移动' if MOVE_MODE else '复制'}")
    print(f"{'='*80}")
    
    # 初始化日志记录
    period_log = {
        "period_index": f"{period_idx}/{total_periods}",
        "start_time": start_time,
        "end_time": end_time,
        "start_timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "status": "processing",
        "steps": []
    }
    
    # 初始化
    filtered_folder = get_filtered_folder_path(output_root, start_time, end_time)
    preprocess_out_dir = os.path.join(main_out, f"{start_time}_{end_time}")
    move_record_path = os.path.join("move_records", f"move_record_{start_time}_{end_time}.json")
    
    try:
        # 1. 打印配置信息
        print(f"\n📥 源db3目录：{source_dir}")
        print(f"📤 筛选输出目录：{filtered_folder}")
        print(f"⚙️  预处理输出目录：{preprocess_out_dir}")
        print(f"🚗 车辆型号：{vehicle}")
        print(f"⏰ 日志时间戳：{logtime}")
        
        # 2. 更新筛选脚本的时间段
        modify_filter_script(start_time, end_time)
        
        # 3. 执行筛选db3文件（使用移动模式）
        print(f"\n🔧 开始筛选步骤...")
        
        # 创建移动记录文件路径
        if MOVE_MODE:
            move_record_path = os.path.join(tempfile.gettempdir(), f"move_{period_idx}_{start_time}_{end_time}.json")
        
        # 构建筛选命令
        filter_cmd = (
            f"{sys.executable} {FILTER_SCRIPT_PATH} "
            f"--source {source_dir} "
            f"--output {output_root} "
            f"--start {start_time} "
            f"--end {end_time}"
        )
        
        if MOVE_MODE:
            filter_cmd += f" --move --save-record {move_record_path}"
        
        filter_result = run_shell_command(filter_cmd, f"第{period_idx}个时间段 - 步骤1/4：筛选db3文件")
        period_log["steps"].append(filter_result)
        
        # 4. 检查筛选结果
        if not os.path.exists(filtered_folder):
            print(f"❌ 筛选失败：未生成目标文件夹 {filtered_folder}")
            print(f"   跳过当前时间段，继续处理下一个...")
            period_log["status"] = "failed"
            period_log["reason"] = "filter output folder not created"
            period_log["duration_seconds"] = round(time.time() - period_start_time, 2)
            period_log["end_timestamp"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            return period_log
        
        # 5. 执行预处理（这一步需要db3文件存在）
        print(f"\n⚙️  开始预处理步骤...")
        run_export_cmd = (
            f"{sys.executable} {RUN_EXPORT_SCRIPT_PATH} "
            f"--bag {filtered_folder} "
            f"--out {preprocess_out_dir} "
            f"--vehicle {vehicle} "
            f"--logtime {logtime}"
        )
        export_result = run_shell_command(run_export_cmd, f"第{period_idx}个时间段 - 步骤2/4：预处理")
        period_log["steps"].append(export_result)
        
        print(f"✅ 预处理完成，现在可以安全恢复db3文件...")
        
        print(f"\n第{period_idx}个时间段 - 步骤3/4：恢复与清理")
        
        # 6. 恢复db3文件（在预处理完成后）
        restore_start = time.time()
        if MOVE_MODE and move_record_path and os.path.exists(move_record_path):
            print(f"\n🔄 恢复db3文件到原始位置...")
            success_count, total_count = restore_moved_files(move_record_path)
            period_log["steps"].append({
                "step_name": "恢复db3文件",
                "status": "success" if success_count == total_count else "partial",
                "restored_files": success_count,
                "total_files": total_count,
                "duration_seconds": round(time.time() - restore_start, 2)
            })
            if success_count < total_count:
                print(f"⚠️  部分文件恢复失败，请检查源目录和目标目录")
        elif MOVE_MODE:
            print(f"⚠️  移动记录文件不存在，无法恢复db3文件")
            period_log["steps"].append({
                "step_name": "恢复db3文件",
                "status": "skipped",
                "reason": "no move record file",
                "duration_seconds": round(time.time() - restore_start, 2)
            })
        
        # 7. 清理临时筛选文件夹（只保留metadata.yaml）
        if os.path.exists(filtered_folder):
            try:
                # 只删除db3文件，保留metadata.yaml
                for filename in os.listdir(filtered_folder):
                    if filename.endswith('.db3'):
                        os.remove(os.path.join(filtered_folder, filename))
                
                # 如果文件夹为空，删除整个文件夹
                if len(os.listdir(filtered_folder)) == 0:
                    os.rmdir(filtered_folder)
                    print(f"🗑️  已清理临时文件夹：{filtered_folder}")
            except Exception as e:
                print(f"⚠️  清理临时文件夹失败：{str(e)}")
        
        # 8. 其他后续步骤
        if CLEAN_BY_SIMPLE_JSON:
            cleanup_result = cleanup_by_simple_json(preprocess_out_dir, period_idx)
            period_log["steps"].append({
                "step_name": "simple.json清理",
                **cleanup_result
            })
        
        # 9. 检查压缩流程
        compress_path = None
        if not SKIP_CHECK_COMPRESS:
            undistorted_path = find_undistorted_folder(preprocess_out_dir)
            if undistorted_path:
                compress_start = time.time()
                compress_path = run_check_and_compress(
                    undistorted_path=undistorted_path,
                    compress_output_dir=preprocess_out_dir,
                    period_idx=period_idx,
                    start_time=start_time,
                    end_time=end_time
                )
                period_log["steps"].append({
                    "step_name": "检查+压缩",
                    "status": "success" if compress_path and os.path.exists(compress_path) else "failed",
                    "compress_path": compress_path if compress_path else None,
                    "duration_seconds": round(time.time() - compress_start, 2)
                })
                delete_raw_undistorted(undistorted_path)
        
        # 10. 打印完成信息
        print(f"\n✅ 第 {period_idx} 个时间段处理完成！")
        print(f"   预处理结果：{preprocess_out_dir}")
        if MOVE_MODE:
            print(f"   db3文件：已移动并恢复")
        if compress_path and os.path.exists(compress_path):
            print(f"   压缩包：{compress_path}")
        
        # 记录成功完成
        period_log["status"] = "success"
        period_log["output_dir"] = preprocess_out_dir
        if compress_path:
            period_log["compress_path"] = compress_path
        period_log["duration_seconds"] = round(time.time() - period_start_time, 2)
        period_log["end_timestamp"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return period_log
        
    except Exception as e:
        print(f"\n❌ 第 {period_idx} 个时间段处理异常：{str(e)}")
        
        # 发生异常时也要尝试恢复文件
        if MOVE_MODE and move_record_path and os.path.exists(move_record_path):
            print(f"🔄 发生异常，尝试恢复db3文件...")
            restore_moved_files(move_record_path)
        
        # 清理临时文件
        if os.path.exists(filtered_folder):
            try:
                shutil.rmtree(filtered_folder)
                print(f"🗑️  已清理临时文件夹：{filtered_folder}")
            except:
                pass
        
        # 记录异常
        period_log["status"] = "failed"
        period_log["error"] = str(e)
        period_log["duration_seconds"] = round(time.time() - period_start_time, 2)
        period_log["end_timestamp"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return period_log


def main():
    global total_periods, SESSION_START_TIME
    SESSION_START_TIME = time.time()
    
    import argparse
    parser = argparse.ArgumentParser(description="ROS 2 Bag 批量时间筛选 + 预处理 + 检查压缩全流程脚本")
    parser.add_argument("--logtime", type=str, required=True, help="日志时间戳（如：20251124_111515，用于 run_export.py）")
    parser.add_argument("--vehicle", type=str, default=DEFAULT_VEHICLE, help=f"车辆型号（默认：{DEFAULT_VEHICLE}）")
    parser.add_argument("--main-out", type=str, default=DEFAULT_MAIN_OUT, help=f"预处理主输出目录（默认：{DEFAULT_MAIN_OUT}）")
    parser.add_argument("--yaml-path", type=str, default=TIME_PERIODS_YAML, help=f"时间段配置YAML文件路径（默认：{TIME_PERIODS_YAML}）")
    parser.add_argument("--skip-check-compress", action="store_true", help=f"跳过检查压缩流程（默认不跳过，优先级高于配置文件）")
    parser.add_argument("--skip-clean-json", action="store_true", help=f"跳过simple.json清理流程（默认不跳过）")
    parser.add_argument("--no-move", action="store_true", help=f"禁用移动模式，使用复制模式（默认使用移动模式）")
    parser.add_argument("--clean-records", action="store_true", help=f"清理所有移动记录文件")
    args = parser.parse_args()
    
    # 覆盖配置
    global MOVE_MODE, SKIP_CHECK_COMPRESS, CLEAN_BY_SIMPLE_JSON
    MOVE_MODE = not args.no_move
    if args.skip_check_compress:
        SKIP_CHECK_COMPRESS = True
    if args.skip_clean_json:
        CLEAN_BY_SIMPLE_JSON = False
    
    # 清理移动记录（如果指定）
    if args.clean_records:
        cleanup_move_records()
        return
    
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
    
    # 2. 读取 filter_by_time.py 的真实配置
    try:
        SOURCE_DIRECTORY, OUTPUT_ROOT_DIRECTORY = get_filter_script_config()
    except Exception as e:
        print(f"❌ 读取筛选脚本配置失败：{str(e)}")
        sys.exit(1)
    
    # 3. 检查基础路径
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
    
    # 4. 检查目录
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
    
    # 5. 创建主输出目录
    os.makedirs(args.main_out, exist_ok=True)
    
    # 6. 记录会话信息到日志
    PIPELINE_LOG["session_info"] = {
        "start_time": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "source_directory": SOURCE_DIRECTORY,
        "filter_output_root": OUTPUT_ROOT_DIRECTORY,
        "preprocess_output": args.main_out,
        "vehicle": args.vehicle,
        "logtime": args.logtime,
        "yaml_config": args.yaml_path,
        "total_periods": total_periods,
        "config": {
            "move_mode": MOVE_MODE,
            "move_record_dir": MOVE_RECORD_DIR if MOVE_MODE else None,
            "clean_by_simple_json": CLEAN_BY_SIMPLE_JSON,
            "skip_check_compress": SKIP_CHECK_COMPRESS,
            "compress_format": COMPRESS_FORMAT if not SKIP_CHECK_COMPRESS else None
        }
    }
    
    # 打印全局配置信息
    print("\n========================================")
    print("📋 全局配置信息")
    print("========================================")
    print(f"📥 源db3目录：{SOURCE_DIRECTORY}")
    print(f"📤 筛选输出根目录：{OUTPUT_ROOT_DIRECTORY}")
    print(f"⚙️  预处理主输出：{args.main_out}")
    print(f"🚗 车辆型号：{args.vehicle}")
    print(f"⏰ 日志时间戳：{args.logtime}")
    print(f"📄 YAML配置文件：{args.yaml_path}")
    print(f"📦 文件模式：{'移动' if MOVE_MODE else '复制'}")
    if MOVE_MODE:
        print(f"📝 移动记录目录：{MOVE_RECORD_DIR}")
    print(f"🧹 simple.json清理：{'启用' if CLEAN_BY_SIMPLE_JSON else '禁用'}")
    print(f"🗜️  检查压缩流程：{'启用' if not SKIP_CHECK_COMPRESS else '禁用'}")
    print("========================================\n")
    
    # 7. 批量处理每个时间段
    success_count = 0
    fail_count = 0
    
    for period_idx, (start_time, end_time) in enumerate(time_periods, 1):
        try:
            period_log = process_single_period(
                period_idx=period_idx,
                start_time=start_time,
                end_time=end_time,
                source_dir=SOURCE_DIRECTORY,
                output_root=OUTPUT_ROOT_DIRECTORY,
                logtime=args.logtime,
                vehicle=args.vehicle,
                main_out=args.main_out
            )
            PIPELINE_LOG["periods_processed"].append(period_log)
            if period_log["status"] == "success":
                success_count += 1
            else:
                fail_count += 1
        except Exception as e:
            print(f"\n❌ 第 {period_idx} 个时间段处理异常：{str(e)}")
            print(f"   跳过当前时间段，继续处理下一个...\n")
            fail_count += 1
            # 记录异常的时间段
            PIPELINE_LOG["periods_processed"].append({
                "period_index": f"{period_idx}/{total_periods}",
                "start_time": start_time,
                "end_time": end_time,
                "status": "exception",
                "error": str(e)
            })
            continue
    
    # 8. 记录汇总信息
    total_duration = time.time() - SESSION_START_TIME
    PIPELINE_LOG["summary"] = {
        "end_time": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "total_periods": total_periods,
        "successful_periods": success_count,
        "failed_periods": fail_count,
        "success_rate": f"{(success_count/total_periods*100):.2f}%" if total_periods > 0 else "0%",
        "total_duration_seconds": round(total_duration, 2),
        "total_duration_formatted": f"{int(total_duration//3600)}h {int((total_duration%3600)//60)}m {int(total_duration%60)}s",
        "average_time_per_period_seconds": round(total_duration / total_periods, 2) if total_periods > 0 else 0
    }
    
    # 输出总体统计结果
    print(f"\n{'='*80}")
    print("📊 批量处理完成！总体统计：")
    print(f"   总时间段数：{total_periods}")
    print(f"   成功处理：{success_count} 个")
    print(f"   失败/跳过：{fail_count} 个")
    print(f"   成功率：{PIPELINE_LOG['summary']['success_rate']}")
    print(f"   总耗时：{PIPELINE_LOG['summary']['total_duration_formatted']}")
    print(f"   平均耗时：{PIPELINE_LOG['summary']['average_time_per_period_seconds']:.2f}秒/时间段")
    print(f"📁 所有预处理结果均保存在：{args.main_out}")
    if MOVE_MODE:
        print(f"📦 使用移动模式：db3文件已全部恢复原始位置")
    print(f"{'='*80}")
    
    # 保存日志
    save_pipeline_log(args.main_out)


if __name__ == "__main__":
    main()
