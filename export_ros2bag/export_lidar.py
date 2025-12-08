#!/usr/bin/env python3

from datetime import datetime
import os
import argparse
import numpy as np
from tqdm import tqdm
import rosbag2_py
from sensor_msgs.msg import PointCloud2, PointField
from sensor_msgs_py import point_cloud2 
import struct
from tqdm import tqdm
import shutil
import threading
import queue

# --- 兼容不同 ROS2 版本的反序列化接口 ---
try:
    from rosidl_runtime_py.utilities import get_message, deserialize_message
except ImportError:
    # 某些老版本可能需要这样导入
    from rosidl_runtime_py.utilities import get_message
    from rclpy.serialization import deserialize_message

# 线程通信用的 Stop 标志
STOP_SIGNAL = "STOP"

# ROS PointField 数据类型到 NumPy dtype 的映射
TYPE_MAP = {
    PointField.INT8: np.dtype('int8'),
    PointField.UINT8: np.dtype('uint8'),
    PointField.INT16: np.dtype('int16'),
    PointField.UINT16: np.dtype('uint16'),
    PointField.INT32: np.dtype('int32'),
    PointField.UINT32: np.dtype('uint32'),
    PointField.FLOAT32: np.dtype('float32'),
    PointField.FLOAT64: np.dtype('float64'),
}

# --- 【最终优化】直接从消息字节缓冲区读取点云数据 ---
def read_points_from_buffer(msg: PointCloud2) -> np.ndarray:
    """
    通过 np.frombuffer 直接读取 PointCloud2 的原始字节数据，
    绕过 sensor_msgs_py 的低效 Python 循环。
    """
    if not msg.fields:
        return np.empty((0,))

    # 1. 动态构建 NumPy 结构化数组的 dtype
    dtype_list = []
    current_offset = 0
    
    for field in msg.fields:
        # 1.1 处理字节对齐/Padding
        if field.offset > current_offset:
            padding_size = field.offset - current_offset
            # 插入 padding 字段
            dtype_list.append((f'_pad_{current_offset}', np.dtype('uint8'), padding_size))
            current_offset += padding_size
            
        # 1.2 获取 NumPy 类型
        np_type = TYPE_MAP.get(field.datatype)
        if np_type is None:
             raise ValueError(f"Unsupported PointField datatype: {field.datatype}")
             
        # 1.3 添加字段
        # PointField.count 允许一个字段有多个元素，但通常 LiDAR 为 1
        if field.count > 1:
             dtype_list.append((field.name, np_type, field.count))
        else:
             dtype_list.append((field.name, np_type))
        
        current_offset += np_type.itemsize * field.count

    # 2. 确保 PointStep 的完整性（可能存在尾部 padding）
    if msg.point_step > current_offset:
        padding_size = msg.point_step - current_offset
        print(f"⚠️ 注意: 在字段末尾添加 padding 大小 {padding_size} 字节以匹配 point_step {msg.point_step}")
        dtype_list.append((f'_pad_end', np.dtype('uint8'), padding_size))

    # 3. 创建最终 dtype
    point_dtype = np.dtype(dtype_list)

    # 4. 使用 np.frombuffer 创建结构化数组视图
    num_points = int(len(msg.data) / msg.point_step)
    cloud_arr = np.frombuffer(
        msg.data, 
        dtype=point_dtype, 
        count=num_points
    )
    
    # 5. 处理字节序 (Endianness)
    if msg.is_bigendian:
        # 如果是大端序，需要字节交换
        cloud_arr = cloud_arr.byteswap().newbyteorder('<')

    return cloud_arr

# --- 辅助函数：PCD Header 生成 ---
def generate_pcd_header(num_points, fields, data_type):
    """生成 PCD 文件头 (ASCII 或 BINARY)"""
    # 这里的 fields 应该是 ['x', 'y', 'z', ...] (不含 padding)
    header = [
        "# .PCD v0.7 - Point Cloud Data file format",
        "VERSION 0.7",
        f"FIELDS {' '.join(fields)}",
        # 假设所有导出的字段都是 float32 (4字节)
        f"SIZE {' '.join(['4' for _ in fields])}",
        f"TYPE {' '.join(['F' for _ in fields])}",
        f"COUNT {' '.join(['1' for _ in fields])}",
        f"WIDTH {num_points}",
        "HEIGHT 1",
        "VIEWPOINT 0 0 0 1 0 0 0",
        f"POINTS {num_points}",
        f"DATA {data_type}"
    ]
    return '\n'.join(header) + '\n'

# --- 辅助函数：将结构化数组转换为连续 float32 数组 ---
def struct_to_contiguous_float32(points, fields):
    """
    将结构化数组（包含 padding）转换为连续的 (N, F) float32 数组。
    fields 参数必须是需要保存的字段列表 (不含 padding)。
    """
    # 这里的 fields 已经是需要保存的字段列表 (e.g., ['x', 'y', 'z', 'intensity'])
    valid_fields = fields 
    num_points = len(points)
    num_fields = len(valid_fields)
    
    if num_points == 0:
        return np.empty((0, num_fields), dtype=np.float32)

    # 预分配目标数组
    points_float32 = np.empty((num_points, num_fields), dtype=np.float32)

    # 逐列赋值，从结构化数组提取数据并转换类型
    for i, field_name in enumerate(valid_fields):
        # 提取字段数据并转换为 float32 赋值到新数组的列
        points_float32[:, i] = points[field_name].astype(np.float32) 
        
    return points_float32

# --- 辅助函数：保存 PCD (ASCII) ---
def save_pcd_ascii(filename, points, fields):
    """以 ASCII 方式保存 .pcd 文件 (points 是结构化数组)"""
    num_points = len(points)
    header = generate_pcd_header(num_points, fields, "ascii")
    
    # ASCII 格式必须使用 np.savetxt
    points_2d = np.column_stack([points[name] for name in fields])
    
    with open(filename, 'w') as f:
        f.write(header)
        np.savetxt(f, points_2d, fmt="%.6f")

# --- 辅助函数：保存 PCD (BINARY) ---
def save_pcd_binary(filename, points, fields):
    """以 BINARY 方式保存 .pcd 文件 (points 是结构化数组)"""
    num_points = len(points)
    if num_points == 0:
        return

    # 1. 生成文件头
    header = generate_pcd_header(num_points, fields, "binary")

    # 2. 【优化】转换为连续 float32 数组
    points_float32 = struct_to_contiguous_float32(points, fields)
        
    # 3. 写入文件
    with open(filename, 'wb') as f:
        f.write(header.encode('ascii'))
        f.write(points_float32.tobytes()) # 写入连续的字节数据


# --- 辅助函数：保存 BIN ---
def save_bin(filename, points, fields):
    """以二进制方式保存 .bin 文件 (points 是结构化数组)"""
    if not fields or len(points) == 0:
        return
        
    # 1. 【优化】转换为连续 float32 数组
    points_float32 = struct_to_contiguous_float32(points, fields)

    # 2. 将 NumPy 数组直接写入文件
    points_float32.tofile(filename)


# --- 辅助函数：统一保存接口 ---
def save_points(filename_base, points, fields, export_format):
    """根据指定的格式调用不同的保存函数"""
    if export_format == 'pcd_ascii':
        filename = f"{filename_base}.pcd"
        save_pcd_ascii(filename, points, fields)
    elif export_format == 'pcd_binary':
        filename = f"{filename_base}.pcd"
        save_pcd_binary(filename, points, fields)
    elif export_format == 'bin':
        filename = f"{filename_base}.bin"
        save_bin(filename, points, fields)
    else:
        raise ValueError(f"不支持的导出格式: {export_format}")


# --- 辅助函数：查找 PointCloud2 Topics (保持不变) ---
def list_pointcloud2_topics(bag_path):
    reader = rosbag2_py.SequentialReader()
    storage_options = rosbag2_py.StorageOptions(uri=bag_path, storage_id="sqlite3")
    converter_options = rosbag2_py.ConverterOptions("", "")
    reader.open(storage_options, converter_options)
    metadata = reader.get_metadata()
    topics = []
    topic_types = {}
    for t in metadata.topics_with_message_count:
        if "PointCloud2" in t.topic_metadata.type:
            topics.append(t.topic_metadata.name)
            topic_types[t.topic_metadata.name] = t.topic_metadata.type
            print(f"Topic: {t.topic_metadata.name}, type: {t.topic_metadata.type}, count: {t.message_count}")
    return topics, topic_types, metadata.topics_with_message_count

# --- 工作线程：处理单个 Topic 的消息并保存 ---
class TopicExporter(threading.Thread):
    def __init__(self, topic_name, msg_type, msg_queue, out_dir, total_msgs, export_format):
        super().__init__()
        self.topic_name = topic_name
        self.msg_type = msg_type
        self.msg_queue = msg_queue
        self.out_dir = out_dir
        self.total_msgs = total_msgs
        self.export_format = export_format # 格式参数
        self.msg_count = 0
        self.fields_printed = False
        
        # 性能监控
        self.start_time = datetime.now()
        self.last_check_time = datetime.now()
        self.last_check_count = 0
        self.time_stats = {'deserialize': [], 'read_points': [], 'format': [], 'save': []}
        
        # 根据格式参数设置子目录名 (pcd_ascii, pcd_binary, bin)
        format_dir = export_format.lower() 
        self.pcd_dir = os.path.join(out_dir, topic_name.strip("/").replace("/", "_"), format_dir)
        os.makedirs(self.pcd_dir, exist_ok=True)
        self.pbar = tqdm(total=total_msgs, desc=f"Saving {topic_name} to {export_format.upper()}", ncols=100)

    def run(self):
        while True:
            item = self.msg_queue.get()
            if item == STOP_SIGNAL:
                self.msg_queue.task_done()
                break

            # item 是 (data, timestamp)
            data, t = item
            self.process_message(data, t)
            self.msg_queue.task_done()
            self.pbar.update(1)

        self.pbar.close()
        
        # 计算最终统计
        total_time = (datetime.now() - self.start_time).total_seconds()
        avg_fps = self.msg_count / total_time if total_time > 0 else 0
        
        avg_stats = {k: sum(v)/len(v) if v else 0 for k, v in self.time_stats.items()}
        
        print(f"\n{'='*80}")
        print(f"🎉 Topic {self.topic_name} 导出完成")
        print(f"{'='*80}")
        print(f"  总帧数: {self.msg_count}")
        print(f"  保存至: {self.pcd_dir}")
        print(f"  总耗时: {total_time:.2f}秒")
        print(f"  平均速率: {avg_fps:.2f} fps")
        print(f"  各阶段平均耗时:")
        print(f"    - 反序列化: {avg_stats['deserialize']:.2f}ms")
        print(f"    - 读取点云: {avg_stats['read_points']:.2f}ms")
        print(f"    - 格式化: {avg_stats['format']:.2f}ms")
        print(f"    - 保存文件: {avg_stats['save']:.2f}ms")
        print(f"  每帧平均总耗时: {sum(avg_stats.values()):.2f}ms")
        print(f"{'='*80}")

    def process_message(self, data, t):
        start_time_total = datetime.now() # 开始总计时

        # 1. 反序列化
        start_time = datetime.now()
        msg = deserialize_message(data, self.msg_type)
        time_deserialize = (datetime.now() - start_time).total_seconds() * 1000 # ms

        # 2. 【最终优化】使用自定义的 np.frombuffer 逻辑
        start_time = datetime.now()
        cloud_arr = read_points_from_buffer(msg) 
        time_read_points = (datetime.now() - start_time).total_seconds() * 1000 # ms

        # 3. 数据处理
        start_time = datetime.now()
        # FIX: 正确提取需要保存的字段名列表
        field_names_to_save = [f.name for f in msg.fields]
        
        # cloud_arr 已经是包含 padding 的结构化数组，直接传递
        points_to_save = cloud_arr 
        time_format_data = (datetime.now() - start_time).total_seconds() * 1000 # ms

        # 4. 文件保存 (I/O)
        timestamp_sec = t / 1e9
        dt = datetime.fromtimestamp(timestamp_sec)
        timestamp_str = dt.strftime("%Y%m%d_%H%M%S_%f")[:-3]  # 精确到毫秒
        file_base = os.path.join(self.pcd_dir, f"{timestamp_str}") 

        start_time = datetime.now()
        # 调用统一保存接口，传入正确提取的字段名列表
        save_points(file_base, points_to_save, field_names_to_save, self.export_format) 
        time_save_file = (datetime.now() - start_time).total_seconds() * 1000 # ms
        
        # 5. 收集性能数据
        self.msg_count += 1
        self.time_stats['deserialize'].append(time_deserialize)
        self.time_stats['read_points'].append(time_read_points)
        self.time_stats['format'].append(time_format_data)
        self.time_stats['save'].append(time_save_file)
        
        # 6. 性能监控和变慢检测
        if self.msg_count % 200 == 0:  # 每200帧检查一次
            current_time = datetime.now()
            elapsed = (current_time - self.start_time).total_seconds()
            interval = (current_time - self.last_check_time).total_seconds()
            frames_in_interval = self.msg_count - self.last_check_count
            
            overall_fps = self.msg_count / elapsed if elapsed > 0 else 0
            interval_fps = frames_in_interval / interval if interval > 0 else 0
            
            # 计算最近200帧的平均耗时
            recent_stats = {k: sum(v[-200:])/len(v[-200:]) if v[-200:] else 0 for k, v in self.time_stats.items()}
            
            time_total = (datetime.now() - start_time_total).total_seconds() * 1000
            print(f"\n{'='*80}")
            print(f"📊 [{self.topic_name}] 性能检测 - 第 {self.msg_count} 帧")
            print(f"{'='*80}")
            print(f"  当前帧 ({len(points_to_save)} pts): {time_total:.2f}ms")
            print(f"  最近200帧平均:")
            print(f"    - 反序列化: {recent_stats['deserialize']:.2f}ms")
            print(f"    - 读取点云: {recent_stats['read_points']:.2f}ms")
            print(f"    - 格式化: {recent_stats['format']:.2f}ms")
            print(f"    - 保存文件: {recent_stats['save']:.2f}ms")
            print(f"    - 合计平均: {sum(recent_stats.values()):.2f}ms")
            print(f"  处理速率:")
            print(f"    - 总体速率: {overall_fps:.2f} fps")
            print(f"    - 当前区间: {interval_fps:.2f} fps")
            print(f"  总耗时: {elapsed:.1f}s")
            
            # 变慢警告
            if self.msg_count > 400 and interval_fps < overall_fps * 0.7:
                print(f"  ⚠️  警告: 处理速度下降 {((1 - interval_fps/overall_fps) * 100):.1f}%")
            
            print(f"{'='*80}")
            
            self.last_check_time = current_time
            self.last_check_count = self.msg_count


# --- 核心函数：统一读取并分发消息 (保持不变) ---
def export_one_bag(bag_path, out_dir, export_format):
    # 1. 识别 PointCloud2 Topics
    topics, topic_types_str, topics_meta = list_pointcloud2_topics(bag_path)
    if not topics:
        print("❌ 未检测到 PointCloud2 topics")
        return

    print("\n检测到以下 PointCloud2 topics:")
    for i, t in enumerate(topics):
        count = next(m.message_count for m in topics_meta if m.topic_metadata.name == t)
        print(f"  [{i}] {t} (Count: {count})")

    # 2. 初始化队列和工作线程
    topic_queues = {topic: queue.Queue(maxsize=100) for topic in topics}
    exporter_threads = []
    total_messages_to_export = 0

    for topic in topics:
        topic_msg_type_str = topic_types_str[topic]
        msg_type = get_message(topic_msg_type_str)
        
        # 获取消息总数
        topic_count = next(m.message_count for m in topics_meta if m.topic_metadata.name == topic)
        total_messages_to_export += topic_count

        thread = TopicExporter(
            topic_name=topic, 
            msg_type=msg_type, 
            msg_queue=topic_queues[topic], 
            out_dir=out_dir, 
            total_msgs=topic_count,
            export_format=export_format # 传递格式参数
        )
        exporter_threads.append(thread)
        thread.start()

    # 3. 配置 SequentialReader 并读取数据
    storage_options = rosbag2_py.StorageOptions(uri=bag_path, storage_id="sqlite3")
    converter_options = rosbag2_py.ConverterOptions("", "")
    
    # 使用 SequentialReader 进行一次遍历
    reader = rosbag2_py.SequentialReader()
    reader.open(storage_options, converter_options)
    
    # 设置 Topic 过滤器，只读取 PointCloud2 消息
    reader.set_filter(rosbag2_py.StorageFilter(topics))

    # 4. 主线程：读取并投递消息
    print("\n[INFO] 主线程开始读取数据并分发...")
    
    total_messages_read = 0
    total_read_time = 0.0
    
    with tqdm(total=total_messages_to_export, desc="Reading and Dispatching", ncols=100) as pbar_read:
        while reader.has_next():
            start_time = datetime.now()
            # (topic, data, t) 仍然是 SequenceReader 的返回格式
            (topic, data, t) = reader.read_next()
            read_time = (datetime.now() - start_time).total_seconds() * 1000 # ms
            total_read_time += read_time
            total_messages_read += 1
            
            if topic in topic_queues:
                topic_queues[topic].put((data, t)) 
                pbar_read.update(1)
            
            # 打印主线程读取耗时 (仅对前几帧或定期打印)
            if total_messages_read <= 5 or total_messages_read % 500 == 0:  # 优化：降低至每500帧
                 print(f"[LOG] Main Thread Read Frame {total_messages_read} | Read/Dispatch Time: {read_time:.2f}ms")

    # 5. 发送停止信号并等待所有线程完成
    avg_read_time = total_read_time / total_messages_read if total_messages_read > 0 else 0
    print(f"\n[INFO] 主线程读取完成，总读取消息 {total_messages_read} 帧。平均读取耗时: {avg_read_time:.2f}ms")
    for topic, q in topic_queues.items():
        q.put(STOP_SIGNAL)

    for thread in exporter_threads:
        thread.join()

    print(f"\n✅ Bag {bag_path} 所有 PointCloud2 Topics 导出完成！")

    
# --- Main 函数 (保持不变) ---
def main():
    parser = argparse.ArgumentParser(description="多线程导出多个 ROS2 bag 的 Lidar 数据")
    parser.add_argument("--bag", required=True, help="ROS2 bag 目录（可以是单个bag目录或包含多个bag子目录的根目录）")
    parser.add_argument("--out", required=True, help="输出根目录")
    parser.add_argument(
        "--format", 
        required=True, 
        choices=['pcd_ascii', 'pcd_binary', 'bin'], 
        help="导出格式: pcd_ascii, pcd_binary (PCD格式的ASCII/二进制), 或 bin (原始二进制 float32)"
    )
    args = parser.parse_args()

    bag_root = os.path.abspath(args.bag)
    out_root = os.path.abspath(args.out)
    export_format = args.format.lower()

    # 检查输入路径是否存在
    if not os.path.exists(bag_root):
        print(f"❌ 错误：输入路径不存在：{bag_root}")
        return

    # 判断输入路径本身是否是一个bag目录（包含metadata.yaml）
    meta_file = os.path.join(bag_root, "metadata.yaml")
    if os.path.exists(meta_file):
        # 单目录模式：直接处理这个目录
        print(f"✅ 输入路径是单个bag目录：{bag_root}")
        bag_paths = [bag_root]
    else:
        # 多目录模式：遍历子目录
        print(f"📁 按多目录模式处理：遍历 {bag_root} 的子目录")
        bag_paths = []
        
        try:
            entries = os.listdir(bag_root)
        except Exception as e:
            print(f"❌ 无法读取目录 {bag_root}: {e}")
            return
        
        if not entries:
            print(f"⚠️  目录为空：{bag_root}")
            return
        
        # 遍历子目录，查找bag目录
        bag_count = 0
        for entry in sorted(entries):
            bag_path = os.path.join(bag_root, entry)
            
            # 只处理目录
            if not os.path.isdir(bag_path):
                continue
            
            # 检查是否是有效的bag目录
            meta_file = os.path.join(bag_path, "metadata.yaml")
            if not os.path.exists(meta_file):
                # 不是bag目录，跳过
                continue
            
            bag_paths.append(bag_path)
            bag_count += 1
            print(f"  找到bag目录 {bag_count}: {entry}")
        
        if bag_count == 0:
            print(f"⚠️  警告：在 {bag_root} 中未找到有效的bag目录")
            print(f"   检查目录结构：应有子目录，每个子目录包含 metadata.yaml")
            return

    print(f"总计找到 {len(bag_paths)} 个bag目录")
    
    # 处理每个bag目录
    for bag_path in bag_paths:
        print(f"\n" + "="*80)
        print(f"[INFO] 开始导出 bag: {bag_path}")
        print(f"[INFO] 导出格式: {export_format.upper()}")
        print("="*80)

        # 为该 bag 创建独立输出路径
        # 使用bag目录的名称作为输出子目录名
        bag_out_dir = os.path.join(out_root)
        
        # 如果输出目录已存在，先删除（保持与原始逻辑一致）
        # if os.path.exists(bag_out_dir):
        #     print(f"⚠️  输出目录已存在，删除：{bag_out_dir}")
        #     shutil.rmtree(bag_out_dir)
        
        os.makedirs(bag_out_dir, exist_ok=True)

        # 调用导出函数
        export_one_bag(bag_path, bag_out_dir, export_format)

    print("\n" + "="*80)
    print("✅ 所有 bag 导出完成！")
    print("="*80)

if __name__ == "__main__":
    main()