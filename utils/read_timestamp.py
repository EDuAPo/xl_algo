import argparse
from datetime import datetime
import os
from pathlib import Path

import sys


import cv2
import gi
import numpy as np

from rosbags.highlevel import AnyReader
from rosbags.serde import deserialize_cdr


# ----------------------------------------------------------------------
# 辅助函数：根据 Connection 对象获取 Topic 名称
def get_topic_name(connection) -> str:
    """从 rosbags connection 对象中提取 topic 名称。"""
    # rosbags 的 connection 对象包含 topic 属性
    return connection.topic

# ----------------------------------------------------------------------

def get_all_bags(input_path):
    bag_root = os.path.abspath(input_path)
    bag_paths = []
    # 遍历子目录
    for entry in sorted(os.listdir(bag_root)):
        bag_path = os.path.join(bag_root, entry)
        if not os.path.isdir(bag_path):
            continue
        # 判断是否为有效 ROS2 bag 目录（含 metadata.yaml）
        meta_file = os.path.join(bag_path, "metadata.yaml")
        if not os.path.exists(meta_file):
            continue

        bag_paths.append(Path(bag_path))

    print(bag_paths)

    return bag_paths

# ... (文件的导入和函数定义保持不变)

# ----------------------------------------------------------------------
# 辅助函数：判断是否为 H.265 关键帧
# 参考: H.265 (HEVC) NAL Unit Type
def is_h265_key_frame(data: bytes) -> bool:
    """
    检查字节数据是否以 H.265 IDR/I 帧（关键帧）开头。

    Args:
        data: 包含 H.265 NAL 单元的字节数据。

    Returns:
        True 如果数据以关键帧 NAL 单元开头。
    """
    # 查找 NAL 单元的起始码 (0x00 0x00 0x01 或 0x00 0x00 0x00 0x01)
    
    # 查找第一个非零字节
    start_index = 0
    while start_index < len(data) and data[start_index] == 0:
        start_index += 1
        
    # 如果数据太短，无法判断
    if len(data) - start_index < 2:
        return False
        
    # 找到 NAL 单元的第一个字节 (NAL header)
    # NAL header 在 H.265 中是 2 个字节，但关键信息在第一个字节
    # NAL Type 在 NAL header 的第 1 到 6 位 (共 6 位)
    # 第一个字节 (byte_0) 的计算: (data[index] >> 1) & 0x3F
    
    # 简化：假设 NAL 单元紧跟在 Start Code 之后
    # 查找 0x01 后的字节
    nal_start = -1
    for i in range(len(data) - 3):
        if data[i] == 0 and data[i+1] == 0 and data[i+2] == 1:
            nal_start = i + 3
            break
        elif i < len(data) - 4 and data[i] == 0 and data[i+1] == 0 and data[i+2] == 0 and data[i+3] == 1:
            nal_start = i + 4
            break
            
    if nal_start == -1 or nal_start >= len(data):
        return False # 找不到有效的 NAL Start Code

    # NAL 单元类型 (nal_unit_type) 位于 NAL header 的第 1 到 6 位 (6 bits)
    # H.265 NAL Header 的第一个字节是 data[nal_start]
    nal_unit_type = (data[nal_start] >> 1) & 0x3F

    # 关键帧 NAL Unit Type 范围:
    # 16-23: Coded slice of a non-IDR picture (P/B 帧)
    # 19-21: Coded slice of an IDR picture (IDR 帧，**关键帧**)
    # 32: VPS, 33: SPS, 34: PPS, 39: SEI
    
    # 关键帧通常对应 IDR (Instantaneous Decoding Refresh) 帧
    # IDR NAL 单元类型是 19, 20, 21 (Coded slice of an IDR picture)
    return 19 <= nal_unit_type <= 21

# ----------------------------------------------------------------------



def main():
    parser = argparse.ArgumentParser(
        description="Decode H.265 data from multiple continuous ROS2 bags.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    

    # 你指定的要读取的 topic 列表
    target_topics = [
        # "/camera/cam_8M_wa_front",
        "/iv_points_front_mid"
    ]

    parser.add_argument("--bag", required=True, help="ROS2 bag 主目录，里面可以有多个 bag 子目录")
    args = parser.parse_args()

    bag_paths = get_all_bags(args.bag)
    # bag_paths = get_all_bags('/home/shucdong/workspace/dataset/test/lidar_bags')

    try:
        with AnyReader(bag_paths) as reader:
            for connection, timestamp, rawdata in reader.messages():
                topic_name = connection.topic
                if topic_name not in target_topics:
                    continue

                timestamp_sec = timestamp / 1e9
                dt = datetime.fromtimestamp(timestamp_sec)
                timestamp_str = dt.strftime("%Y%m%d_%H%M%S_%f")[:-3]  # 精确到毫秒

                # print(f'topic: {topic_name}, timestamp: {timestamp}, ms: {timestamp_str} rawdata size: {len(rawdata)} bytes')

                rawdata_msg = deserialize_cdr(rawdata, connection.msgtype)

                # --- 新增的关键帧判断逻辑 ---
                is_key_frame = False

                # 仅对 Image Topic 进行 H.265 检查
                if topic_name == "/camera/cam_8M_wa_front":
                # if topic_name == "/camera/cam_8M_wa_front":
                    # 假设 H.265 字节数据位于 rawdata_msg 的 data 字段中
                    # if hasattr(rawdata_msg, 'data') and isinstance(rawdata_msg.data, (bytes, bytearray)):
                    if hasattr(rawdata_msg, 'data'):
                        is_key_frame = is_h265_key_frame(rawdata_msg.data)
                    else:
                         # 这里的 print 可以帮助调试，如果 H.265 数据不在 .data 字段中
                         # print(f"Warning: {topic_name} message does not have a standard 'data' field for H.265 bytes.")
                         pass 

                sec = rawdata_msg.header.stamp.sec
                nanosec = rawdata_msg.header.stamp.nanosec
                header_timestamp = sec + nanosec / 1e9
                header_dt = datetime.fromtimestamp(header_timestamp)
                header_timestamp_str = header_dt.strftime("%Y%m%d_%H%M%S_%f")[:-3] # 精确到毫秒


                key_frame_status = "🔑 KEY FRAME" if is_key_frame else " " # 非关键帧显示为空格

                print(f'topic: {topic_name}, msg_ms: {timestamp_str}, header_ms: {header_timestamp_str} {key_frame_status}')


                # print(f'topic: {topic_name}, header timestamp: {header_timestamp}, ms: {header_timestamp_str} rawdata size: {len(rawdata)} bytes')


    except Exception as e:
        print(f"\nAn error occurred: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
    finally:
        # 这个 'finally' 块只在所有bag文件都被处理完毕后才会执行
        print("\nFinished...")


if __name__ == "__main__":
    main()


