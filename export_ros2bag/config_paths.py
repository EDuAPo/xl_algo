#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
统一路径配置管理模块

本模块提供项目中所有路径的集中配置和管理，避免硬编码路径导致的维护问题。
所有路径配置都可以通过环境变量或配置文件覆盖，支持灵活的部署环境。

使用方式:
    from config_paths import PathConfig
    
    # 获取配置实例
    config = PathConfig()
    
    # 访问路径
    source_dir = config.source_directory
    output_dir = config.output_root_directory
    
    # 或者使用类方法直接获取
    source_dir = PathConfig.get_source_directory()
"""

import os
import json
from pathlib import Path
from typing import Dict, Optional


class PathConfig:
    """统一路径配置类"""
    
    # ==================== 核心项目路径 ====================
    # 项目根目录（自动检测）
    PROJECT_ROOT = Path(__file__).resolve().parent
    
    # ==================== 默认数据路径配置 ====================
    # 这些是默认值，可以通过环境变量或配置文件覆盖
    
    # ROS2 Bag源数据目录（输入）
    DEFAULT_SOURCE_DIRECTORY = "/media/xl/T7/1204/rosbag2_2025_12_04-10_42_08/"
    
    # 筛选后bag输出根目录（中间结果）
    DEFAULT_OUTPUT_ROOT_DIRECTORY = "/media/xl/T7/1204_out1/"
    
    # 预处理主输出目录（最终结果）
    DEFAULT_MAIN_OUT = "/media/xl/T7/1204_out/"
    
    # 移动记录保存目录
    DEFAULT_MOVE_RECORD_DIR = "/media/xl/T7/1204_out/"
    
    # ==================== 脚本路径（相对于项目根目录）====================
    FILTER_SCRIPT = "filter_rosbag.py"
    RUN_EXPORT_SCRIPT = "run_export.py"
    CHECK_COMPRESS_SCRIPT = "check_and_compress.py"
    EXPORT_CAMERA_SCRIPT = "export_camera.py"
    EXPORT_LIDAR_SCRIPT = "export_lidar.py"
    EXPORT_IMU_SCRIPT = "export_imu/export_imu.py"
    UNDISTORTION_SCRIPT = "undistortion/undistortion.py"
    EXTRACT_SAMPLE_SCRIPT = "extract_sample_undistorted.py"
    
    # ==================== 配置文件路径 ====================
    TIME_PERIODS_YAML = "time_peridos.yaml"
    CAMERA_CONFIG_YAML = "utils/camera_config.yaml"
    
    # ==================== 参数目录路径 ====================
    UNDISTORTION_PARAMS_DIR = "undistortion/intrinsic_param"
    CAMERA_INTRI_DIR = "project_lidar_to_camera/intri"
    LIDAR_EXTRINIC_DIR = "project_lidar_to_camera/lidar_extrinic"
    
    # ==================== ROS2 相关路径 ====================
    IMU_MSGS_INSTALL_PATH = "export_imu/imu_msgs/install"
    
    # ==================== 环境变量键名 ====================
    ENV_SOURCE_DIR = "XL_SOURCE_DIRECTORY"
    ENV_OUTPUT_ROOT = "XL_OUTPUT_ROOT_DIRECTORY"
    ENV_MAIN_OUT = "XL_MAIN_OUT_DIRECTORY"
    ENV_MOVE_RECORD_DIR = "XL_MOVE_RECORD_DIRECTORY"
    
    # ==================== 配置文件路径 ====================
    CONFIG_FILE_NAME = "paths_config.json"
    
    def __init__(self, config_file: Optional[str] = None):
        """
        初始化路径配置
        
        优先级顺序（从高到低）：
        1. 环境变量
        2. 配置文件
        3. 默认值
        
        Args:
            config_file: 自定义配置文件路径（可选）
        """
        self._config_file = config_file or self.PROJECT_ROOT / self.CONFIG_FILE_NAME
        self._load_config()
    
    def _load_config(self):
        """加载配置（优先级：环境变量 > 配置文件 > 默认值）"""
        # 先尝试从配置文件加载
        file_config = {}
        if os.path.exists(self._config_file):
            try:
                with open(self._config_file, 'r', encoding='utf-8') as f:
                    file_config = json.load(f)
            except Exception as e:
                print(f"警告: 读取配置文件失败 {self._config_file}: {e}")
        
        # 按优先级设置路径（环境变量 > 配置文件 > 默认值）
        self.source_directory = (
            os.environ.get(self.ENV_SOURCE_DIR) or 
            file_config.get('source_directory') or 
            self.DEFAULT_SOURCE_DIRECTORY
        )
        
        self.output_root_directory = (
            os.environ.get(self.ENV_OUTPUT_ROOT) or 
            file_config.get('output_root_directory') or 
            self.DEFAULT_OUTPUT_ROOT_DIRECTORY
        )
        
        self.main_out = (
            os.environ.get(self.ENV_MAIN_OUT) or 
            file_config.get('main_out') or 
            self.DEFAULT_MAIN_OUT
        )
        
        self.move_record_dir = (
            os.environ.get(self.ENV_MOVE_RECORD_DIR) or 
            file_config.get('move_record_dir') or 
            self.DEFAULT_MOVE_RECORD_DIR
        )
    
    # ==================== 脚本路径获取方法 ====================
    
    def get_script_path(self, script_name: str) -> str:
        """获取脚本的绝对路径"""
        return str(self.PROJECT_ROOT / script_name)
    
    @property
    def filter_script_path(self) -> str:
        """筛选脚本路径"""
        return self.get_script_path(self.FILTER_SCRIPT)
    
    @property
    def run_export_script_path(self) -> str:
        """预处理脚本路径"""
        return self.get_script_path(self.RUN_EXPORT_SCRIPT)
    
    @property
    def check_compress_script_path(self) -> str:
        """检查压缩脚本路径"""
        return self.get_script_path(self.CHECK_COMPRESS_SCRIPT)
    
    @property
    def export_camera_script_path(self) -> str:
        """相机导出脚本路径"""
        return self.get_script_path(self.EXPORT_CAMERA_SCRIPT)
    
    @property
    def export_lidar_script_path(self) -> str:
        """激光雷达导出脚本路径"""
        return self.get_script_path(self.EXPORT_LIDAR_SCRIPT)
    
    @property
    def export_imu_script_path(self) -> str:
        """IMU导出脚本路径"""
        return self.get_script_path(self.EXPORT_IMU_SCRIPT)
    
    @property
    def undistortion_script_path(self) -> str:
        """去畸变脚本路径"""
        return self.get_script_path(self.UNDISTORTION_SCRIPT)
    
    @property
    def extract_sample_script_path(self) -> str:
        """提取样本脚本路径"""
        return self.get_script_path(self.EXTRACT_SAMPLE_SCRIPT)
    
    # ==================== 配置文件路径获取方法 ====================
    
    @property
    def time_periods_yaml_path(self) -> str:
        """时间段配置YAML路径"""
        return self.get_script_path(self.TIME_PERIODS_YAML)
    
    @property
    def camera_config_yaml_path(self) -> str:
        """相机配置YAML路径"""
        return self.get_script_path(self.CAMERA_CONFIG_YAML)
    
    # ==================== 参数目录路径获取方法 ====================
    
    @property
    def undistortion_params_dir_path(self) -> str:
        """去畸变参数目录路径"""
        return self.get_script_path(self.UNDISTORTION_PARAMS_DIR)
    
    @property
    def camera_intri_dir_path(self) -> str:
        """相机内参目录路径"""
        return self.get_script_path(self.CAMERA_INTRI_DIR)
    
    @property
    def lidar_extrinic_dir_path(self) -> str:
        """激光雷达外参目录路径"""
        return self.get_script_path(self.LIDAR_EXTRINIC_DIR)
    
    # ==================== ROS2 路径获取方法 ====================
    
    @property
    def imu_msgs_install_path(self) -> str:
        """IMU消息安装路径"""
        return self.get_script_path(self.IMU_MSGS_INSTALL_PATH)
    
    # ==================== 工具方法 ====================
    
    def save_config(self):
        """保存当前配置到配置文件"""
        config_data = {
            'source_directory': self.source_directory,
            'output_root_directory': self.output_root_directory,
            'main_out': self.main_out,
            'move_record_dir': self.move_record_dir,
        }
        
        try:
            with open(self._config_file, 'w', encoding='utf-8') as f:
                json.dump(config_data, f, indent=2, ensure_ascii=False)
            print(f"✅ 配置已保存到: {self._config_file}")
        except Exception as e:
            print(f"❌ 保存配置文件失败: {e}")
    
    def print_config(self):
        """打印当前配置信息"""
        print("\n" + "="*60)
        print("📋 当前路径配置")
        print("="*60)
        print(f"项目根目录: {self.PROJECT_ROOT}")
        print(f"\n数据目录:")
        print(f"  源数据目录: {self.source_directory}")
        print(f"  筛选输出目录: {self.output_root_directory}")
        print(f"  预处理输出目录: {self.main_out}")
        print(f"  移动记录目录: {self.move_record_dir}")
        print(f"\n配置文件:")
        print(f"  配置文件路径: {self._config_file}")
        print(f"  时间段配置: {self.time_periods_yaml_path}")
        print("="*60 + "\n")
    
    def validate_paths(self) -> bool:
        """验证关键路径是否存在"""
        errors = []
        
        # 检查脚本是否存在
        scripts = [
            ('筛选脚本', self.filter_script_path),
            ('预处理脚本', self.run_export_script_path),
            ('相机导出脚本', self.export_camera_script_path),
            ('激光雷达导出脚本', self.export_lidar_script_path),
            ('IMU导出脚本', self.export_imu_script_path),
            ('去畸变脚本', self.undistortion_script_path),
            ('提取样本脚本', self.extract_sample_script_path),
        ]
        
        for name, path in scripts:
            if not os.path.exists(path):
                errors.append(f"❌ {name}不存在: {path}")
        
        # 检查数据目录
        if not os.path.exists(self.source_directory):
            errors.append(f"❌ 源数据目录不存在: {self.source_directory}")
        
        if errors:
            print("\n路径验证失败:")
            for error in errors:
                print(error)
            return False
        
        print("✅ 所有关键路径验证通过")
        return True
    
    # ==================== 类方法（便捷访问）====================
    
    @classmethod
    def get_instance(cls, config_file: Optional[str] = None) -> 'PathConfig':
        """获取PathConfig实例（单例模式）"""
        if not hasattr(cls, '_instance'):
            cls._instance = cls(config_file)
        return cls._instance
    
    @classmethod
    def get_source_directory(cls) -> str:
        """快速获取源目录"""
        return cls.get_instance().source_directory
    
    @classmethod
    def get_output_root_directory(cls) -> str:
        """快速获取输出根目录"""
        return cls.get_instance().output_root_directory
    
    @classmethod
    def get_main_out(cls) -> str:
        """快速获取主输出目录"""
        return cls.get_instance().main_out


def create_default_config():
    """创建默认配置文件"""
    config = PathConfig()
    config.save_config()
    config.print_config()


def main():
    """命令行工具：配置路径管理"""
    import argparse
    
    parser = argparse.ArgumentParser(description="路径配置管理工具")
    parser.add_argument('--init', action='store_true', help='创建默认配置文件')
    parser.add_argument('--show', action='store_true', help='显示当前配置')
    parser.add_argument('--validate', action='store_true', help='验证路径是否存在')
    parser.add_argument('--set-source', type=str, help='设置源数据目录')
    parser.add_argument('--set-output', type=str, help='设置输出根目录')
    parser.add_argument('--set-main-out', type=str, help='设置主输出目录')
    
    args = parser.parse_args()
    
    config = PathConfig()
    
    if args.init:
        create_default_config()
        return
    
    # 设置路径
    if args.set_source:
        config.source_directory = args.set_source
        config.save_config()
        print(f"✅ 源数据目录已设置为: {args.set_source}")
    
    if args.set_output:
        config.output_root_directory = args.set_output
        config.save_config()
        print(f"✅ 输出根目录已设置为: {args.set_output}")
    
    if args.set_main_out:
        config.main_out = args.set_main_out
        config.save_config()
        print(f"✅ 主输出目录已设置为: {args.set_main_out}")
    
    if args.show:
        config.print_config()
    
    if args.validate:
        config.validate_paths()
    
    # 如果没有任何参数，显示帮助
    if not any(vars(args).values()):
        parser.print_help()


if __name__ == "__main__":
    main()
