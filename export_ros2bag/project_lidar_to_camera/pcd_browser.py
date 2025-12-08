#!/usr/bin/env python3

import open3d as o3d
import numpy as np
import os
import sys
import argparse
import re

# ======================================================================
# 【修复点 1】通用键盘键码定义 (绕过 'o3d.visualization.key' 依赖)
# 这些是 Open3D 底层使用的 GLFW 键码。
# ======================================================================
KEY_LEFT = 263
KEY_RIGHT = 262
KEY_UP = 265
KEY_DOWN = 264

# ======================================================================
# 辅助函数 (保持不变)
# ======================================================================

def extract_time_id(filename: str) -> int:
    """
    从文件名中提取完整的数字串作为时间ID。
    """
    base_name = os.path.splitext(filename)[0]
    time_id_str = re.sub(r'[^0-9]', '', base_name)
    
    if time_id_str:
        return int(time_id_str)
    return -1

# ======================================================================
# 核心类：交互式点云浏览器
# ======================================================================

class PCDBrowser:
    def __init__(self, pcd_dir, initial_point_size=2.0):
        self.pcd_dir = pcd_dir
        self.initial_point_size = initial_point_size
        self.files = self._load_sorted_files()
        self.current_index = 0
        self.current_pcd = o3d.geometry.PointCloud()
        self.vis = None
        
        if not self.files:
            print(f"❌ 错误: 目录 {pcd_dir} 中未找到任何 PCD/BIN 文件。")
            sys.exit(1)

        print(f"✅ 找到 {len(self.files)} 个文件。准备启动浏览器...")

    def _load_sorted_files(self):
        """加载目录中所有 .pcd 或 .bin 文件，并按时间 ID 排序。"""
        file_list = []
        
        for filename in os.listdir(self.pcd_dir):
            if filename.lower().endswith(('.pcd', '.bin')):
                file_path = os.path.join(self.pcd_dir, filename)
                time_id = extract_time_id(filename)
                if time_id > 0:
                    file_list.append((time_id, file_path))
                    
        file_list.sort(key=lambda x: x[0])
        return [item[1] for item in file_list]

    def _load_pcd(self, file_path):
        """加载点云文件。"""
        try:
            pcd = o3d.io.read_point_cloud(file_path)
            if not pcd.has_points():
                return None
            return pcd
        except Exception as e:
            print(f"❌ 加载文件 {os.path.basename(file_path)} 失败: {e}")
            return None

    def _update_visualization(self):
        """更新可视化窗口中的点云。"""
        if self.vis is None:
            return

        # 移除旧的点云
        self.vis.remove_geometry(self.current_pcd, reset_bounding_box=False)
        
        file_path = self.files[self.current_index]
        new_pcd = self._load_pcd(file_path)
        
        if new_pcd is None:
            # 如果加载失败，尝试下一张
            print(f"❌ 加载当前帧 {os.path.basename(file_path)} 失败，尝试下一帧...")
            self.current_index = (self.current_index + 1) % len(self.files)
            self._update_visualization()
            return

        self.current_pcd = new_pcd
        self.vis.add_geometry(self.current_pcd, reset_bounding_box=True) 
        
        # 【修复点 2】: 移除动态更新窗口标题 (set_window_title)
        filename = os.path.basename(file_path)
        
        self.vis.update_renderer()
        # 将帧信息输出到终端，代替窗口标题
        print(f"✅ 已加载 Frame {self.current_index + 1}/{len(self.files)}: {filename}")
        
    # =================================================================
    # 【修复点 3】: 独立回调函数，不再依赖 vis.get_key()
    # =================================================================
    
    def _next_frame_callback(self, vis, action, mods):
        """处理向右或向下的按键 (下一帧)。"""
        # 只处理按键按下事件 (action == 1)
        if action == 1:
            if self.current_index < len(self.files) - 1:
                self.current_index += 1
                self._update_visualization()
            else:
                # 仅在终端提示
                print("提示: 已是最后一帧！") 
            return True # 告诉 Open3D 已经处理了该事件
        return False
        
    def _prev_frame_callback(self, vis, action, mods):
        """处理向左或向上的按键 (上一帧)。"""
        # 只处理按键按下事件 (action == 1)
        if action == 1:
            if self.current_index > 0:
                self.current_index -= 1
                self._update_visualization()
            else:
                # 仅在终端提示
                print("提示: 已是第一帧！")
            return True # 告诉 Open3D 已经处理了该事件
        return False


    def run(self):
        """启动浏览器可视化。"""
        self.vis = o3d.visualization.VisualizerWithKeyCallback()
        
        # 在创建时设置初始窗口标题
        self.vis.create_window(window_name="PCD Browser (Open3D)", width=1280, height=720)

        # 【修复点 4】注册键盘回调函数，使用整数键码和独立回调函数
        # 向前：右箭头和下箭头
        self.vis.register_key_action_callback(KEY_RIGHT, self._next_frame_callback)
        self.vis.register_key_action_callback(KEY_DOWN, self._next_frame_callback)
        
        # 向后：左箭头和上箭头
        self.vis.register_key_action_callback(KEY_LEFT, self._prev_frame_callback)
        self.vis.register_key_action_callback(KEY_UP, self._prev_frame_callback)
        
        # 设置初始渲染选项
        render_option = self.vis.get_render_option()
        render_option.point_size = self.initial_point_size
        
        # 加载并显示第一帧
        self._update_visualization()
        
        # 开始主循环
        self.vis.run()
        self.vis.destroy_window()


# ======================================================================
# 主函数
# ======================================================================

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="交互式点云浏览器：浏览指定目录下按时间排序的 PCD/BIN 文件。",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument("--pcd", type=str, required=True, 
                        help="包含要查看的 PCD/BIN 文件的目录路径。")
    parser.add_argument("--size", type=float, default=0.5, 
                        help="点云渲染时的点大小 (默认: 0.5)。")

    args = parser.parse_args()
    
    pcd_directory = os.path.abspath(args.pcd)
    
    if not os.path.isdir(pcd_directory):
        print(f"❌ 错误: 输入目录 '{pcd_directory}' 不存在或不是一个目录。")
        sys.exit(1)

    try:
        browser = PCDBrowser(pcd_directory, args.size)
        browser.run()
    except Exception as e:
        print(f"❌ 发生致命错误: {e}")