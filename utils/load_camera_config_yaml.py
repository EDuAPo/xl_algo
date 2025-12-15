import yaml
from typing import Dict, Any
import os

def load_camera_configs_from_yaml(file_path: str) -> Dict[str, Any]:
    """
    从YAML文件加载相机配置并转换为字典格式
    
    Args:
        file_path: YAML文件路径
        
    Returns:
        包含相机配置的字典，格式与原始CAMERA_CONFIGS相同
    """
    # 检查文件是否存在
    if not os.path.exists(file_path):
        print(f"文件不存在: {file_path}")
        return {}
    
    try:
        # 读取YAML文件
        with open(file_path, 'r', encoding='utf-8') as file:
            camera_configs = yaml.safe_load(file)
        
        print(f"成功从 {file_path} 加载相机配置")
        return camera_configs
    
    except yaml.YAMLError as e:
        print(f"YAML解析错误: {e}")
        return {}
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
        return {}
    

if __name__ == "__main__":  
    # 测试加载函数
    test_file = "/home/shucdong/workspace/xl/export_ros2bag/utils/camera_config.yaml"  # 替换为实际的YAML文件路径
    configs = load_camera_configs_from_yaml(test_file)
    print(configs)