#!/usr/bin/env python3
import argparse
import rosbag2_py
from rclpy.serialization import deserialize_message
from rosidl_runtime_py.utilities import get_message

def analyze_one_image(bag_path, topic_name):
    # 打开 rosbag2
    reader = rosbag2_py.SequentialReader()
    storage_options = rosbag2_py.StorageOptions(uri=bag_path, storage_id="sqlite3")
    converter_options = rosbag2_py.ConverterOptions("", "")
    reader.open(storage_options, converter_options)
    reader.set_filter(rosbag2_py.StorageFilter([topic_name]))

    topic_types = {topic_name: 'sensor_msgs/msg/Image'}

    # 读取第一帧
    if reader.has_next():
        topic, data, t = reader.read_next()
        msg_type = get_message(topic_types[topic])
        msg = deserialize_message(data, msg_type)

        print("反序列化后的 msg 类型:", type(msg))
        print("字段信息:")
        for field_name in msg.__slots__:
            value = getattr(msg, field_name)
            print(f"  {field_name}: type={type(value)}, value preview={value if isinstance(value, (int, float, str)) else str(type(value))}")

        # 特别打印 data 字段长度
        print(f"\n注意: data 字段长度 = {len(msg.data)} 字节")

    else:
        print(f"{topic_name} 没有数据！")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze one Image message in ROS2 bag")
    parser.add_argument("--bag", required=True, help="Path to rosbag2 folder")
    parser.add_argument("--topic", required=True, help="Image topic to analyze")
    args = parser.parse_args()

    analyze_one_image(args.bag, args.topic)
