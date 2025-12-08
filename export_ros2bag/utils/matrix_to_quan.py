import numpy as np

# 完整的 4x4 变换矩阵 (T)
T_matrix = np.array([
    [0.997775, -0.019222, -0.063840, 1.544956],
    [0.018845, 0.999801, -0.006498, -0.086107],
    [0.063952, 0.005280, 0.997939, 1.408000],
    [0.000000, 0.000000, 0.000000, 1.000000]
])

# 提取旋转矩阵 (R) - 选取前3行和前3列
R_matrix = T_matrix[0:3, 0:3]

print("--- 旋转矩阵 (R) ---")
print(R_matrix)

# 如果您也想提取平移向量 (t)
t_vector = T_matrix[0:3, 3]
print("\n--- 平移向量 (t) ---")
print(t_vector)


ego_to_lidar_matrix = R_matrix.T
print("\n--- 车体坐标系到激光雷达坐标系的旋转矩阵 (R_ego_to_lidar) ---")
print(ego_to_lidar_matrix)


def matrix_to_quaternion(R: np.ndarray) -> np.ndarray:
    """
    将 3x3 旋转矩阵转换为四元数 (x, y, z, w)。
    """
    qw = np.sqrt(1 + R[0, 0] + R[1, 1] + R[2, 2]) / 2
    qx = (R[2, 1] - R[1, 2]) / (4 * qw)
    qy = (R[0, 2] - R[2, 0]) / (4 * qw)
    qz = (R[1, 0] - R[0, 1]) / (4 * qw)

    return np.array([qx, qy, qz, qw])


quaternion = matrix_to_quaternion(ego_to_lidar_matrix)

print("\n--- 四元数 [x, y, z, w] ---")
print(quaternion)