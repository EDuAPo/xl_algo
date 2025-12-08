import open3d as o3d
import sys
import os

def view_pcd_file(filepath):
    """加载并使用 Open3D Viewer 显示 PCD 文件，并调整点大小。"""
    if not os.path.exists(filepath):
        print(f"❌ 错误: 文件未找到: {filepath}")
        return

    print(f"✅ 正在加载点云文件: {filepath}")
    
    try:
        pcd = o3d.io.read_point_cloud(filepath)
        
        if not pcd.has_points():
            print("⚠️ 警告: 点云文件为空，无法显示。")
            return
        
        # ----------------------------------------------------
        # 【核心修改部分】: 创建和配置渲染选项
        # ----------------------------------------------------
        vis = o3d.visualization.Visualizer()
        vis.create_window(window_name="Open3D Point Cloud Viewer")
        vis.add_geometry(pcd)
        
        # 获取渲染控制器
        render_option = vis.get_render_option()
        
        # 1. 调整点大小 (以像素为单位)
        # 默认值通常是 3.0 或 4.0。 1.0 是最小的可见尺寸。
        # 您可以尝试 1.0 或 2.0
        render_option.point_size = 0.3
        
        # 可选：关闭或调整光源，防止点云被阴影干扰
        # render_option.light_on = False 

        # 2. 运行可视化
        vis.run()
        vis.destroy_window()
        
    except Exception as e:
        print(f"❌ 加载或显示点云时发生错误: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python view_pcd.py <点云文件路径>")
    else:
        view_pcd_file(sys.argv[1])