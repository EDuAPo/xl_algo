import numpy as np
from scipy.spatial.transform import Rotation as R
import argparse
import sys

# --- 转换函数 (已包含打印输出和万向锁警告) ---

def euler_to_quaternion(roll_deg, pitch_deg, yaw_deg, sequence='zyx'):
    """
    将欧拉角 (Roll, Pitch, Yaw) 转换为四元数 (x, y, z, w)。
    
    参数:
        roll_deg (float): 绕X轴的旋转角度 (度)。
        pitch_deg (float): 绕Y轴的旋转角度 (度)。
        yaw_deg (float): 绕Z轴的旋转角度 (度)。
        sequence (str): 欧拉角旋转顺序 (例如 'zyx', 'xyz' 等)。
        
    返回:
        numpy.ndarray: 包含 [x, y, z, w] 的四元数数组。
    """
    # --- 万向锁检查 ---
    if abs(pitch_deg) >= 89.99 and abs(pitch_deg) <= 90.01:
        print(f"\n⚠️ 警告：Pitch ({pitch_deg:.4f}度) 接近 90度，已触发万向锁 (Gimbal Lock)。")
        print(f"   此时 Roll 和 Yaw 的组合旋转存在无限解，不同的 Roll/Yaw 组合可能表示相同的姿态，导致相同的四元数。")
        
    # 将度转换为弧度
    roll_rad = np.deg2rad(roll_deg)
    pitch_rad = np.deg2rad(pitch_deg)
    yaw_rad = np.deg2rad(yaw_deg)

    # 1. 创建角度映射 (Key: 轴, Value: 弧度值)
    angle_map = {
        'x': roll_rad,
        'y': pitch_rad,
        'z': yaw_rad
    }

    # 2. 根据 sequence 动态构建 SciPy 所需的 euler_input 列表
    # SciPy 期望的输入顺序是 [对应 sequence 第一个轴的角度, 第二个轴的角度, 第三个轴的角度]
    try:
        euler_input = [angle_map[axis] for axis in sequence]
    except KeyError:
        print(f"❌ 错误: 欧拉角序列 '{sequence}' 包含无效轴字符 (必须是 'x', 'y', 'z')。", file=sys.stderr)
        sys.exit(1)
        
    # 创建旋转对象
    r = R.from_euler(sequence, euler_input)

    # 转换为四元数 [x, y, z, w] 格式
    quaternion = r.as_quat()

    # --- 打印转换结果 ---
    print(f"\n==============================================")
    print(f"✅ 欧拉角 -> 四元数 转换结果:")
    print(f"   输入欧拉角 (度): Roll={roll_deg:.4f}, Pitch={pitch_deg:.4f}, Yaw={yaw_deg:.4f}")
    print(f"   欧拉角旋转顺序: {sequence}")
    print(f"   SciPy输入角度顺序: {[np.rad2deg(a) for a in euler_input]}")
    print(f"   输出四元数 [x, y, z, w]: {quaternion[0]:.6f}, {quaternion[1]:.6f}, {quaternion[2]:.6f}, {quaternion[3]:.6f}")
    print(f"==============================================")
    
    return quaternion

def quaternion_to_euler(x, y, z, w, sequence='zyx'):
    """
    将四元数 (x, y, z, w) 转换为欧拉角 (Roll, Pitch, Yaw)。
    
    参数:
        x, y, z, w (float): 四元数分量。
        sequence (str): 欧拉角旋转顺序 (例如 'zyx', 'xyz' 等)。
        
    返回:
        numpy.ndarray: 包含 [Roll, Pitch, Yaw] (度) 的欧拉角数组。
    """
    # 创建一个旋转对象，输入为四元数 [x, y, z, w]
    r = R.from_quat([x, y, z, w])

    # 转换为欧拉角 (弧度)，输出顺序对应于 sequence
    euler_rad = r.as_euler(sequence)

    # 将弧度转换为度
    euler_deg = np.rad2deg(euler_rad)

    # 提取 Roll, Pitch, Yaw (为了便于用户理解，重新命名)
    roll_deg, pitch_deg, yaw_deg = np.nan, np.nan, np.nan
    
    try:
        # 1. 确定 SciPy 输出的轴顺序
        output_axes = list(sequence)
        
        # 2. 找到 R, P, Y 对应的索引
        r_idx = output_axes.index('x') if 'x' in output_axes else -1
        p_idx = output_axes.index('y') if 'y' in output_axes else -1
        y_idx = output_axes.index('z') if 'z' in output_axes else -1
        
        # 3. 赋值 (如果轴在 sequence 中)
        if r_idx != -1: roll_deg = euler_deg[r_idx]
        if p_idx != -1: pitch_deg = euler_deg[p_idx]
        if y_idx != -1: yaw_deg = euler_deg[y_idx]

    except ValueError:
        # 如果 sequence 不是有效的 x,y,z 组合，但 SciPy 接受了 (例如 'xyy' 是不行的)
        print(f"⚠️ 注意: 欧拉角输出顺序为 SciPy 的'{sequence}'顺序: {euler_deg}", file=sys.stderr)
        
    # --- 打印转换结果 ---
    print(f"\n==============================================")
    print(f"✅ 四元数 -> 欧拉角 转换结果:")
    print(f"   输入四元数 [x, y, z, w]: [{x:.6f}, {y:.6f}, {z:.6f}, {w:.6f}]")
    print(f"   目标欧拉角顺序: {sequence}")
    print(f"   SciPy输出角度顺序 (对应 {sequence} 轴): {euler_deg}")
    print(f"   输出欧拉角 (度, 对应Roll/X, Pitch/Y, Yaw/Z): Roll={roll_deg:.4f}, Pitch={pitch_deg:.4f}, Yaw={yaw_deg:.4f}")
    print(f"==============================================")

    # 返回 [Roll_deg, Pitch_deg, Yaw_deg] 数组 (为了保持一致性)
    return np.array([roll_deg, pitch_deg, yaw_deg]) 

# --- 主函数和命令行解析 (保持不变) ---

def main():
    """
    使用命令行参数解析，调用相应的转换函数。
    """
    # 创建解析器
    parser = argparse.ArgumentParser(
        description="欧拉角和四元数相互转换脚本。需要安装 numpy 和 scipy。",
        formatter_class=argparse.RawTextHelpFormatter
    )

    # 定义转换类型参数
    parser.add_argument(
        '--type',
        choices=['e2q', 'q2e'],
        required=True,
        help="转换类型: \n'e2q' (Euler to Quaternion) - 欧拉角转四元数\n'q2e' (Quaternion to Euler) - 四元数转欧拉角"
    )
    
    # 可选参数：欧拉角旋转顺序
    parser.add_argument(
        '--sequence',
        default='zyx',
        help="欧拉角旋转顺序 (例如 'zyx', 'xyz' 等)。默认 'zyx' (Yaw-Pitch-Roll)。"
    )

    # 定义输入参数组
    group = parser.add_argument_group('输入参数 (根据 --type 选择对应输入)')
    
    # 欧拉角输入 (Roll Pitch Yaw)
    group.add_argument(
        '--rpy',
        nargs=3,
        type=float,
        metavar=('ROLL', 'PITCH', 'YAW'),
        help="欧拉角输入 (度): ROLL (绕X), PITCH (绕Y), YAW (绕Z)。"
    )

    # 四元数输入 (X Y Z W)
    group.add_argument(
        '--xyzw',
        nargs=4,
        type=float,
        metavar=('X', 'Y', 'Z', 'W'),
        help="四元数输入: X, Y, Z, W。"
    )

    # 解析参数
    args = parser.parse_args()

    # --- 调用转换逻辑 ---

    try:
        if args.type == 'e2q':
            if args.rpy is None or args.xyzw is not None:
                parser.error("--type 'e2q' 需要 --rpy 参数 (ROLL PITCH YAW)，且不能提供 --xyzw。")
            
            roll, pitch, yaw = args.rpy
            # 这里的 Roll, Pitch, Yaw 是根据命令行参数的约定 (R, P, Y) 传递给函数的
            euler_to_quaternion(roll, pitch, yaw, sequence=args.sequence)

        elif args.type == 'q2e':
            if args.xyzw is None or args.rpy is not None:
                parser.error("--type 'q2e' 需要 --xyzw 参数 (X Y Z W)，且不能提供 --rpy。")

            x, y, z, w = args.xyzw
            quaternion_to_euler(x, y, z, w, sequence=args.sequence)
            
    except Exception as e:
        print(f"\n❌ 运行时发生错误: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    # 确保依赖库已安装
    try:
        import numpy as np
        from scipy.spatial.transform import Rotation as R
    except ImportError:
        print("\n❌ 错误: 需要安装 'numpy' 和 'scipy' 库。")
        print("   请运行: pip install numpy scipy")
        sys.exit(1)
        
    main()