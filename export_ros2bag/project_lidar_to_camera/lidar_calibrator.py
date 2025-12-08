import numpy as np
from scipy.spatial.transform import Rotation as R
from typing import Dict, List, Tuple

# ======================================================================
# 1. 激光雷达安装参数配置 (LIDAR_CONFIGS)
# 请手动将您的标定结果填入到下面的 'translation' 和 'rpy_angles' 字段中。
# ----------------------------------------------------------------------
# 约定:
# - translation: [x, y, z] (单位: 米)
# - rpy_angles: [roll, pitch, yaw] (单位: 弧度 或 角度，取决于你如何填入)
#   **重要提示**: SciPy 默认 RPY 顺序为 Z-Y-X (Yaw-Pitch-Roll)
# ======================================================================

LIDAR_CONFIGS: Dict[str, Dict[str, List[float]]] = {
    #-0.0444048 0.0496087 -0.0306114 -0.140688 0.0247991 6.22395e-310
    "iv_points_front_left": {
        # 相对于自车坐标系的平移 [x, y, z]
        "translation": [2.048, 0.5695, 0.698],  
        # 旋转角度 [Roll, Pitch, Yaw]
        # "rpy_angles": [0.0, 0.0, 45.0]     
        # "rpy_angles": [np.rad2deg(-0.0444048), np.rad2deg(0.0496087), 45+np.rad2deg(-0.0306114)]
        "rpy_angles": [np.rad2deg(-0.0444048) + 1, -0.45, 45+np.rad2deg(-0.0306114) -0.5]   
    },
    "iv_points_front_right": {
        "translation": [2.048, -0.5695, 0.698],
        "rpy_angles": [np.rad2deg(-0.0152855)+2, np.rad2deg(0.0215469)-1.2, -45.0 + np.rad2deg(0.0497281)+0.75]
        # "rpy_angles": [np.rad2deg(-0.0113257), np.rad2deg(-0.0167676), -45.0 + np.rad2deg(0.0558086)]
    },
    "iv_points_front_mid": {
        # "translation": [1.946, 0.0, 1.408],
        "translation": [1.946, 0.02, 1.408],
        "rpy_angles": [np.rad2deg(-0.0071599), np.rad2deg(-0.0538616), np.rad2deg(-0.000957744)-0.5]
    },
    # 注意: 您可能有两个 "iv_points_front_left"，我保留了一个并添加了您列出的其他四个。
    # 假设这里的 "iv_points_front_left" 是一个笔误，我将使用您在请求中列出的五个唯一ID：
    # iv_points_front_left, iv_points_front_right, iv_points_front_mid, iv_points_rear_left, iv_points_rear_right
    "iv_points_rear_left": {
        "translation": [-0.794, 0.594, 0.698],
        "rpy_angles": [np.rad2deg(-0.00757353) + 1, np.rad2deg(-0.0135103) + 0.9, 135.0 + np.rad2deg(-0.0809288)+ 0.7]
    },
    "iv_points_rear_right": {
        "translation": [-0.794, -0.593, 0.698],
        # "rpy_angles": [np.rad2deg(-0.0349293), np.rad2deg(0.0369922), -135 + np.rad2deg(0.217622)]
        "rpy_angles": [+2.45, np.rad2deg(0.0369922)-0.2, -135 + np.rad2deg(0.217622) - 0.85]
    }
}

# ----------------------------------------------------------------------
# 配置开关
# ----------------------------------------------------------------------
# 如果您的 rpy_angles 是以“角度”为单位，请设置为 True。如果单位是“弧度”，请设置为 False。
ANGLES_IN_DEGREES = True 

# ----------------------------------------------------------------------
# 2. RPY 到四元数转换函数
# ----------------------------------------------------------------------

def rpy_to_quaternion(roll: float, pitch: float, yaw: float, 
                      order: str = 'zyx', degrees: bool = ANGLES_IN_DEGREES) -> np.ndarray:
    """
    将 Roll, Pitch, Yaw 欧拉角转换为四元数 (x, y, z, w)。
    
    采用 Z-Y-X 顺序 (Yaw -> Pitch -> Roll) 进行转换。
    
    Args:
        roll (float): X 轴旋转角度 (Roll)。
        pitch (float): Y 轴旋转角度 (Pitch)。
        yaw (float): Z 轴旋转角度 (Yaw)。
        order (str): 欧拉角应用的旋转顺序，默认 'zyx'。
        degrees (bool): 输入角度的单位。True 为度，False 为弧度。
        
    Returns:
        np.ndarray: 包含四元数 [x, y, z, w] 的 NumPy 数组。
    """
    # SciPy 的 Rotation 类接受 RPY 角度和旋转顺序
    # order='zyx' 意味着输入的欧拉角数组顺序是 [yaw, pitch, roll]
    
    # 按照 'zyx' 顺序创建输入数组: [Z角, Y角, X角] -> [Yaw, Pitch, Roll]
    rpy_array = np.array([yaw, pitch, roll]) 
    
    try:
        # 使用 SciPy 的 Rotation.from_euler 方法进行转换
        r = R.from_euler(order, rpy_array, degrees=degrees)
        # 转换为四元数，SciPy 返回 [x, y, z, w] 顺序
        quaternion = r.as_quat()
        return quaternion
    except ValueError as e:
        print(f"❌ 转换错误: {e}")
        return np.array([np.nan, np.nan, np.nan, np.nan])

# ----------------------------------------------------------------------
# 3. 示例执行和测试
# ----------------------------------------------------------------------

def run_conversion_and_print_matrix():
    """
    遍历所有雷达配置，计算它们的四元数和 4x4 变换矩阵。
    """
    print("=====================================================")
    print(f"✨ Lidar 外部标定参数解析 ({'角度' if ANGLES_IN_DEGREES else '弧度'} 输入)")
    print("=====================================================")
    
    all_calibrations = {}
    
    for lidar_id, config in LIDAR_CONFIGS.items():
        roll, pitch, yaw = config["rpy_angles"]
        tx, ty, tz = config["translation"]
        
        # 将 RPY 转换为四元数
        quat = rpy_to_quaternion(roll, pitch, yaw)
        
        # 将 RPY 转换为 3x3 旋转矩阵
        rpy_array = np.array([yaw, pitch, roll])
        R_matrix = R.from_euler('zyx', rpy_array, degrees=ANGLES_IN_DEGREES).as_matrix()
        
        # 构建 4x4 齐次变换矩阵 M
        T_matrix = np.eye(4)
        T_matrix[:3, :3] = R_matrix
        T_matrix[:3, 3] = [tx, ty, tz]

        # 存储结果
        all_calibrations[lidar_id] = {
            "quaternion_xyzw": quat.tolist(),
            "translation_xyz": config["translation"],
            "rotation_matrix_4x4": T_matrix.tolist()
        }

        # 打印结果
        print(f"\n--- 🆔 {lidar_id} ---")
        print(f"   平移 (T_xyz): {config['translation']}")
        print(f"   欧拉角 (RPY): {[round(roll, 6), round(pitch, 6), round(yaw, 6)]}")
        print(f"   四元数 (xyzw): {[round(q, 6) for q in quat.tolist()]}")
        print("\n   4x4 变换矩阵 M (从Lidar到Vehicle):")
        print(T_matrix)
        
    print("\n=====================================================")
    print("✅ 所有激光雷达的四元数和变换矩阵已计算完毕。")
    print("=====================================================")
    
    # 假设这里是调用一个函数将点云P_L转换到自车坐标系P_V的示例
    # P_V = M @ P_L
    
    # 返回所有计算结果以备后用
    return all_calibrations

if __name__ == "__main__":
    # 运行转换和打印函数
    run_conversion_and_print_matrix()