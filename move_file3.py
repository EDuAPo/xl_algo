import os
import shutil
from typing import Optional, Tuple
from datetime import datetime

def parse_hms_input(hms_str: str) -> Optional[int]:
    """
    解析时分秒输入，转换为整数（HHMMSS格式）
    支持格式：144303、14:43:03、14-43-03、14.43.03
    返回：整数形式的HHMMSS（如144303），解析失败返回None
    """
    hms_str = hms_str.strip()
    for sep in [':', '-', '.']:
        hms_str = hms_str.replace(sep, '')
    
    if len(hms_str) != 6 or not hms_str.isdigit():
        return None
    
    hour = int(hms_str[:2])
    minute = int(hms_str[2:4])
    second = int(hms_str[4:6])
    if 0 <= hour < 24 and 0 <= minute < 60 and 0 <= second < 60:
        return int(hms_str)
    return None

def extract_file_datetime(filename: str) -> Optional[datetime]:
    """
    从文件名中提取完整时间（格式：YYYYMMDD_HHMMSS_xxx.xxx）
    返回：datetime对象（包含年月日时分秒），提取失败返回None
    """
    name_without_ext = os.path.splitext(filename)[0]
    parts = name_without_ext.split('_')
    if len(parts) >= 2:
        date_part = parts[0]
        time_part = parts[1]
        # 验证日期（8位数字）和时间（6位数字）格式
        if len(date_part) == 8 and date_part.isdigit() and len(time_part) == 6 and time_part.isdigit():
            try:
                return datetime.strptime(f"{date_part}_{time_part}", "%Y%m%d_%H%M%S")
            except:
                pass
    return None

def should_copy_file(filename: str, start_hms: int, end_hms: int) -> Tuple[bool, Optional[datetime]]:
    """
    判断文件是否需要复制，并返回文件的完整时间（用于命名最外层文件夹）
    返回：(是否复制, 文件完整时间)
    """
    # JSON文件直接复制，无完整时间返回None
    if filename.endswith(('.json','.npy')):
        return True, None
    
    # 提取文件完整时间和时分秒
    file_dt = extract_file_datetime(filename)
    if file_dt is None:
        return False, None
    
    file_hms = int(file_dt.strftime("%H%M%S"))
    # 判断时分秒是否在范围内（支持跨零点）
    if start_hms <= end_hms:
        should_copy = start_hms <= file_hms <= end_hms
    else:
        should_copy = file_hms >= start_hms or file_hms <= end_hms
    
    return should_copy, (file_dt if should_copy else None)

def copy_special_folder(src_folder: str, dest_folder: str):
    """完整复制 combined_scales 文件夹（包含所有子文件和子文件夹）"""
    if os.path.exists(dest_folder):
        shutil.rmtree(dest_folder)
    shutil.copytree(src_folder, dest_folder)
    print(f"✅ 已完整复制特殊文件夹：{src_folder} -> {dest_folder}")

def process_regular_folder(src_folder: str, dest_folder: str, start_hms: int, end_hms: int, file_dts: list):
    """
    处理普通文件夹：
    - 筛选时分秒范围内的文件，保持目录结构
    - 收集符合条件文件的完整时间（用于命名）
    """
    for root, dirs, files in os.walk(src_folder):
        rel_path = os.path.relpath(root, src_folder)
        current_dest = os.path.join(dest_folder, rel_path)
        os.makedirs(current_dest, exist_ok=True)
        
        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(current_dest, file)
            
            should_copy, file_dt = should_copy_file(file, start_hms, end_hms)
            if should_copy:
                shutil.copy2(src_file, dest_file)
                print(f"📄 复制文件：{src_file} -> {dest_file}")
                # 收集文件完整时间（去重）
                if file_dt and file_dt not in file_dts:
                    file_dts.append(file_dt)

def process_root_files(src_root: str, dest_root: str, start_hms: int, end_hms: int, file_dts: list):
    """处理大文件夹根目录下的文件，收集符合条件文件的完整时间"""
    for file in os.listdir(src_root):
        src_file = os.path.join(src_root, file)
        if os.path.isfile(src_file):
            should_copy, file_dt = should_copy_file(file, start_hms, end_hms)
            if should_copy:
                dest_file = os.path.join(dest_root, file)
                shutil.copy2(src_file, dest_file)
                print(f"📁 复制根目录文件：{src_file} -> {dest_file}")
                if file_dt and file_dt not in file_dts:
                    file_dts.append(file_dt)

def collect_all_matching_files(src_root: str, start_hms: int, end_hms: int) -> list:
    """预扫描所有符合条件的文件，收集它们的完整时间（用于确定最外层文件夹名称）"""
    file_dts = []
    print("🔍 正在预扫描文件以收集完整时间...")
    
    # 扫描根目录文件
    for file in os.listdir(src_root):
        file_path = os.path.join(src_root, file)
        if os.path.isfile(file_path):
            _, file_dt = should_copy_file(file, start_hms, end_hms)
            if file_dt and file_dt not in file_dts:
                file_dts.append(file_dt)
    
    # 扫描所有子文件夹
    for root, dirs, files in os.walk(src_root):
        # 跳过combined_scales文件夹（无需扫描，直接复制）
        if os.path.basename(root) == "combined_scales":
            continue
        for file in files:
            _, file_dt = should_copy_file(file, start_hms, end_hms)
            if file_dt and file_dt not in file_dts:
                file_dts.append(file_dt)
    
    return sorted(file_dts)

def main():
    # ===================== 配置参数（请根据实际需求修改）=====================
    SOURCE_ROOT = "/media/finnan/T7/1124/cmy/undistorted/"  # Linux源大文件夹路径
    DEST_BASE = "/media/finnan/T7/1124/cmy/zip/"      # Linux保存文件夹路径
    START_HMS_STR = "11:48:29"                     # 开始时分秒（支持：143000、14:30:00等）
    END_HMS_STR = "11:48:55"                       # 结束时分秒（格式同上）
    SPECIAL_FOLDER_NAME = "combined_scales"        # 特殊文件夹名称
    # =======================================================================

    # 解析时分秒输入
    start_hms = parse_hms_input(START_HMS_STR)
    end_hms = parse_hms_input(END_HMS_STR)
    
    if not start_hms or not end_hms:
        print(f"❌ 时分秒格式错误！支持格式：143000、14:30:00、14-30-03、14.30.03")
        return

    # 预扫描所有符合条件的文件，收集完整时间
    file_dts = collect_all_matching_files(SOURCE_ROOT, start_hms, end_hms)
    if not file_dts:
        print("⚠️  未找到符合条件的文件（按时分秒筛选）")
        return

    # 确定最外层文件夹名称（最早时间_最晚时间）
    earliest_dt = file_dts[0]
    latest_dt = file_dts[-1]
    start_full_str = earliest_dt.strftime("%Y%m%d_%H%M%S")
    end_full_str = latest_dt.strftime("%Y%m%d_%H%M%S")
    outer_folder_name = f"{start_full_str}_to_{end_full_str}"
    DEST_ROOT = os.path.join(DEST_BASE, outer_folder_name)
    os.makedirs(DEST_ROOT, exist_ok=True)

    # 格式化输出信息
    start_hms_display = f"{start_hms:06d}"
    start_hms_display = f"{start_hms_display[:2]}:{start_hms_display[2:4]}:{start_hms_display[4:6]}"
    end_hms_display = f"{end_hms:06d}"
    end_hms_display = f"{end_hms_display[:2]}:{end_hms_display[2:4]}:{end_hms_display[4:6]}"

    # 处理大文件夹根目录下的文件
    print("🔍 正在处理大文件夹根目录文件...")
    process_root_files(SOURCE_ROOT, DEST_ROOT, start_hms, end_hms, file_dts)

    # 遍历所有一级子文件夹
    for folder_name in os.listdir(SOURCE_ROOT):
        src_folder = os.path.join(SOURCE_ROOT, folder_name)
        if not os.path.isdir(src_folder):
            continue
        
        dest_folder = os.path.join(DEST_ROOT, folder_name)
        os.makedirs(dest_folder, exist_ok=True)
        print(f"\n📁 正在处理文件夹：{folder_name}")

        # 遍历当前文件夹下的内容
        for item_name in os.listdir(src_folder):
            item_path = os.path.join(src_folder, item_name)
            
            # 完整复制特殊文件夹
            if item_name == SPECIAL_FOLDER_NAME and os.path.isdir(item_path):
                dest_special = os.path.join(dest_folder, item_name)
                copy_special_folder(item_path, dest_special)
            
            # 处理普通文件夹（筛选文件）
            elif os.path.isdir(item_path):
                dest_regular = os.path.join(dest_folder, item_name)
                process_regular_folder(item_path, dest_regular, start_hms, end_hms, file_dts)
            
            # 处理一级子文件夹下的文件
            elif os.path.isfile(item_path):
                should_copy, _ = should_copy_file(item_name, start_hms, end_hms)
                if should_copy:
                    dest_file = os.path.join(dest_folder, item_name)
                    shutil.copy2(item_path, dest_file)
                    print(f"📄 复制一级子文件夹文件：{item_path} -> {dest_file}")

    print(f"\n🎉 所有文件处理完成！")
    print(f"📌 结果保存至：{DEST_ROOT}")
    print(f"📊 统计信息：")
    print(f"   - 符合条件的文件时间范围：{start_full_str} ~ {end_full_str}")
    print(f"   - 涉及日期数量：{len(set(dt.strftime('%Y%m%d') for dt in file_dts))} 天")

if __name__ == "__main__":
    main()
