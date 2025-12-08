import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.transform import Rotation as R
import argparse
import sys

# ----------------------------------------------------------------------
# 配置
# ----------------------------------------------------------------------
# 欧拉角旋转顺序：Z (Yaw) -> Y (Pitch) -> X (Roll)。与您之前确认的顺序一致。
ROTATION_ORDER = 'zyx'  
TIME_FIELD = 'timestamp_nanosec' # 用于X轴的时间戳字段
QUAT_FIELDS = ['quaternion_x', 'quaternion_y', 'quaternion_z', 'quaternion_w']
# ----------------------------------------------------------------------

def quaternion_to_euler_plotter(file_path: str, order: str):
    """
    读取 JSON 文件中的四元数，转换为欧拉角（弧度），并将其可视化。

    Args:
        file_path (str): 输入 JSON 文件的路径。
        order (str): SciPy Rotation 模块中的欧拉角顺序 (例如 'zyx')。
    """
    print(f"--- 🚀 开始处理文件：{file_path} ---")

    try:
        # 1. 读取数据
        with open(file_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"❌ 错误：文件未找到 at {file_path}")
        return
    except json.JSONDecodeError:
        print("❌ 错误：JSON 文件解码失败，请检查文件格式。")
        return
    
    if not isinstance(data, list) or not data:
        print("⚠️ 警告：JSON 文件内容格式不正确或为空。期望是包含多个数据点的列表。")
        return

    print(f"✅ 成功读取 {len(data)} 个数据点。")
    
    timestamps = []
    quaternions = []

    for entry in data:
        # 提取时间戳（转换为秒，便于绘图）
        timestamp_ns = entry.get(TIME_FIELD)
        if timestamp_ns is not None:
            # 转换为秒
            timestamps.append(timestamp_ns / 1e9) 
        else:
             # 如果没有时间戳，使用索引作为替代
            timestamps.append(len(timestamps)) 

        # 提取四元数：SciPy 需要 (x, y, z, w) 顺序
        try:
            quat = [entry[QUAT_FIELDS[0]], entry[QUAT_FIELDS[1]], entry[QUAT_FIELDS[2]], entry[QUAT_FIELDS[3]]]
            quaternions.append(quat)
        except KeyError as e:
            print(f"❌ 错误：缺少四元数字段 {e}。请检查字段名称是否正确: {QUAT_FIELDS}")
            return

    # 将列表转换为 NumPy 数组
    timestamps = np.array(timestamps)
    quaternions = np.array(quaternions)
    
    if len(timestamps) == 0:
        print("⚠️ 警告：没有有效的数据可以处理。")
        return

    # 归一化时间戳，从第一个时间点开始
    start_time = timestamps[0]
    relative_times = timestamps - start_time

    # 2. 四元数到欧拉角转换
    print(f"🔄 正在将四元数转换为欧拉角 (基于 {order.upper()} 顺序)...")
    
    try:
        # SciPy 的 Rotation 类处理四元数 (x, y, z, w)
        rotations = R.from_quat(quaternions)
        # 转换为欧拉角，单位为度
        # order='zyx' 对应 [Yaw, Pitch, Roll]
        euler_deg = rotations.as_euler(order, degrees=True)
    except Exception as e:
        print(f"❌ 错误：四元数转换失败。请确保四元数数据有效 (例如，没有 NaN 或非单位向量): {e}")
        return

    # 分离欧拉角
    # euler_deg[:, 0] -> Z 轴旋转 (Yaw/Azimuth)
    # euler_deg[:, 1] -> Y 轴旋转 (Pitch)
    # euler_deg[:, 2] -> X 轴旋转 (Roll)
    yaw = euler_deg[:, 0]
    pitch = euler_deg[:, 1]
    roll = euler_deg[:, 2]

    # 3. 可视化
    print("📈 正在生成可视化图表...")

    plt.figure(figsize=(15, 8))

    # Roll 
    plt.subplot(3, 1, 1)
    plt.plot(relative_times, roll, label='Roll (X-axis Rotation)', color='r')
    plt.title(f'Roll (X-axis)')
    plt.ylabel('Angle (Degrees)')
    plt.grid(True)
    
    # Pitch
    plt.subplot(3, 1, 2)
    plt.plot(relative_times, pitch, label='Pitch (Y-axis Rotation)', color='g')
    plt.title(f'Pitch (Y-axis)')
    plt.ylabel('Angle (Degrees)')
    plt.grid(True)

    # Yaw/Azimuth
    plt.subplot(3, 1, 3)
    plt.plot(relative_times, yaw, label='Yaw (Z-axis Rotation/Azimuth)', color='b')
    plt.title(f'Yaw / Azimuth (Z-axis)')
    plt.xlabel(f'Time (Seconds, relative to start time)')
    plt.ylabel('Angle (Degrees)')
    plt.grid(True)

    plt.suptitle(f'四元数转换的欧拉角时间序列 (基于 {order.upper()} 旋转顺序)', fontsize=16, y=1.02)
    plt.tight_layout(rect=[0, 0.03, 1, 0.98])
    plt.show()

    print("--- ✅ 脚本执行完毕，图表已显示。 ---")
    print("\n* 提示: 欧拉角固有问题（如万向锁和周期性）可能导致 ±180° 或 ±90° 附近的跳变，这是正常的。")
    print(f"* 转换顺序: Yaw={order[0].upper()}, Pitch={order[1].upper()}, Roll={order[2].upper()}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="读取 JSON 文件中的四元数，转换为欧拉角（Z-Y-X 顺序），并可视化。")
    # 添加一个必需的位置参数来指定文件路径
    parser.add_argument("file_path", type=str, 
                        help="INS数据JSON文件的路径，例如: ins.json 或 /path/to/ins.json")
    
    args = parser.parse_args()

    # 调用主功能函数
    quaternion_to_euler_plotter(args.file_path, ROTATION_ORDER)