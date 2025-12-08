from rosbag2_py import SequentialReader, StorageOptions, ConverterOptions
from rclpy.serialization import deserialize_message
from rosidl_runtime_py.utilities import get_message

bag_path = "/home/shucdong/workspace/dataset/test/lidar_bags/split_bag_041_20251104_160012/"
topic_name = "/iv_points_front_mid"

# 打开 rosbag
storage_options = StorageOptions(uri=bag_path, storage_id="sqlite3")
converter_options = ConverterOptions(input_serialization_format="cdr", output_serialization_format="cdr")
reader = SequentialReader()
reader.open(storage_options, converter_options)

PointCloud2 = get_message("sensor_msgs/msg/PointCloud2")

# 读取第一帧
while reader.has_next():
    topic, data, t = reader.read_next()
    if topic != topic_name:
        continue
    msg = deserialize_message(data, PointCloud2)

    print("Fields in PointCloud2:")
    for f in msg.fields:
        print(f"  name: {f.name}, datatype: {f.datatype}, offset: {f.offset}, count: {f.count}")
    break
