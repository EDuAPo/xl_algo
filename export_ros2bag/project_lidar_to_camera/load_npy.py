import numpy as np
import argparse
import sys
import os

def load_and_print_npy(file_path: str):
    """
    加载 .npy 文件，并打印其内容、类型、形状和维度。
    
    Args:
        file_path (str): .npy 文件的路径。
    """
    print(f"--- 🚀 正在解析文件: {file_path} ---")

    if not os.path.exists(file_path):
        print(f"❌ 错误：文件未找到 at {file_path}")
        return

    try:
        # 使用 numpy.load 加载文件
        params = np.load(file_path, allow_pickle=True)
        
        print("✅ 文件加载成功！")
        
        print("\n--- 文件内容详情 ---")
        
        # 1. 打印数据类型 (dtype)
        if hasattr(params, 'dtype'):
            print(f"1. 数据类型 (dtype): {params.dtype}")
        
        # 2. 打印形状 (shape)
        if hasattr(params, 'shape'):
            print(f"2. 形状 (shape): {params.shape}")
        
        # 3. 打印维度 (ndim)
        if hasattr(params, 'ndim'):
            print(f"3. 维度 (ndim): {params.ndim}")
            
        # 4. 打印完整内容
        print("\n4. 完整内容 (params):")
        # 设置打印选项，确保能完整显示数组内容，而不是省略号
        np.set_printoptions(threshold=sys.maxsize, linewidth=150)
        print(params)
        
        # 5. 如果内容是字典或列表（allow_pickle=True），可以打印其结构
        if isinstance(params, np.ndarray) and params.dtype == object and params.ndim == 0:
            # 这是一个包含单个非数组对象的零维数组（通常是字典或列表）
            print("\n5. 内部对象类型:")
            print(type(params.item()))
            print("\n6. 展开内部对象内容:")
            # 使用 .item() 获取实际存储的对象
            print(params.item())

        print("\n--- 解析完成 ---")
        
    except ValueError:
        print("❌ 错误：尝试加载文件失败。确保这是一个有效的 NumPy .npy 文件。")
    except Exception as e:
        print(f"❌ 发生未知错误: {e}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="解析并打印 NumPy .npy 文件中的内容。")
    # 添加一个必需的位置参数来指定文件路径
    parser.add_argument("npy_file_path", type=str, 
                        help="NumPy .npy 文件的路径，例如: camera_params.npy")
    
    args = parser.parse_args()

    # 调用主功能函数
    load_and_print_npy(args.npy_file_path)