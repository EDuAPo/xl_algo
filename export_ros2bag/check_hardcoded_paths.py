#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
路径硬编码检查工具

扫描项目中的Python文件，查找可能存在的硬编码路径，
帮助开发者完成路径配置迁移。
"""

import os
import re
from pathlib import Path


# 需要排除的文件和目录
EXCLUDE_PATTERNS = [
    '__pycache__',
    '.git',
    'build',
    'install',
    'log',
    'config_paths.py',  # 配置文件本身
    'setup_paths.py',   # 设置向导
    'check_hardcoded_paths.py',  # 本脚本自己
]

# 硬编码路径的匹配模式
PATH_PATTERNS = [
    # 绝对路径（Linux/macOS）
    (r'["\']/(home|media|mnt|data|opt|tmp|var)/[^"\']+["\']', '绝对路径 (Linux/macOS)'),
    # 绝对路径（Windows）
    (r'["\'][A-Z]:\\[^"\']+["\']', '绝对路径 (Windows)'),
    # 相对路径配置（可能需要检查）
    (r'DEFAULT_\w*(?:DIR|PATH|DIRECTORY)\s*=\s*["\'][^"\']+["\']', 'DEFAULT路径配置'),
    # 其他路径配置
    (r'(?:SOURCE|OUTPUT|ROOT)_(?:DIR|PATH|DIRECTORY)\s*=\s*["\'][^"\']+["\']', '路径配置变量'),
]


class PathChecker:
    def __init__(self, root_dir):
        self.root_dir = Path(root_dir)
        self.findings = []
    
    def should_skip(self, path):
        """判断是否应该跳过该路径"""
        path_str = str(path)
        for pattern in EXCLUDE_PATTERNS:
            if pattern in path_str:
                return True
        return False
    
    def check_file(self, file_path):
        """检查单个文件中的硬编码路径"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            file_findings = []
            
            for line_num, line in enumerate(lines, 1):
                # 跳过注释行
                if line.strip().startswith('#'):
                    continue
                
                # 检查各种路径模式
                for pattern, desc in PATH_PATTERNS:
                    matches = re.finditer(pattern, line)
                    for match in matches:
                        file_findings.append({
                            'line': line_num,
                            'content': line.strip(),
                            'match': match.group(),
                            'type': desc
                        })
            
            if file_findings:
                self.findings.append({
                    'file': file_path,
                    'findings': file_findings
                })
        
        except Exception as e:
            print(f"⚠️  读取文件失败 {file_path}: {e}")
    
    def scan_directory(self):
        """扫描整个目录"""
        print(f"🔍 开始扫描目录: {self.root_dir}")
        print(f"   排除模式: {', '.join(EXCLUDE_PATTERNS)}\n")
        
        py_files = list(self.root_dir.rglob('*.py'))
        total_files = len(py_files)
        
        print(f"   找到 {total_files} 个Python文件\n")
        
        for idx, py_file in enumerate(py_files, 1):
            if self.should_skip(py_file):
                continue
            
            # 显示进度
            print(f"\r   进度: {idx}/{total_files} - 检查 {py_file.name}", end='', flush=True)
            self.check_file(py_file)
        
        print("\n\n✅ 扫描完成！\n")
    
    def print_report(self):
        """打印检查报告"""
        if not self.findings:
            print("🎉 太棒了！未发现硬编码路径。")
            print("\n所有路径配置都已迁移到统一配置系统。")
            return
        
        print("="*80)
        print("📋 发现以下可能需要迁移的硬编码路径:")
        print("="*80)
        
        total_issues = 0
        
        for file_info in self.findings:
            file_path = file_info['file']
            findings = file_info['findings']
            
            print(f"\n📄 文件: {file_path.relative_to(self.root_dir)}")
            print(f"   发现 {len(findings)} 处可能的硬编码路径:\n")
            
            for finding in findings:
                total_issues += 1
                print(f"   行 {finding['line']:4d} | {finding['type']}")
                print(f"            | {finding['content'][:70]}")
                print(f"            | 匹配: {finding['match']}\n")
        
        print("="*80)
        print(f"📊 总计: 在 {len(self.findings)} 个文件中发现 {total_issues} 处可能的硬编码路径")
        print("="*80)
        
        print("\n💡 建议:")
        print("   1. 检查上述路径是否可以迁移到 config_paths.py")
        print("   2. 如果是配置项，使用 PathConfig 类获取路径")
        print("   3. 如果是示例代码或文档，可以保持不变")
        print("   4. 使用 'from config_paths import PathConfig' 导入配置")
        
        print("\n📖 示例迁移:")
        print("   # 迁移前")
        print("   SOURCE_DIR = '/media/xl/T7/1204/rosbag'")
        print("\n   # 迁移后")
        print("   from config_paths import PathConfig")
        print("   path_config = PathConfig()")
        print("   SOURCE_DIR = path_config.source_directory")
    
    def save_report(self, output_file='path_check_report.txt'):
        """保存报告到文件"""
        if not self.findings:
            return
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("硬编码路径检查报告\n")
            f.write("="*80 + "\n\n")
            
            for file_info in self.findings:
                file_path = file_info['file']
                findings = file_info['findings']
                
                f.write(f"文件: {file_path.relative_to(self.root_dir)}\n")
                f.write(f"发现 {len(findings)} 处:\n\n")
                
                for finding in findings:
                    f.write(f"  行 {finding['line']:4d} | {finding['type']}\n")
                    f.write(f"          | {finding['content']}\n")
                    f.write(f"          | 匹配: {finding['match']}\n\n")
                
                f.write("-"*80 + "\n\n")
        
        print(f"\n💾 报告已保存到: {output_file}")


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description='检查项目中的硬编码路径')
    parser.add_argument('--dir', type=str, default='.', 
                       help='要检查的目录（默认：当前目录）')
    parser.add_argument('--save', action='store_true',
                       help='保存报告到文件')
    
    args = parser.parse_args()
    
    # 创建检查器
    checker = PathChecker(args.dir)
    
    # 扫描目录
    checker.scan_directory()
    
    # 打印报告
    checker.print_report()
    
    # 保存报告
    if args.save:
        checker.save_report()


if __name__ == "__main__":
    main()
