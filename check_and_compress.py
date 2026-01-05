import os
import json
import zipfile
import re
import shutil
import argparse
from datetime import datetime, timedelta
from pathlib import Path
import platform

class FolderCompressor:
    def __init__(self, root_dir):
        self.root_dir = Path(root_dir)
        # 配置项 - 请根据实际情况修改
        self.required_json_files = ['sensor_config_combined_latest.json', 'ins.json', 'sample.json']  # 必需的JSON文件列表
        self.folder_groups = [
            ['camera_cam_3M_front/scale_0.20','camera_cam_3M_rear/scale_0.20','camera_cam_3M_right/scale_0.20','camera_cam_3M_left/scale_0.20'],     # 这些文件夹内的文件数量必须相同
            ['iv_points_front_left/pcd_binary', 'iv_points_front_right/pcd_binary', 'iv_points_rear_left/pcd_binary','iv_points_front_mid/pcd_binary','iv_points_rear_right/pcd_binary', 'iv_points_left_mid/pcd_binary', 'iv_points_right_mid/pcd_binary'],  # 这些文件夹内的文件数量必须相同
            ['combined_scales']                   # 单个文件夹也要检查不为空
        ]
        self.time_sensitive_folders = ['camera_cam_3M_front/scale_0.20','camera_cam_3M_rear/scale_0.20','camera_cam_3M_right/scale_0.20','camera_cam_3M_left/scale_0.20','iv_points_front_left/pcd_binary', 'iv_points_front_right/pcd_binary', 'iv_points_rear_left/pcd_binary','iv_points_front_mid/pcd_binary','iv_points_rear_right/pcd_binary', 'iv_points_left_mid/pcd_binary', 'iv_points_right_mid/pcd_binary']  # 包含时间信息的文件夹
        self.min_zip_size_gb = 4  # 最小压缩包大小（GB）
        self.min_zip_size_bytes = self.min_zip_size_gb * 1024 * 1024 * 1024  # 转换为字节
        self.keep_folder_name = "undistorted"  # 需要保留的文件夹名
        self.required_free_space_gb = 100  # 所需最小剩余空间（GB）
        self.required_free_space_bytes = self.required_free_space_gb * 1024 * 1024 * 1024  # 转换为字节
    
    def get_free_disk_space(self, path):
        """获取指定路径所在磁盘的剩余空间（字节）"""
        try:
            if platform.system() == 'Windows':
                # Windows系统
                import ctypes
                free_bytes = ctypes.c_ulonglong(0)
                total_bytes = ctypes.c_ulonglong(0)
                # 获取磁盘空间信息
                ctypes.windll.kernel32.GetDiskFreeSpaceExW(
                    ctypes.c_wchar_p(str(path)),
                    None,
                    ctypes.pointer(total_bytes),
                    ctypes.pointer(free_bytes)
                )
                return free_bytes.value
            else:
                # Linux/macOS系统
                statvfs = os.statvfs(str(path))
                # 计算剩余空间：块大小 * 可用块数
                return statvfs.f_frsize * statvfs.f_bavail
        except Exception as e:
            print(f"  ❌ 获取磁盘空间失败: {e}")
            return -1
    
    def check_disk_space(self):
        """检查目标目录的剩余空间是否满足要求"""
        print(f"\n📊 正在检查磁盘空间...")
        free_space = self.get_free_disk_space(self.root_dir)
        
        if free_space < 0:
            print(f"  ❌ 无法获取磁盘空间信息，程序终止")
            return False
        
        # 格式化空间大小显示
        free_space_gb = free_space / (1024 * 1024 * 1024)
        
        print(f"  📈 磁盘剩余空间: {free_space_gb:.2f} GB")
        print(f"  📋 所需最小空间: {self.required_free_space_gb} GB")
        
        if free_space >= self.required_free_space_bytes:
            print(f"  ✅ 磁盘空间满足要求")
            return True
        else:
            print(f"  ❌ 磁盘空间不足！")
            print(f"     剩余: {free_space_gb:.2f} GB, 所需: {self.required_free_space_gb} GB")
            print(f"     程序将立即终止，避免压缩失败")
            return False
    
    def get_undistorted_folder(self, target_folder_path):
        """获取undistorted文件夹路径，不存在则返回None"""
        if target_folder_path.name == self.keep_folder_name:
            if target_folder_path.exists() and target_folder_path.is_dir():
                return target_folder_path
            else:
                print(f"  ❌ 文件夹不存在: {target_folder_path}")
                return None

        undistorted_folder = target_folder_path / self.keep_folder_name
        if not undistorted_folder.exists() or not undistorted_folder.is_dir():
            print(f"  ❌ 未找到 '{self.keep_folder_name}' 文件夹: {undistorted_folder}")
            return None
        return undistorted_folder
    
    def find_json_files(self, undistorted_folder):
        """在undistorted文件夹内递归查找JSON文件"""
        found_jsons = {}
        for json_file in self.required_json_files:
            # 递归查找JSON文件（在undistorted目录下）
            for file_path in undistorted_folder.rglob(f"*{json_file}"):
                if file_path.name == json_file:
                    found_jsons[json_file] = file_path
                    break  # 找到第一个匹配的就停止
        
        return found_jsons
    
    def check_json_files(self, target_folder_path):
        """检查undistorted文件夹内的JSON文件是否存在且不为空"""
        # 先获取undistorted文件夹
        undistorted_folder = self.get_undistorted_folder(target_folder_path)
        if not undistorted_folder:
            return False
        
        print(f"  🔍 正在检查 '{self.keep_folder_name}' 文件夹内的JSON文件...")
        found_jsons = self.find_json_files(undistorted_folder)
        
        for json_file in self.required_json_files:
            if json_file not in found_jsons:
                print(f"  ❌ 缺少JSON文件: {json_file}（在 {self.keep_folder_name} 目录下）")
                return False
            
            json_path = found_jsons[json_file]
            # 检查JSON文件是否为空
            if json_path.stat().st_size == 0:
                print(f"  ❌ JSON文件为空: {json_file}（路径: {json_path}）")
                return False
            
        
        print(f"  ✅ JSON文件检查通过（基于 {self.keep_folder_name} 目录）")
        return True
    
    def check_folder_structure(self, target_folder_path):
        """检查undistorted文件夹内的结构和文件数量"""
        # 先获取undistorted文件夹
        undistorted_folder = self.get_undistorted_folder(target_folder_path)
        if not undistorted_folder:
            return False
        
        print(f"  🔍 正在检查 '{self.keep_folder_name}' 文件夹内的结构...")
        all_folders_exist = True
        
        # 检查所有配置的文件夹是否在undistorted目录下存在
        for folder_group in self.folder_groups:
            for folder_path_str in folder_group:
                # 处理嵌套文件夹路径（相对于undistorted文件夹）
                folder_path = undistorted_folder / folder_path_str
                if not folder_path.exists() or not folder_path.is_dir():
                    print(f"  ❌ 文件夹不存在: {self.keep_folder_name}/{folder_path_str}")
                    all_folders_exist = False
        
        if not all_folders_exist:
            return False
        
        # 检查文件夹文件数量（基于undistorted目录下的路径）
        for folder_group in self.folder_groups:
            if len(folder_group) > 1:
                file_counts = []
                for folder_path_str in folder_group:
                    folder_path = undistorted_folder / folder_path_str
                    file_count = len([f for f in folder_path.iterdir() if f.is_file()])
                    file_counts.append(file_count)
                
                # 检查同一组内文件夹文件数量是否相同
                if len(set(file_counts)) != 1:
                    print(f"  ❌ 文件夹组 {folder_group} 文件数量不一致: {dict(zip(folder_group, file_counts))}")
            
            else:  # 单个文件夹检查是否为空
                folder_path_str = folder_group[0]
                folder_path = undistorted_folder / folder_path_str
                file_count = len([f for f in folder_path.iterdir() if f.is_file()])
                if file_count == 0:
                    print(f"  ❌ 文件夹为空: {self.keep_folder_name}/{folder_path_str}")
                    return False
        
        print(f"  ✅ 文件夹结构检查通过（基于 {self.keep_folder_name} 目录）")
        return True
    
    def extract_time_from_filename(self, filename):
        """从文件名中提取时分秒字符串，返回格式为 HH:MM:SS，失败返回 None"""
        # 优先匹配：文件名开头的 YYYYMMDD_HHMMSS 格式
        combined_pattern = r'^(\d{8})_(\d{6})'
        match = re.search(combined_pattern, str(filename))
        if match:
            hms_str = match.group(2)  # 提取 6 位时分秒（HHMMSS）
            try:
                # 验证是否为有效时分秒
                datetime.strptime(hms_str, '%H%M%S')
                return f"{hms_str[:2]}:{hms_str[2:4]}:{hms_str[4:6]}"
            except ValueError:
                print(f"  ⚠️  警告：文件名 {filename} 中的时分秒 {hms_str} 格式无效")
                return None
        
        # 备用匹配：仅匹配 6 位数字（HHMMSS）
        hms_pattern = r'(\d{6})'
        match = re.search(hms_pattern, str(filename))
        if match:
            hms_str = match.group(1)
            try:
                datetime.strptime(hms_str, '%H%M%S')
                return f"{hms_str[:2]}:{hms_str[2:4]}:{hms_str[4:6]}"
            except ValueError:
                print(f"  ⚠️  警告：文件名 {filename} 中的时分秒 {hms_str} 格式无效")
                return None
        
        return None

    
    def parse_folder_time_range(self, folder_name):
        """从文件夹名解析时间范围（支持 HHMMSS_HHMMSS 格式）"""
        pattern = r'^(\d{6})_(\d{6})$'
        match = re.search(pattern, folder_name)
        if not match:
            return None, None
        
        start_str, end_str = match.groups()
        try:
            # 解析为时间对象并格式化为 HH:MM:SS
            start_time = datetime.strptime(start_str, '%H%M%S').strftime('%H:%M:%S')
            end_time = datetime.strptime(end_str, '%H%M%S').strftime('%H:%M:%S')
            return start_time, end_time
        except ValueError as e:
            print(f"  ⚠️  无法解析文件夹 {folder_name} 的时间范围: {e}")
            return None, None
    
    def check_time_consistency(self, target_folder_path, folder_name):
        """检查undistorted文件夹内的时间一致性"""
        # 先获取undistorted文件夹
        undistorted_folder = self.get_undistorted_folder(target_folder_path)
        if not undistorted_folder:
            return False
        
        folder_start, folder_end = self.parse_folder_time_range(folder_name)
        if not folder_start or not folder_end:
            print(f"  ❌ 无法解析文件夹时间范围（需符合 HHMMSS_HHMMSS 格式）: {folder_name}")
            return False
        
        print(f"  🕒 文件夹时间范围: {folder_start} - {folder_end}")
        print(f"  🔍 正在检查 '{self.keep_folder_name}' 文件夹内的时间一致性...")
        all_time_folders_valid = True
        time_tolerance = timedelta(seconds=3)
        fmt = "%H:%M:%S"
        
        for time_folder_path_str in self.time_sensitive_folders:
            # 时间敏感文件夹路径相对于undistorted文件夹
            time_folder_path = undistorted_folder / time_folder_path_str
            if not time_folder_path.exists():
                print(f"  ⚠️  时间敏感文件夹不存在: {self.keep_folder_name}/{time_folder_path_str}")
                continue
            
            # 获取文件夹内所有非json、非npy文件并按文件名排序
            files = sorted([f for f in time_folder_path.iterdir() if f.is_file() 
                          and not (f.name.lower().endswith('.json') or f.name.lower().endswith('.npy'))])
            if not files:
                print(f"  ❌ 时间敏感文件夹为空: {self.keep_folder_name}/{time_folder_path_str}")
                all_time_folders_valid = False
                continue
            
            # 检查第一个文件的时间
            first_file_time = self.extract_time_from_filename(files[0].name)
            if not first_file_time:
                print(f"  ❌ 无法从文件提取时间: {files[0].name}")
                all_time_folders_valid = False
                continue
            
            # 检查最后一个文件的时间
            last_file_time = self.extract_time_from_filename(files[-1].name)
            if not last_file_time:
                print(f"  ❌ 无法从文件提取时间: {files[-1].name}")
                all_time_folders_valid = False
                continue
            
            # 转换为datetime对象进行比较
            folder_start_dt = datetime.strptime(folder_start, fmt)
            folder_end_dt = datetime.strptime(folder_end, fmt)
            file_start_dt = datetime.strptime(first_file_time, fmt)
            file_end_dt = datetime.strptime(last_file_time, fmt)
            
            # 检查时间差
            if abs(file_start_dt - folder_start_dt) > time_tolerance:
                print(f"  ❌ 起始时间不匹配: {self.keep_folder_name}/{time_folder_path_str}")
                print(f"     文件夹起始: {folder_start}, 文件起始: {first_file_time}")
                all_time_folders_valid = False
            
            if abs(file_end_dt - folder_end_dt) > time_tolerance:
                print(f"  ❌ 结束时间不匹配: {self.keep_folder_name}/{time_folder_path_str}")
                print(f"     文件夹结束: {folder_end}, 文件结束: {last_file_time}")
                all_time_folders_valid = False
        
        if all_time_folders_valid:
            print(f"  ✅ 时间一致性检查通过（基于 {self.keep_folder_name} 目录）")
        return all_time_folders_valid
    
    def format_file_size(self, size_bytes):
        """格式化文件大小（B/KB/MB/GB）"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.2f} TB"
    
    def clean_folder_before_compress(self, target_folder_path):
        """清理文件夹：直接删除除指定保留文件夹外的所有内容（无确认）"""
        print(f"  开始清理文件夹: {target_folder_path.name}")
        print(f"  仅保留 '{self.keep_folder_name}' 文件夹，自动删除其他所有内容")
        
        # 先检查是否存在要保留的文件夹
        keep_folder = target_folder_path / self.keep_folder_name
        if not keep_folder.exists() or not keep_folder.is_dir():
            print(f"  ⚠️  警告：未找到 '{self.keep_folder_name}' 文件夹，将删除所有内容！")
        
        # 列出所有要删除的内容（不包括保留文件夹）
        items_to_delete = []
        for item in target_folder_path.iterdir():
            if item.name != self.keep_folder_name:
                items_to_delete.append(item)
        
        if not items_to_delete:
            print(f"  ✅ 无需清理：文件夹内仅包含 '{self.keep_folder_name}' 文件夹")
            return True
        
        # 显示要删除的项目数量
        print(f"  📋 正在删除 {len(items_to_delete)} 个项目...")
        
        # 执行删除操作
        deleted_count = 0
        failed_items = []
        for item in items_to_delete:
            try:
                if item.is_file():
                    item.unlink()  # 删除文件
                else:
                    shutil.rmtree(item)  # 删除文件夹及其内容
                deleted_count += 1
            except Exception as e:
                failed_items.append(f"{item.name}: {str(e)}")
        
        # 输出删除结果
        print(f"  ✅ 清理完成：成功删除 {deleted_count} 个项目")
        if failed_items:
            print(f"  ⚠️  有 {len(failed_items)} 个项目删除失败：")
            for item in failed_items:
                print(f"     - {item}")
        
        # 最后检查保留文件夹状态
        if keep_folder.exists() and keep_folder.is_dir():
            keep_folder_size = sum(f.stat().st_size for f in keep_folder.rglob('*') if f.is_file())
            if keep_folder_size == 0:
                print(f"  ⚠️  警告：保留的 '{self.keep_folder_name}' 文件夹为空")
            return True
        else:
            print(f"  ❌ 错误：保留的 '{self.keep_folder_name}' 文件夹不存在或已被删除")
            return False
    
    def compress_folder(self, target_folder_path, output_path=None):
        """压缩文件夹，并检查压缩包大小"""
        # 获取当前日期
        current_date = datetime.now().strftime('%Y%m%d')
        
        if output_path:
            zip_path = Path(output_path)
            zip_filename = zip_path.name
        else:
            # 压缩包保存到root_dir下，添加日期前缀
            zip_filename = f"{current_date}_{target_folder_path.name}.zip"
            zip_path = self.root_dir / zip_filename
        
        # 如果压缩包已存在，直接覆盖（无需确认）
        if zip_path.exists():
            print(f"  ⚠️  压缩包 {zip_filename} 已存在，将直接覆盖")
            zip_path.unlink()  # 删除已存在的压缩包
        
        try:
            print(f"  📦 开始压缩文件夹（仅包含 '{self.keep_folder_name}' 目录）...")
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(target_folder_path):
                    for file in files:
                        file_path = Path(root) / file
                        # 在ZIP文件中保持相对路径（相对于root_dir）
                        try:
                            arcname = file_path.relative_to(self.root_dir)
                        except ValueError:
                            # 如果不在root_dir下（例如单文件夹模式），则相对于target_folder_path的父目录
                            arcname = file_path.relative_to(target_folder_path.parent)
                            
                        zipf.write(file_path, arcname)
            
            # 检查压缩包大小
            zip_size_bytes = zip_path.stat().st_size
            zip_size_formatted = self.format_file_size(zip_size_bytes)
            
            print(f"  ✅ 压缩完成: {zip_filename}")
            print(f"  📊 压缩包大小: {zip_size_formatted}")
            
            # 如果小于最小配置大小，给出警告
            if zip_size_bytes < self.min_zip_size_bytes:
                print(f"  ⚠️  警告: 压缩包大小小于 {self.min_zip_size_gb}GB，可能存在数据不完整！")
            
            return True
        except Exception as e:
            print(f"  ❌ 压缩失败: {e}")
            # 如果压缩失败且文件已创建，删除不完整的压缩包
            if zip_path.exists():
                zip_path.unlink()
            return False
            # 如果压缩失败且文件已创建，删除不完整的压缩包
            if zip_path.exists():
                zip_path.unlink()
            return False
            if zip_path.exists():
                zip_path.unlink()
            return False
    
    def is_time_format_folder(self, folder_name):
        """判断文件夹名是否为时间格式（HHMMSS_HHMMSS）"""
        pattern = r'^\d{6}_\d{6}$'
        return bool(re.match(pattern, folder_name))
    
    def process_single_undistorted_folder(self, undistorted_path, compress_path):
        """处理单个undistorted文件夹（Pipeline模式）"""
        target_folder = Path(undistorted_path)
        print(f"\n📂 正在处理单个文件夹: {target_folder}")
        print("-" * 50)
        
        # 检查磁盘空间 (检查压缩包所在目录)
        compress_dir = Path(compress_path).parent
        if not compress_dir.exists():
            compress_dir.mkdir(parents=True, exist_ok=True)
            
        print(f"\n📊 正在检查磁盘空间 (目标: {compress_dir})...")
        free_space = self.get_free_disk_space(compress_dir)
        if free_space >= 0:
            free_space_gb = free_space / (1024 * 1024 * 1024)
            print(f"  📈 磁盘剩余空间: {free_space_gb:.2f} GB")
            if free_space < self.required_free_space_bytes:
                print(f"  ❌ 磁盘空间不足！所需: {self.required_free_space_gb} GB")
                return False
        
        # 执行检查
        checks_passed = True
        
        # 检查1: JSON文件
        if not self.check_json_files(target_folder):
            checks_passed = False
        
        # 检查2: 文件夹结构
        if not self.check_folder_structure(target_folder):
            checks_passed = False
            
        if checks_passed:
            print(f" 所有检查通过，开始压缩...")
            # 注意：Pipeline模式下不执行 clean_folder_before_compress，由Pipeline脚本负责清理
            
            if self.compress_folder(target_folder, output_path=compress_path):
                return True
        else:
            print(f"  ❌ 检查未通过，跳过压缩")
            
        return False

    def process_all_target_folders(self):
        """处理root_dir下所有时间格式的子文件夹"""
        # 验证根目录是否存在
        if not self.root_dir.exists():
            print(f"❌ 错误: 根目录不存在: {self.root_dir}")
            return
        
        # 查找所有时间格式的子文件夹（直接子目录）
        target_folders = [f for f in self.root_dir.iterdir() 
                        if f.is_dir() and self.is_time_format_folder(f.name)]
        
        if not target_folders:
            print(f"在 {self.root_dir} 中未找到符合格式的时间文件夹（需为 HHMMSS_HHMMSS 格式）")
            return
        
        print(f"找到 {len(target_folders)} 个需要处理的时间文件夹")
        
        successful_compressions = 0
        
        for idx, target_folder in enumerate(target_folders, 1):
            print(f"\n📂 正在处理 [{idx}/{len(target_folders)}]: {target_folder.name}")
            print("-" * 50)
            
            # 处理每个文件夹前先检查磁盘空间
            if not self.check_disk_space():
                # 空间不足，直接终止程序
                print(f"\n❌ 磁盘空间不足，程序终止！")
                print(f"已成功处理 {successful_compressions}/{idx-1} 个文件夹")
                return
            
            # 执行所有检查（均基于undistorted目录）
            checks_passed = True
            
            # 检查1: JSON文件（undistorted目录下）
            if not self.check_json_files(target_folder):
                checks_passed = False
            
            # 检查2: 文件夹结构（undistorted目录下）
            if not self.check_folder_structure(target_folder):
                checks_passed = False
            
            # 检查3: 时间一致性（undistorted目录下）
            # if not self.check_time_consistency(target_folder, target_folder.name):
            #     checks_passed = False
            
            # 如果所有检查通过，执行清理然后压缩
            if checks_passed:
                print(f" 所有检查通过，开始清理文件夹...")
                # 清理文件夹（无确认）
                if not self.clean_folder_before_compress(target_folder):
                    print(f"  ❌ 清理失败，跳过压缩")
                    continue
                
                # 清理成功后进行压缩
                if self.compress_folder(target_folder):
                    successful_compressions += 1
            else:
                print(f"  ❌ 检查未通过，跳过压缩")
            print("-" * 50)
        
        print(f"\n" + "="*60)
        print(f"📊 处理完成! 成功压缩 {successful_compressions}/{len(target_folders)} 个文件夹")

def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="文件夹批量压缩工具")
    parser.add_argument("--undistorted-path", type=str, help="单个undistorted文件夹路径")
    parser.add_argument("--compress-path", type=str, help="输出压缩包路径")
    parser.add_argument("--compress-format", type=str, default="zip", help="压缩格式")
    parser.add_argument("--period", type=str, help="时间段标识")
    
    args, unknown = parser.parse_known_args()
    
    if args.undistorted_path and args.compress_path:
        # Pipeline模式
        print("🚀 启动 Pipeline 单文件夹处理模式")
        # root_dir 设置为 undistorted_path 的父目录，以便计算相对路径
        root_dir = Path(args.undistorted_path).parent
        compressor = FolderCompressor(root_dir)
        compressor.process_single_undistorted_folder(args.undistorted_path, args.compress_path)
        return

    print("📁 文件夹批量压缩工具（基于undistorted目录 + 自动清理 + 无确认 + 磁盘空间检查）")
    print("=" * 60)
    print("⚠️  警告：程序会自动删除目标文件夹中除 'undistorted' 外的所有内容，不可逆！")
    print(f"⚠️  要求：目标目录剩余空间需大于 50 GB")
    print(f"⚠️  说明：所有数据检查均基于 'undistorted' 子目录")
    print("=" * 60)
    
    # 根目录：包含所有时间格式子文件夹的目录
    root_dir = "/media/zgw/5211BF7864DFC4FA/1230out/"
    
    # 创建压缩器实例并处理
    compressor = FolderCompressor(root_dir)
    compressor.process_all_target_folders()

if __name__ == "__main__":
    main()
