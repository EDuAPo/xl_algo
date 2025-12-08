import numpy as np
from typing import Dict, List, Any
from scipy.spatial.transform import Rotation as R
from .global_mapping import CAMERA_MAP

# ======================================================================
# 相机参数配置 (CAMERA_CONFIGS)
# 请手动将您的相机标定结果填入。
# ----------------------------------------------------------------------
# 配置优先级：如果 ext_quaternion_xyzw 不全为零，则优先使用四元数进行旋转计算。
# 如果 ext_quaternion_xyzw 全为零，则使用 ext_rpy_angles。
# ======================================================================

STANDARD_CAMERAS_IDS = ["camera_cam_8M_wa_front"]

CAMERA_CONFIGS: Dict[str, Dict[str, List[float]]] = {
    "camera_cam_3M_front": {
        # 相机在自车坐标系下的平移 [x, y, z] (单位: 米)
        "ext_translation": [2.0554651664686703, -0.0060563259766355515, 0.7719874730328724],
        
        # 旋转方式 1: 四元数 [x, y, z, w] (优先使用)
        "ext_quaternion_xyzw": [-0.59727991, 0.60367301, -0.37121864, 0.37554271],
        
        # 旋转方式 2: 欧拉角 [Roll, Pitch, Yaw] (如果四元数全为零，则使用此项)
        # Roll (X), Pitch (Y), Yaw (Z) (单位: 角度)
        "ext_rpy_angles": [0.0, 0.0, 0.0],
        
        # 内参: 焦距 [fx, fy] (像素单位)
        "focal_length": [570.58060231, 570.72929139],
        
        # 内参: 主点 [cx, cy] (像素单位)
        "principal_point": [961.14455421, 764.61773278],
        
        # 内参: 畸变系数 (径向和切向畸变)
        # 格式: [k1, k2, p1, p2]
        "distortion_coeffs": [0.01384849, -0.00557897, -0.00019125, -0.000271]
    },
    
    "camera_cam_3M_left": {
        # 相机在自车坐标系下的平移 [x, y, z] (单位: 米)
        "ext_translation": [0.6399342363722622, 0.5465569043094777, 0.7740377856469716],
        
        # 旋转方式 1: 四元数 [x, y, z, w] (优先使用)
        "ext_quaternion_xyzw": [-0.7965188127280065, -0.009603685458836405, -0.014041396620831974, 0.6043743784914373],
        
        # 旋转方式 2: 欧拉角 [Roll, Pitch, Yaw] (如果四元数全为零，则使用此项)
        # Roll (X), Pitch (Y), Yaw (Z) (单位: 角度)
        "ext_rpy_angles": [0.0, 0.0, 0.0],
        
        # 内参: 焦距 [fx, fy] (像素单位)
        "focal_length": [574.46857959, 574.74972345],
        
        # 内参: 主点 [cx, cy] (像素单位)
        "principal_point": [959.90342689, 764.76712126],
        
        # 内参: 畸变系数 (径向和切向畸变)
        # 格式: [k1, k2, p1, p2]
        "distortion_coeffs": [0.014729234, -0.00518548001, -0.00140932415, 8.43700503e-05]
    },
    
    "camera_cam_3M_rear": {
        # 相机在自车坐标系下的平移 [x, y, z] (单位: 米)
        "ext_translation": [-0.8120441845528125, -0.007706656679650613, 0.7790851763643512],
        
        # 旋转方式 1: 四元数 [x, y, z, w] (优先使用)
        "ext_quaternion_xyzw": [0.59428544, 0.59424186, -0.38014468, -0.38625309],
        
        # 旋转方式 2: 欧拉角 [Roll, Pitch, Yaw] (如果四元数全为零，则使用此项)
        # Roll (X), Pitch (Y), Yaw (Z) (单位: 角度)
        "ext_rpy_angles": [0.0, 0.0, 0.0],
        
        # 内参: 焦距 [fx, fy] (像素单位)
        "focal_length": [572.8924374, 573.1017971],
        
        # 内参: 主点 [cx, cy] (像素单位)
        "principal_point": [954.37442618, 763.51180296],
        
        # 内参: 畸变系数 (径向和切向畸变)
        # 格式: [k1, k2, p1, p2]
        "distortion_coeffs": [0.0168507092, -0.00639218326, -0.000988783168, 5.17753632e-05]
    },
    
    "camera_cam_3M_right": {
        # 相机在自车坐标系下的平移 [x, y, z] (单位: 米)
        "ext_translation": [0.6370943155534893, -0.5415086896102413, 0.767813168376311],
        
        # 旋转方式 1: 四元数 [x, y, z, w] (优先使用)
        "ext_quaternion_xyzw": [0.02445160333385736, 0.7852763089378643, -0.618635143035094, 0.005813563216857122],
        
        # 旋转方式 2: 欧拉角 [Roll, Pitch, Yaw] (如果四元数全为零，则使用此项)
        # Roll (X), Pitch (Y), Yaw (Z) (单位: 角度)
        "ext_rpy_angles": [0.0, 0.0, 0.0],
        
        # 内参: 焦距 [fx, fy] (像素单位)
        "focal_length": [571.88705254, 572.39154819],
        
        # 内参: 主点 [cx, cy] (像素单位)
        "principal_point": [962.36612444, 767.3246358],
        
        # 内参: 畸变系数 (径向和切向畸变)
        # 格式: [k1, k2, p1, p2]
        "distortion_coeffs": [0.01649807, -0.00668417, 0.00043621, -0.00045291]
    },
    
    "camera_cam_8M_wa_front": {
        # 相机在自车坐标系下的平移 [x, y, z] (单位: 米)
        "ext_translation": [1.946, 0.007, 0.998],
        
        # 旋转方式 1: 四元数 [x, y, z, w] (优先使用)
        "ext_quaternion_xyzw": [-0.49928652, 0.50428056, -0.50067057, 0.49572481],
        
        # 旋转方式 2: 欧拉角 [Roll, Pitch, Yaw] (如果四元数全为零，则使用此项)
        # Roll (X), Pitch (Y), Yaw (Z) (单位: 角度)
        "ext_rpy_angles": [-4, 89.5, -85.5],
        
        # 内参: 焦距 [fx, fy] (像素单位)
        "focal_length": [1923.77263, 1924.71305],
        
        # 内参: 主点 [cx, cy] (像素单位)
        "principal_point": [1914.74603, 1131.61475],
        
        # 内参: 畸变系数 (径向和切向畸变)
        # 格式: [k1, k2, p1, p2, k3] (8M相机使用5参数模型)
        "distortion_coeffs": [-0.319543334, 0.108013901, 6.43760453e-06, -9.69524494e-05, -0.0168342887]
    }
}

# ----------------------------------------------------------------------
# 配置开关
# ----------------------------------------------------------------------
# 如果您的 ext_rpy_angles 是以“角度”为单位，请设置为 True。如果单位是“弧度”，请设置为 False。
CAMERA_ANGLES_IN_DEGREES = True 

# ----------------------------------------------------------------------
# 辅助函数: 用于从配置中构建相机变换矩阵和内参矩阵
# ----------------------------------------------------------------------

def get_camera_extrinsics(short_name: str) -> Dict[str, Any]:
    """
    根据相机短名称 (例如: '8m_wa_front', '3m_front') 获取其外参配置。
    
    参数:
        short_name (str): 相机的短名称。
        
    返回:
        Dict[str, Any]: 包含 "translation" 和 "rotation" (四元数) 的字典。
        如果找不到配置，则返回默认的零值配置。
    """
    # 1. 通过 CAMERA_MAP 将短名称转换为长名称 (Config ID)
    config_id = CAMERA_MAP.get(short_name)
    
    # 2. 从 CAMERA_CONFIGS 获取完整配置
    config = CAMERA_CONFIGS.get(config_id)

    # 3. 检查并构造返回结果
    if config:
        # 从 CAMERA_CONFIGS 中提取 translation 和 rotation (四元数)
        return {
            "translation": config.get("ext_translation", [0.0, 0.0, 0.0]),
            "rotation": config.get("ext_quaternion_xyzw", [0.0, 0.0, 0.0, 1.0])
        }
    else:
        # 如果找不到，返回一个默认配置 (与您原始函数行为一致)
        print(f"WARNING: 找不到短名称 '{short_name}' 对应的相机配置，使用默认零值。")
        return {
            "translation": [0.0, 0.0, 0.0],
            "rotation": [0.0, 0.0, 0.0, 1.0] # x, y, z, w (这里使用 w=1.0)
        }
    
def get_camera_extrinsics_matrix(camera_id: str) -> np.ndarray:
    """
    根据配置获取相机从自车坐标系到相机坐标系的 4x4 变换矩阵 (T_vehicle_to_camera)。
    优先使用配置中的四元数进行旋转计算。
    
    Args:
        camera_id (str): 相机的ID。
        
    Returns:
        np.ndarray: 从自车坐标系到相机坐标系的 4x4 变换矩阵。
    """
    config = CAMERA_CONFIGS.get(camera_id)
    if not config:
        raise ValueError(f"未找到相机ID '{camera_id}' 的配置。")
    
    tx, ty, tz = config["ext_translation"]
    
    # --- 1. 构建旋转对象 R_camera_in_vehicle ---
    
    # 优先级 1: 检查四元数
    quat = np.array(config["ext_quaternion_xyzw"], dtype=np.float64)
    # 检查四元数是否全为零 (例如 [0, 0, 0, 0])
    is_quat_zero = np.allclose(quat, np.zeros_like(quat))
    
    if not is_quat_zero:
        print(f"INFO: 使用相机 '{camera_id}' 的四元数外参进行旋转计算。")
        # 四元数 [x, y, z, w] 
        r_camera_in_vehicle_obj = R.from_quat(quat)
    else:
        # 优先级 2: 使用 RPY (如果四元数全为零)
        print(f"INFO: 四元数为零，使用相机 '{camera_id}' 的欧拉角外参进行旋转计算 (Z-Y-X 顺序)。")
        roll, pitch, yaw = config["ext_rpy_angles"]
        # SciPy 的 from_euler('zyx', angles) 默认 angles 顺序为 [yaw, pitch, roll]
        angles = [yaw, pitch, roll] 
        r_camera_in_vehicle_obj = R.from_euler('zyx', angles, degrees=CAMERA_ANGLES_IN_DEGREES)

    # 获取旋转矩阵
    R_camera_in_vehicle = r_camera_in_vehicle_obj.as_matrix()
    
    # --- 2. 构建 T_camera_in_vehicle ---
    # T_cam_in_veh 定义了相机坐标系原点和姿态相对于自车坐标系的位置和姿态
    T_cam_in_veh = np.eye(4)
    T_cam_in_veh[:3, :3] = R_camera_in_vehicle
    T_cam_in_veh[:3, 3] = np.array([tx, ty, tz])
    
    # --- 3. 计算逆变换矩阵 ---
    # T_vehicle_to_camera = T_camera_in_vehicle.inv()
    # 这个矩阵用于将自车坐标系下的点 P_V 转换到相机坐标系下 P_C: P_C = T_V_C @ P_V
    T_vehicle_to_camera_matrix = np.linalg.inv(T_cam_in_veh)
    
    return T_vehicle_to_camera_matrix

# 以下函数保持不变

def get_camera_intrinsics_matrix(camera_id: str) -> np.ndarray:
    """
    根据配置获取相机的 3x3 内参矩阵 (K)。
    """
    config = CAMERA_CONFIGS.get(camera_id)
    if not config:
        raise ValueError(f"未找到相机ID '{camera_id}' 的配置。")
        
    fx, fy = config["focal_length"]
    cx, cy = config["principal_point"]
    
    K = np.array([
        [fx, 0, cx],
        [0, fy, cy],
        [0, 0, 1]
    ], dtype=np.float64)
    
    return K

def get_camera_distortion_coefficients(camera_id: str) -> np.ndarray:
    """
    根据配置获取相机的畸变系数。
    """
    config = CAMERA_CONFIGS.get(camera_id)
    if not config:
        raise ValueError(f"未找到相机ID '{camera_id}' 的配置。")
        
    return np.array(config["distortion_coeffs"], dtype=np.float64)

def is_fisheye_camera(camera_id: str) -> bool:
    """
    检查给定的相机ID是否属于鱼眼相机。
    """
    return camera_id not in STANDARD_CAMERAS_IDS

# ----------------------------------------------------------------------
# 示例用法 (可选，用于测试 camera_calibrator.py 本身)
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("--- ⚙️ 相机标定参数测试 ---")
    camera_id = "front_camera"
    
    # 设置一个示例四元数用于测试 (例如：绕 Z 轴旋转 90 度)
    # cos(45), 0, 0, sin(45) -> w, x, y, z
    # 四元数 (x, y, z, w) -> [0, 0, 0.70710678, 0.70710678]
    test_quat = [0.0, 0.0, 0.70710678, 0.70710678] 
    
    # 临时覆盖配置进行四元数测试
    temp_config = CAMERA_CONFIGS[camera_id].copy()
    temp_config["ext_quaternion_xyzw"] = test_quat
    
    # 模拟运行
    try:
        CAMERA_CONFIGS[camera_id] = temp_config
        T_v_to_c_quat = get_camera_extrinsics_matrix(camera_id)
        
        print(f"\n四元数 '{test_quat}' 对应的外部变换矩阵 (T_vehicle_to_camera):")
        print(T_v_to_c_quat)
        
        # 临时覆盖配置进行 RPY 回退测试 (将四元数置零)
        temp_config["ext_quaternion_xyzw"] = [0.0, 0.0, 0.0, 0.0]
        temp_config["ext_rpy_angles"] = [0.0, 0.0, 90.0] # 绕Z轴90度
        CAMERA_CONFIGS[camera_id] = temp_config
        
        T_v_to_c_rpy = get_camera_extrinsics_matrix(camera_id)
        
        print(f"\nRPY '[0, 0, 90.0]' 对应的外部变换矩阵 (T_vehicle_to_camera):")
        print(T_v_to_c_rpy)
        
    except ValueError as e:
        print(f"错误: {e}")