#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
快速路径配置向导

帮助用户快速设置项目路径配置
"""

import os
import sys
from config_paths import PathConfig


def print_header(text):
    """打印标题"""
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60)


def print_step(step, text):
    """打印步骤"""
    print(f"\n【步骤 {step}】{text}")


def get_user_input(prompt, default=None):
    """获取用户输入"""
    if default:
        full_prompt = f"{prompt} [{default}]: "
    else:
        full_prompt = f"{prompt}: "
    
    user_input = input(full_prompt).strip()
    
    if not user_input and default:
        return default
    
    return user_input


def validate_directory(path, create_if_not_exist=False):
    """验证目录是否存在"""
    if os.path.exists(path):
        if os.path.isdir(path):
            return True, "目录存在 ✅"
        else:
            return False, "路径存在但不是目录 ❌"
    else:
        if create_if_not_exist:
            try:
                os.makedirs(path, exist_ok=True)
                return True, "目录已创建 ✅"
            except Exception as e:
                return False, f"创建目录失败: {e} ❌"
        else:
            return False, "目录不存在 ⚠️"


def main():
    """主函数"""
    print_header("🎯 ROS2 Bag 数据处理管道 - 路径配置向导")
    
    print("\n欢迎使用路径配置向导！")
    print("本向导将帮助您快速配置项目所需的所有路径。")
    
    # 检查是否已有配置
    config = PathConfig()
    config_file = config._config_file
    
    if os.path.exists(config_file):
        print(f"\n⚠️  检测到已存在配置文件: {config_file}")
        choice = get_user_input("是否重新配置？(y/n)", "n")
        if choice.lower() != 'y':
            print("\n已取消配置")
            config.print_config()
            return
    
    print("\n")
    print("提示：")
    print("  - 直接回车使用默认值")
    print("  - 输出目录如果不存在会自动创建")
    print("  - 源目录必须已存在")
    
    # 步骤1: 源数据目录
    print_step(1, "配置源数据目录（ROS2 Bag文件所在目录）")
    print(f"   默认值: {config.DEFAULT_SOURCE_DIRECTORY}")
    
    while True:
        source_dir = get_user_input("请输入源数据目录", config.DEFAULT_SOURCE_DIRECTORY)
        
        # 验证源目录必须存在
        valid, msg = validate_directory(source_dir, create_if_not_exist=False)
        print(f"   验证结果: {msg}")
        
        if valid:
            config.source_directory = source_dir
            break
        else:
            retry = get_user_input("   目录不存在，是否重新输入？(y/n)", "y")
            if retry.lower() != 'y':
                print("   已取消，使用默认值")
                config.source_directory = config.DEFAULT_SOURCE_DIRECTORY
                break
    
    # 步骤2: 筛选输出根目录
    print_step(2, "配置筛选输出根目录（筛选后的bag文件保存位置）")
    print(f"   默认值: {config.DEFAULT_OUTPUT_ROOT_DIRECTORY}")
    
    output_root_dir = get_user_input("请输入筛选输出根目录", config.DEFAULT_OUTPUT_ROOT_DIRECTORY)
    valid, msg = validate_directory(output_root_dir, create_if_not_exist=True)
    print(f"   验证结果: {msg}")
    config.output_root_directory = output_root_dir
    
    # 步骤3: 预处理主输出目录
    print_step(3, "配置预处理主输出目录（最终处理结果保存位置）")
    print(f"   默认值: {config.DEFAULT_MAIN_OUT}")
    
    main_out_dir = get_user_input("请输入预处理主输出目录", config.DEFAULT_MAIN_OUT)
    valid, msg = validate_directory(main_out_dir, create_if_not_exist=True)
    print(f"   验证结果: {msg}")
    config.main_out = main_out_dir
    
    # 步骤4: 移动记录目录
    print_step(4, "配置移动记录目录（用于记录移动的文件，便于恢复）")
    print(f"   提示: 通常与主输出目录相同")
    print(f"   默认值: {main_out_dir}")
    
    move_record_dir = get_user_input("请输入移动记录目录", main_out_dir)
    valid, msg = validate_directory(move_record_dir, create_if_not_exist=True)
    print(f"   验证结果: {msg}")
    config.move_record_dir = move_record_dir
    
    # 保存配置
    print_step(5, "保存配置")
    config.save_config()
    
    # 显示配置摘要
    print_header("✅ 配置完成")
    config.print_config()
    
    # 验证路径
    print("\n正在验证配置...")
    if config.validate_paths():
        print("\n🎉 所有配置已完成并验证通过！")
        print("\n现在您可以运行:")
        print("  python pipeline_batch.py --logtime 20251204_104208 --vehicle vehicle_000")
    else:
        print("\n⚠️  部分路径验证失败，请检查配置")
    
    print("\n提示:")
    print("  - 查看配置: python config_paths.py --show")
    print("  - 修改配置: python config_paths.py --set-source /new/path")
    print("  - 验证配置: python config_paths.py --validate")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n已取消配置")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n❌ 配置过程出错: {e}")
        sys.exit(1)
