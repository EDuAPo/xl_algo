import numpy as np
from scipy.spatial.transform import Rotation as R
import argparse
import sys

# --- 辅助函数：格式化和打印矩阵 ---
def print_matrix(M, title="矩阵"):
    """ 打印 3x3 旋转矩阵或 4x4 齐次变换矩阵 """
    print(f"\n--- {title} ---")
    rows, cols = M.shape
    
    # 构建格式化字符串，确保对齐
    format_str = "[[" + ", ".join([f"{{:.6f}}"] * cols) + "]]"
    
    for i in range(rows):
        row_data = [M[i, j] for j in range(cols)]
        # 打印并确保多行矩阵的格式对齐
        print(" " * (i > 0) + format_str.format(*row_data).replace('],', '],')[:-1]) 

# --- 内部辅助函数：欧拉角轴值提取 ---
def _extract_rpy_from_euler(euler_deg, sequence):
    """ 根据 sequence 从 euler_deg 中提取 Roll, Pitch, Yaw 度数 """
    roll_deg, pitch_deg, yaw_deg = np.nan, np.nan, np.nan
    output_axes = list(sequence)
    r_idx = output_axes.index('x') if 'x' in output_axes else -1
    p_idx = output_axes.index('y') if 'y' in output_axes else -1
    y_idx = output_axes.index('z') if 'z' in output_axes else -1
    
    if r_idx != -1: roll_deg = euler_deg[r_idx]
    if p_idx != -1: pitch_deg = euler_deg[p_idx]
    if y_idx != -1: yaw_deg = euler_deg[y_idx]
    return roll_deg, pitch_deg, yaw_deg

# --- 内部辅助函数：欧拉角准备 ---
def _prepare_euler_input(roll_deg, pitch_deg, yaw_deg, sequence):
    """ 将 RPY 度数和 sequence 转换为 scipy.spatial.transform.Rotation 库需要的输入 """
    angle_map = {'x': np.deg2rad(roll_deg), 'y': np.deg2rad(pitch_deg), 'z': np.deg2rad(yaw_deg)}
    return [angle_map[axis] for axis in sequence]

# =========================================================================
# I. 欧拉角 <-> 四元数 (E <-> Q)
# =========================================================================

def euler_to_quaternion(roll_deg, pitch_deg, yaw_deg, sequence='zyx'):
    """ 欧拉角 (Roll, Pitch, Yaw) -> 四元数 (x, y, z, w) """
    if abs(pitch_deg) >= 89.99 and abs(pitch_deg) <= 90.01:
        print(f"\n⚠️ 警告：Pitch ({pitch_deg:.4f}度) 接近 90度，已触发万向锁 (Gimbal Lock)。")
        
    euler_input = _prepare_euler_input(roll_deg, pitch_deg, yaw_deg, sequence)
    r = R.from_euler(sequence, euler_input)
    quaternion = r.as_quat()

    print(f"\n==============================================")
    print(f"✅ 欧拉角 -> 四元数 转换结果:")
    print(f"   输入欧拉角 (度): R={roll_deg:.4f}, P={pitch_deg:.4f}, Y={yaw_deg:.4f} (顺序: {sequence})")
    print(f"   输出四元数 [x, y, z, w]: {quaternion[0]:.6f}, {quaternion[1]:.6f}, {quaternion[2]:.6f}, {quaternion[3]:.6f}")
    print(f"==============================================")
    return quaternion

def quaternion_to_euler(x, y, z, w, sequence='zyx'):
    """ 四元数 (x, y, z, w) -> 欧拉角 (Roll, Pitch, Yaw) """
    r = R.from_quat([x, y, z, w])
    euler_rad = r.as_euler(sequence)
    euler_deg = np.rad2deg(euler_rad)
    roll_deg, pitch_deg, yaw_deg = _extract_rpy_from_euler(euler_deg, sequence)

    print(f"\n==============================================")
    print(f"✅ 四元数 -> 欧拉角 转换结果:")
    print(f"   输入四元数 [x, y, z, w]: [{x:.6f}, {y:.6f}, {z:.6f}, {w:.6f}]")
    print(f"   目标欧拉角顺序: {sequence}")
    print(f"   输出欧拉角 (度, 对应Roll/X, Pitch/Y, Yaw/Z): R={roll_deg:.4f}, P={pitch_deg:.4f}, Y={yaw_deg:.4f}")
    print(f"==============================================")
    return np.array([roll_deg, pitch_deg, yaw_deg])

# =========================================================================
# II. 旋转矩阵转换 (M <-> E/Q)
# =========================================================================

def euler_to_matrix(roll_deg, pitch_deg, yaw_deg, sequence='zyx'):
    """ 欧拉角 -> 旋转矩阵 (3x3) """
    if abs(pitch_deg) >= 89.99 and abs(pitch_deg) <= 90.01:
        print(f"\n⚠️ 警告：Pitch ({pitch_deg:.4f}度) 接近 90度，已触发万向锁 (Gimbal Lock)。")

    euler_input = _prepare_euler_input(roll_deg, pitch_deg, yaw_deg, sequence)
    r = R.from_euler(sequence, euler_input)
    matrix = r.as_matrix()
    
    print(f"\n==============================================")
    print(f"✅ 欧拉角 -> 旋转矩阵 转换结果:")
    print(f"   输入欧拉角 (度): R={roll_deg:.4f}, P={pitch_deg:.4f}, Y={yaw_deg:.4f} (顺序: {sequence})")
    print_matrix(matrix)
    print(f"==============================================")
    return matrix

def matrix_to_euler(matrix_flat, sequence='zyx'):
    """ 旋转矩阵 (3x3) -> 欧拉角 (Roll, Pitch, Yaw) """
    matrix = np.array(matrix_flat).reshape((3, 3))
    r = R.from_matrix(matrix)
    euler_rad = r.as_euler(sequence)
    euler_deg = np.rad2deg(euler_rad)
    roll_deg, pitch_deg, yaw_deg = _extract_rpy_from_euler(euler_deg, sequence)

    print(f"\n==============================================")
    print(f"✅ 旋转矩阵 -> 欧拉角 转换结果:")
    print_matrix(matrix, "输入旋转矩阵 (3x3)")
    print(f"   目标欧拉角顺序: {sequence}")
    print(f"   输出欧拉角 (度, 对应Roll/X, Pitch/Y, Yaw/Z): R={roll_deg:.4f}, P={pitch_deg:.4f}, Y={yaw_deg:.4f}")
    print(f"==============================================")
    return np.array([roll_deg, pitch_deg, yaw_deg])

def quaternion_to_matrix(x, y, z, w):
    """ 四元数 (x, y, z, w) -> 旋转矩阵 (3x3) """
    r = R.from_quat([x, y, z, w])
    matrix = r.as_matrix()
    
    print(f"\n==============================================")
    print(f"✅ 四元数 -> 旋转矩阵 转换结果:")
    print(f"   输入四元数 [x, y, z, w]: [{x:.6f}, {y:.6f}, {z:.6f}, {w:.6f}]")
    print_matrix(matrix)
    print(f"==============================================")
    return matrix

def matrix_to_quaternion(matrix_flat):
    """ 旋转矩阵 (3x3) -> 四元数 (x, y, z, w) """
    matrix = np.array(matrix_flat).reshape((3, 3))
    r = R.from_matrix(matrix)
    quaternion = r.as_quat()
    
    print(f"\n==============================================")
    print(f"✅ 旋转矩阵 -> 四元数 转换结果:")
    print_matrix(matrix, "输入旋转矩阵 (3x3)")
    print(f"   输出四元数 [x, y, z, w]: {quaternion[0]:.6f}, {quaternion[1]:.6f}, {quaternion[2]:.6f}, {quaternion[3]:.6f}")
    print(f"==============================================")
    return quaternion

# =========================================================================
# III. 齐次变换矩阵解析 (H -> T + R/Q/E) (新增功能)
# =========================================================================

def homogeneous_to_translation(H):
    """ 从 4x4 齐次变换矩阵 H 中提取平移向量 t。 (内部辅助)"""
    return H[0:3, 3]

def homogeneous_to_rotation(H, target_type='q', sequence='zyx'):
    """ 从 4x4 齐次变换矩阵 H 中提取旋转 R，并转换为指定格式。 (内部辅助) """
    R_matrix = H[0:3, 0:3]
    r = R.from_matrix(R_matrix)
    
    if target_type == 'q':
        return r.as_quat()
    
    elif target_type == 'e':
        euler_rad = r.as_euler(sequence)
        euler_deg = np.rad2deg(euler_rad)
        roll_deg, pitch_deg, yaw_deg = _extract_rpy_from_euler(euler_deg, sequence)
        return np.array([roll_deg, pitch_deg, yaw_deg])
        
    else:
        raise ValueError("目标类型必须是 'q' 或 'e'。")


def homogeneous_matrix_to_tq(H_flat):
    """ 齐次变换矩阵 (4x4) -> 平移向量 t + 四元数 q """
    H = np.array(H_flat).reshape((4, 4))
    
    t_vector = homogeneous_to_translation(H)
    quaternion = homogeneous_to_rotation(H, target_type='q')
    
    print(f"\n==============================================")
    print(f"✅ 齐次变换矩阵 -> 平移向量 + 四元数 转换结果:")
    print_matrix(H, "输入齐次变换矩阵 (4x4)")
    
    print(f"\n--- 平移向量 t (Tx, Ty, Tz) ---")
    print(f"[{t_vector[0]:.6f}, {t_vector[1]:.6f}, {t_vector[2]:.6f}]")
    
    print(f"\n--- 旋转表示 (四元数 [x, y, z, w]) ---")
    print(f"[{quaternion[0]:.6f}, {quaternion[1]:.6f}, {quaternion[2]:.6f}, {quaternion[3]:.6f}]")
    print(f"==============================================")
    
    return t_vector, quaternion


def homogeneous_matrix_to_te(H_flat, sequence):
    """ 齐次变换矩阵 (4x4) -> 平移向量 t + 欧拉角 e """
    H = np.array(H_flat).reshape((4, 4))
    
    t_vector = homogeneous_to_translation(H)
    euler_output = homogeneous_to_rotation(H, target_type='e', sequence=sequence)
    roll_deg, pitch_deg, yaw_deg = euler_output
    
    print(f"\n==============================================")
    print(f"✅ 齐次变换矩阵 -> 平移向量 + 欧拉角 转换结果:")
    print_matrix(H, "输入齐次变换矩阵 (4x4)")
    
    print(f"\n--- 平移向量 t (Tx, Ty, Tz) ---")
    print(f"[{t_vector[0]:.6f}, {t_vector[1]:.6f}, {t_vector[2]:.6f}]")
    
    print(f"\n--- 旋转表示 (欧拉角 {sequence} 顺序, 度) ---")
    print(f"Roll (绕X): {roll_deg:.4f}")
    print(f"Pitch (绕Y): {pitch_deg:.4f}")
    print(f"Yaw (绕Z): {yaw_deg:.4f}")
    
    print(f"==============================================")
    
    return t_vector, euler_output


# =========================================================================
# IV. 主函数和命令行解析
# =========================================================================

def main():
    parser = argparse.ArgumentParser(
        description="旋转/平移表示 (欧拉角/四元数/旋转矩阵/齐次矩阵) 相互转换脚本。",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        '--type',
        choices=['e2q', 'q2e', 'e2m', 'm2e', 'q2m', 'm2q', 'h2tq', 'h2te'],
        required=True,
        help="转换类型:\n"
             "'e2q': 欧拉角 -> 四元数 | 'q2e': 四元数 -> 欧拉角\n"
             "'e2m': 欧拉角 -> 旋转矩阵 | 'm2e': 旋转矩阵 -> 欧拉角\n"
             "'q2m': 四元数 -> 旋转矩阵 | 'm2q': 旋转矩阵 -> 四元数\n"
             "'h2tq': 齐次矩阵 -> 平移向量 + 四元数\n"
             "'h2te': 齐次矩阵 -> 平移向量 + 欧拉角"
    )
    
    parser.add_argument(
        '--sequence',
        default='zyx',
        help="欧拉角旋转顺序 (例如 'zyx', 'xyz' 等)。默认 'zyx' (Yaw-Pitch-Roll)。"
    )

    group = parser.add_argument_group('输入参数 (根据 --type 选择对应输入)')
    
    group.add_argument(
        '--rpy',
        nargs=3, type=float, metavar=('ROLL', 'PITCH', 'YAW'),
        help="欧拉角输入 (度): ROLL (绕X), PITCH (绕Y), YAW (绕Z)。"
    )

    group.add_argument(
        '--xyzw',
        nargs=4, type=float, metavar=('X', 'Y', 'Z', 'W'),
        help="四元数输入: X, Y, Z, W。"
    )

    group.add_argument(
        '--matrix',
        nargs=9, type=float, metavar=('R11', 'R12', '...', 'R33'),
        help="旋转矩阵输入 (3x3): R11 R12 R13 R21 R22 R23 R31 R32 R33 (共9个值)。"
    )
    
    group.add_argument(
        '--homogeneous',
        nargs=16, 
        type=float,
        metavar=('H11', 'H12', '...', 'H44'),
        help="齐次变换矩阵输入 (4x4): 16个值，按行主序输入 (R11 R12 R13 Tx R21...)."
    )
    
    args = parser.parse_args()

    # --- 调用转换逻辑 ---
    try:
        # 欧拉角 -> X
        if args.type == 'e2q':
            if args.rpy is None: parser.error("--type 'e2q' 需要 --rpy。")
            euler_to_quaternion(*args.rpy, sequence=args.sequence)
        elif args.type == 'e2m':
            if args.rpy is None: parser.error("--type 'e2m' 需要 --rpy。")
            euler_to_matrix(*args.rpy, sequence=args.sequence)
            
        # 四元数 -> X
        elif args.type == 'q2e':
            if args.xyzw is None: parser.error("--type 'q2e' 需要 --xyzw。")
            quaternion_to_euler(*args.xyzw, sequence=args.sequence)
        elif args.type == 'q2m':
            if args.xyzw is None: parser.error("--type 'q2m' 需要 --xyzw。")
            quaternion_to_matrix(*args.xyzw)
            
        # 旋转矩阵 -> X
        elif args.type == 'm2e':
            if args.matrix is None: parser.error("--type 'm2e' 需要 --matrix。")
            matrix_to_euler(args.matrix, sequence=args.sequence)
        elif args.type == 'm2q':
            if args.matrix is None: parser.error("--type 'm2q' 需要 --matrix。")
            matrix_to_quaternion(args.matrix)

        # 齐次矩阵 -> 平移 + 旋转
        elif args.type == 'h2tq':
            if args.homogeneous is None: parser.error("--type 'h2tq' 需要 --homogeneous。")
            homogeneous_matrix_to_tq(args.homogeneous)
        elif args.type == 'h2te':
            if args.homogeneous is None: parser.error("--type 'h2te' 需要 --homogeneous。")
            homogeneous_matrix_to_te(args.homogeneous, args.sequence)
            
    except Exception as e:
        print(f"\n❌ 运行时发生错误: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    try:
        # 检查依赖
        import numpy as np
        from scipy.spatial.transform import Rotation as R
    except ImportError:
        print("\n❌ 错误: 需要安装 'numpy' 和 'scipy' 库。")
        print("   请运行: pip install numpy scipy")
        sys.exit(1)
        
    # 如果没有命令行参数，则进行一次内置演示
    if len(sys.argv) == 1:
        print("--- 自动演示模式：请使用命令行参数运行实际转换 ---")
        H_demo = [0.997775, -0.019222, -0.063840, 1.544956,
                  0.018845, 0.999801, -0.006498, -0.086107,
                  0.063952, 0.005280, 0.997939, 1.408000,
                  0.000000, 0.000000, 0.000000, 1.000000]
        
        homogeneous_matrix_to_tq(H_demo)
        
    else:
        main()