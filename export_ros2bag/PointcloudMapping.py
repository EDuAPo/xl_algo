import json
import os
import numpy as np
import open3d as o3d
from scipy.spatial.transform import Rotation as R

def process_point_clouds(index_json_path, ins_json_path, pcd_base_folder="./"):
    """
    读取JSON配置，匹配时间戳，拼接点云。
    
    Args:
        index_json_path: 包含 iv_points_front_mid 和 ins 的 json 文件路径
        ins_json_path: 包含 timestamp_desc 和位姿信息的 json 文件路径
        pcd_base_folder: pcd 文件所在的文件夹路径
    """
    
    # --- 1. 读取 JSON 数据 ---
    try:
        with open(index_json_path, 'r', encoding='utf-8') as f:
            sensor_data_list = json.load(f)
            # 如果json包含在列表里，直接用；如果是单个对象，转为列表
            if isinstance(sensor_data_list, dict):
                sensor_data_list = [sensor_data_list]

        with open(ins_json_path, 'r', encoding='utf-8') as f:
            ins_data_list = json.load(f)
    except Exception as e:
        print(f"读取JSON文件失败: {e}")
        return

    # --- 2. 构建位姿查询字典 (Hash Map) ---
    # 将 INS 数据转为字典，key 为 timestamp_desc，方便快速查找 O(1)
    ins_map = {item['timestamp_desc']: item for item in ins_data_list}

    # 初始化全局点云对象
    global_pcd = o3d.geometry.PointCloud()
    
    print(f"开始处理 {len(sensor_data_list)} 帧数据...")

    # --- 3. 循环处理每一帧 ---
    for idx, frame in enumerate(sensor_data_list):
        # 获取关联键 ins (对应 ins_data 中的 timestamp_desc)
        ins_key = frame.get("ins")
        pcd_filename = frame.get("iv_points_front_mid")

        if not ins_key or not pcd_filename:
            print(f"跳过第 {idx} 帧: 缺少 ins 或 pcd 文件名")
            continue

        # 在 ins_map 中查找对应的位姿数据
        pose_data = ins_map.get(ins_key)
        
        if pose_data is None:
            print(f"未找到对应位姿数据: {ins_key}")
            continue
        if idx > 10:continue

        # --- 4. 构建变换矩阵 ---
        # 提取平移 (根据你的要求使用 tran_utm_x, tran_utm_y)
        # 注意：如果是2D平面移动，Z通常设为0或读取 tran_utm_z (如果存在)
        tx = pose_data.get("tran_utm_x", 0.0)
        ty = pose_data.get("tran_utm_y", 0.0)
        tz = pose_data.get("tran_utm_z", 0.0) # 样例中虽未强调，但通常需要Z轴

        translation = np.array([tx, ty, tz])

        # 提取四元数 (x, y, z, w)
        qx = pose_data.get("quaternion_x", 0.0)
        qy = pose_data.get("quaternion_y", 0.0)
        qz = pose_data.get("quaternion_z", 0.0)
        qw = pose_data.get("quaternion_w", 1.0)

        # 使用 scipy 将四元数转换为 3x3 旋转矩阵
        # scipy 的顺序通常是 scalar_last (x, y, z, w)
        r = R.from_quat([qx, qy, qz, qw])
        rotation_matrix = r.as_matrix()

        # 构建 4x4 齐次变换矩阵
        transform_matrix = np.eye(4)
        transform_matrix[:3, :3] = rotation_matrix
        transform_matrix[:3, 3] = translation

        # --- 5. 加载并变换点云 ---
        pcd_path = os.path.join(pcd_base_folder, pcd_filename)
        
        if not os.path.exists(pcd_path):
            print(f"文件不存在: {pcd_path}")
            continue
            
        # 读取点云
        current_pcd = o3d.io.read_point_cloud(pcd_path)
        
        # 应用变换 (将局部坐标系点云转换到全局/世界坐标系)
        current_pcd.transform(transform_matrix)
        
        # 叠加到全局点云
        global_pcd += current_pcd
        print(f"已合并: {ins_key}")

    # --- 6. 结果展示与保存 ---
    if not global_pcd.is_empty():
        print("处理完成，正在进行体素下采样以优化显示...")
        # 可选：体素下采样，防止点云过密导致卡顿
        global_pcd = global_pcd.voxel_down_sample(voxel_size=0.1)
        
        print("正在显示拼接结果...")
        o3d.visualization.draw_geometries([global_pcd], 
                                          window_name="Point Cloud Mapping",
                                          width=800, height=600)
        
        # 保存结果
        # o3d.io.write_point_cloud("merged_map.pcd", global_pcd)
    else:
        print("未能合并任何点云。")

# --- 使用示例 ---
# 请将下面的路径替换为你实际的文件路径
if __name__ == "__main__":
    # 假设你有两个json文件: sensor_index.json 和 ins_pose.json
    # 以及存放pcd文件的目录 pcd_data/
    
    # 为了演示，这里假设代码和json在同一目录
    process_point_clouds(
        index_json_path="/home/zgw/Desktop/test00/sample.json", 
        ins_json_path="/media/zgw/T7/1124/cmy/bag/full_output/113046_113048/undistorted/ins.json", 
        pcd_base_folder="/media/zgw/T7/1124/cmy/bag/full_output/113046_113048/undistorted/iv_points_front_mid/pcd_binary" 
    )