import os
import shutil
import re
import sys
import subprocess
import json
import argparse
from datetime import datetime, timedelta
from typing import Dict, List, Tuple

# ------------------- 默认配置 -------------------
# 保持原有配置，但会被命令行参数覆盖
DEFAULT_SOURCE_DIRECTORY = "/media/xl/MyPass/123/"
DEFAULT_OUTPUT_ROOT_DIRECTORY = "/media/xl/MyPass/123/out1"
DEFAULT_TARGET_START_TIME = "102145"  # 自动更新于 2025-12-05 14:40:34
DEFAULT_TARGET_END_TIME = "112245"    # 自动更新于 2025-12-05 14:40:34
# ----------------------------------------------

def copy_rosbag_files(source_dir: str, output_root_dir: str, start_time_str: str, end_time_str: str, move_mode: bool = False) -> Dict[str, str]:
    """
    转移指定时间段内的rosbag文件（db3），并通过ROS 2原生指令生成标准metadata.yaml
    """
    # 验证输入参数
    _validate_inputs(source_dir, output_root_dir, start_time_str, end_time_str)
    
    # 解析用户输入时间
    user_hh_start, user_mm_start, user_ss_start = _parse_time_str(start_time_str)
    user_hh_end, user_mm_end, user_ss_end = _parse_time_str(end_time_str)
    
    # 1. 查找并解析所有符合格式的db3文件
    all_db3_files = _find_and_parse_db3_files(source_dir)
    if not all_db3_files:
        raise FileNotFoundError(f"源文件夹 {source_dir} 中未找到符合格式的db3文件")
    
    # 2. 匹配用户指定时间段的db3文件（时间范围交集）
    matching_db3_files = _match_db3_by_time(
        all_db3_files,
        user_hh_start, user_mm_start, user_ss_start,
        user_hh_end, user_mm_end, user_ss_end
    )
    if not matching_db3_files:
        print(f"未找到与时间段 {start_time_str} - {end_time_str} 有交集的db3文件")
        return {}
    
    # 3. 创建输出文件夹并转移db3文件
    output_dir = _create_output_dir(output_root_dir, start_time_str, end_time_str)
    moved_files = _transfer_db3_files(matching_db3_files, output_dir, move_mode)
    
    # 4. 调用ROS 2指令生成yaml（兼容版：重定向输出+格式清理）
    _generate_yaml_by_ros2_compatible(output_dir)
    
    operation = "移动" if move_mode else "复制"
    print(f"\n操作完成！共{operation} {len(matching_db3_files)} 个db3文件，并生成标准 metadata.yaml 到 {output_dir}")
    
    return moved_files


def _validate_inputs(source_dir: str, output_root_dir: str, start_time: str, end_time: str):
    """验证输入参数的合法性"""
    if not os.path.isdir(source_dir):
        raise NotADirectoryError(f"源文件夹不存在：{source_dir}")
    if not os.path.isdir(output_root_dir):
        raise NotADirectoryError(f"输出根文件夹不存在：{output_root_dir}")
    if not (len(start_time) == 6 and start_time.isdigit()):
        raise ValueError("起始时间格式错误，必须是6位数字（HHMMSS）")
    if not (len(end_time) == 6 and end_time.isdigit()):
        raise ValueError("结束时间格式错误，必须是6位数字（HHMMSS）")


def _parse_time_str(time_str: str) -> Tuple[int, int, int]:
    """将HHMMSS格式字符串解析为（时，分，秒）"""
    return int(time_str[:2]), int(time_str[2:4]), int(time_str[4:6])


def _find_and_parse_db3_files(source_dir: str) -> List[Dict]:
    """查找源文件夹中所有符合格式的db3文件，并解析基础信息"""
    db3_pattern = r"rosbag2_(\d{4}_\d{2}_\d{2})-(\d{2}_\d{2}_\d{2})_(\d+)\.db3"
    all_db3_files = []
    
    for filename in os.listdir(source_dir):
        match = re.match(db3_pattern, filename)
        if match:
            try:
                date_str = match.group(1)
                base_time_str = match.group(2)
                seq_num = int(match.group(3))
                
                # 计算实际开始时间
                base_hh, base_mm, base_ss = _parse_time_str(base_time_str.replace("_", ""))
                base_datetime = datetime.strptime(
                    f"{date_str} {base_hh:02d}:{base_mm:02d}:{base_ss:02d}",
                    "%Y_%m_%d %H:%M:%S"
                )
                actual_start = base_datetime + timedelta(minutes=seq_num)
                
                all_db3_files.append({
                    "filename": filename,
                    "date_str": date_str,
                    "seq_num": seq_num,
                    "actual_start": actual_start,
                    "path": os.path.join(source_dir, filename)
                })
            except Exception as e:
                print(f"警告：跳过格式异常的文件 {filename}，错误：{str(e)}")
                continue
    
    # 按实际开始时间排序
    return sorted(all_db3_files, key=lambda x: x["actual_start"])


def _match_db3_by_time(
    db3_files: List[Dict],
    user_hh_start: int, user_mm_start: int, user_ss_start: int,
    user_hh_end: int, user_mm_end: int, user_ss_end: int
) -> List[Dict]:
    """根据用户指定的时间段匹配db3文件（时间范围有交集即匹配）"""
    matching_files = []
    target_date = None
    
    for db3 in db3_files:
        # 构造用户时间段（与当前db3同日期）
        user_start = datetime(
            year=db3["actual_start"].year,
            month=db3["actual_start"].month,
            day=db3["actual_start"].day,
            hour=user_hh_start,
            minute=user_mm_start,
            second=user_ss_start
        )
        user_end = datetime(
            year=db3["actual_start"].year,
            month=db3["actual_start"].month,
            day=db3["actual_start"].day,
            hour=user_hh_end,
            minute=user_mm_end,
            second=user_ss_end
        )
        
        # 只匹配同一日期的文件
        if target_date is None:
            target_date = db3["date_str"]
        elif db3["date_str"] != target_date:
            continue
        
        # 计算db3的结束时间（正常1分钟，或下一包开始时间）
        db3_end = db3["actual_start"] + timedelta(minutes=1)
        next_idx = db3_files.index(db3) + 1
        if next_idx < len(db3_files) and db3_files[next_idx]["date_str"] == target_date:
            next_start = db3_files[next_idx]["actual_start"]
            if next_start < db3_end:
                db3_end = next_start
        
        # 时间范围交集判断
        if db3["actual_start"] < user_end and db3_end > user_start:
            matching_files.append(db3)
    
    return list({db["path"]: db for db in matching_files}.values())  # 去重


def _create_output_dir(output_root: str, start_time: str, end_time: str) -> str:
    """创建输出文件夹（命名为"开始时间-结束时间"）"""
    output_dir_name = f"{start_time}_{end_time}"
    output_dir = os.path.join(output_root, output_dir_name)
    os.makedirs(output_dir, exist_ok=True)
    print(f"输出文件夹已创建：{output_dir}")
    return output_dir


def _transfer_db3_files(db3_files: List[Dict], output_dir: str, move_mode: bool) -> Dict[str, str]:
    """
    转移db3文件到输出文件夹
    返回: 移动的文件映射 {目标路径: 原始路径}（仅在移动模式下有效）
    """
    moved_files = {}
    operation = "移动" if move_mode else "复制"
    
    print(f"\n{operation}db3文件：")
    for db3 in db3_files:
        dest_path = os.path.join(output_dir, db3["filename"])
        
        if move_mode:
            # 移动文件
            shutil.move(db3["path"], dest_path)
            moved_files[dest_path] = db3["path"]
            print(f"  - 已移动：{db3['filename']}（开始时间：{db3['actual_start'].strftime('%H:%M:%S')}）")
        else:
            # 复制文件
            shutil.copy2(db3["path"], dest_path)
            print(f"  - 已复制：{db3['filename']}（开始时间：{db3['actual_start'].strftime('%H:%M:%S')}）")
    
    return moved_files


def _generate_yaml_by_ros2_compatible(output_dir: str):
    """
    兼容所有ROS 2版本的yaml生成方式
    """
    yaml_filename = "metadata.yaml"
    yaml_path = os.path.join(output_dir, yaml_filename)
    bag_folder_path = output_dir
    
    print(f"\n正在通过ROS 2生成 {yaml_filename}...")
    try:
        result = subprocess.run(
            f"ros2 bag reindex {bag_folder_path} --storage sqlite3",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        
        # 验证文件是否生成
        if not os.path.exists(yaml_path) or os.path.getsize(yaml_path) == 0:
            raise RuntimeError(f"yaml文件生成失败，文件为空或不存在")
        
        # 清理yaml格式
        _clean_yaml_format(yaml_path)
        
        print(f"成功生成标准metadata.yaml：{yaml_path}")
    
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr.strip() or "未知错误"
        raise RuntimeError(f"ROS 2指令执行失败：{error_msg}")
    except Exception as e:
        raise RuntimeError(f"生成yaml时发生异常：{str(e)}")


def _clean_yaml_format(yaml_path: str):
    """清理yaml文件格式：去除开头非yaml内容"""
    with open(yaml_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    # 找到yaml起始行
    start_idx = 0
    for i, line in enumerate(lines):
        if line.strip().startswith("rosbag2_bagfile_information:"):
            start_idx = i
            break
    
    cleaned_lines = lines[start_idx:]
    with open(yaml_path, "w", encoding="utf-8") as f:
        f.writelines(cleaned_lines)
    
    with open(yaml_path, "r", encoding="utf-8") as f:
        first_line = f.readline().strip()
        if not first_line.startswith("rosbag2_bagfile_information:"):
            raise RuntimeError(f"yaml格式清理失败，文件开头不是标准结构：{first_line}")


def save_move_record(moved_files: Dict[str, str], record_path: str):
    """保存移动记录到JSON文件"""
    with open(record_path, 'w', encoding='utf-8') as f:
        json.dump(moved_files, f, indent=2, ensure_ascii=False)


def load_move_record(record_path: str) -> Dict[str, str]:
    """从JSON文件加载移动记录"""
    with open(record_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def main():
    """主函数，支持命令行参数和默认配置"""
    parser = argparse.ArgumentParser(description="筛选并转移指定时间段的db3文件")
    parser.add_argument("--move", action="store_true", help="使用移动模式（默认：复制模式）")
    parser.add_argument("--source", type=str, default=DEFAULT_SOURCE_DIRECTORY, 
                       help=f"源目录路径（默认：{DEFAULT_SOURCE_DIRECTORY}）")
    parser.add_argument("--output", type=str, default=DEFAULT_OUTPUT_ROOT_DIRECTORY, 
                       help=f"输出目录路径（默认：{DEFAULT_OUTPUT_ROOT_DIRECTORY}）")
    parser.add_argument("--start", type=str, default=DEFAULT_TARGET_START_TIME, 
                       help=f"开始时间（HHMMSS，默认：{DEFAULT_TARGET_START_TIME}）")
    parser.add_argument("--end", type=str, default=DEFAULT_TARGET_END_TIME, 
                       help=f"结束时间（HHMMSS，默认：{DEFAULT_TARGET_END_TIME}）")
    parser.add_argument("--save-record", type=str, help="保存移动记录的文件路径（仅在移动模式下有效）")
    
    args = parser.parse_args()
    
    # 执行转移操作
    try:
        moved_files = copy_rosbag_files(
            source_dir=args.source,
            output_root_dir=args.output,
            start_time_str=args.start,
            end_time_str=args.end,
            move_mode=args.move
        )
        
        # 保存移动记录（如果指定了保存路径且确实移动了文件）
        if args.move and moved_files and args.save_record:
            save_move_record(moved_files, args.save_record)
            print(f"📝 移动记录已保存到：{args.save_record}")
            
    except Exception as e:
        print(f"执行过程中出现错误：{str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()