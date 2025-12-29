from typing import Dict, List
# ======================================================================
# 全局配置 & Lidar 映射表
# ======================================================================

# Lidar 映射表: 用户输入参数(短名称)到配置ID(长名称)的映射
LIDAR_MAP = {
    "front_mid": "iv_points_front_mid",
    "front_left": "iv_points_front_left",
    "front_right": "iv_points_front_right",
    "rear_left": "iv_points_rear_left",
    "rear_right": "iv_points_rear_right",
    "left_mid": "iv_points_left_mid",
    "right_mid": "iv_points_right_mid",
}

CAMERA_MAP = {
    "front_8M": "camera_cam_8M_wa_front",
    "left": "camera_cam_3M_left",
    "right": "camera_cam_3M_right",
    "front": "camera_cam_3M_front",
    "rear": "camera_cam_3M_rear",
}

LIDAR_CAMERA_MAP: Dict[str, List[str]] = {
    "front_mid": ["front", "front_8M"],
    "front_left": ["left", "front"],
    "front_right": ["right", "front"],
    "left_mid": ["left"],
    "right_mid": ["right"],
    "rear_left": ["left", "rear"],
    "rear_right": ["right", "rear"],
}