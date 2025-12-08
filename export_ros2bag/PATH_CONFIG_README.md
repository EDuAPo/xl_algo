# 路径配置管理系统说明

## 📋 概述

为了解决项目中硬编码路径导致的维护困难和运行失败问题，我们引入了统一的路径配置管理系统 `config_paths.py`。

## 🎯 解决的问题

### 之前存在的问题：
1. ❌ 路径分散在多个文件中，难以统一管理
2. ❌ 每次更换环境需要修改多个文件
3. ❌ 路径层级关系不清晰，容易出错
4. ❌ 缺乏统一的路径验证机制

### 现在的优势：
1. ✅ 所有路径集中在 `config_paths.py` 管理
2. ✅ 支持三种配置方式（环境变量、配置文件、默认值）
3. ✅ 自动处理相对路径和绝对路径
4. ✅ 内置路径验证功能

## 🚀 快速开始

### 1. 初始化配置

第一次使用时，运行以下命令生成默认配置文件：

```bash
python config_paths.py --init
```

这将在项目根目录创建 `paths_config.json` 文件，包含所有路径配置。

### 2. 查看当前配置

```bash
python config_paths.py --show
```

输出示例：
```
============================================================
📋 当前路径配置
============================================================
项目根目录: /path/to/export_ros2bag

数据目录:
  源数据目录: /media/xl/T7/1204/rosbag2_2025_12_04-10_42_08/
  筛选输出目录: /media/xl/T7/1204_out1/
  预处理输出目录: /media/xl/T7/1204_out/
  移动记录目录: /media/xl/T7/1204_out/

配置文件:
  配置文件路径: /path/to/export_ros2bag/paths_config.json
  时间段配置: /path/to/export_ros2bag/time_peridos.yaml
============================================================
```

### 3. 验证路径

验证所有关键路径是否存在：

```bash
python config_paths.py --validate
```

### 4. 修改配置

#### 方法一：通过命令行（推荐）

```bash
# 设置源数据目录
python config_paths.py --set-source /path/to/your/rosbag

# 设置输出根目录
python config_paths.py --set-output /path/to/output

# 设置主输出目录
python config_paths.py --set-main-out /path/to/main_out
```

#### 方法二：编辑配置文件

直接编辑 `paths_config.json`：

```json
{
  "source_directory": "/your/new/source/path",
  "output_root_directory": "/your/new/output/path",
  "main_out": "/your/new/main_out/path",
  "move_record_dir": "/your/new/record/path"
}
```

#### 方法三：使用环境变量（适合不同环境切换）

```bash
# 临时设置（当前会话有效）
export XL_SOURCE_DIRECTORY="/path/to/source"
export XL_OUTPUT_ROOT_DIRECTORY="/path/to/output"
export XL_MAIN_OUT_DIRECTORY="/path/to/main_out"

# 永久设置（添加到 ~/.bashrc 或 ~/.zshrc）
echo 'export XL_SOURCE_DIRECTORY="/path/to/source"' >> ~/.bashrc
source ~/.bashrc
```

## 📖 在代码中使用

### 基本使用

```python
from config_paths import PathConfig

# 方式1: 创建配置实例
config = PathConfig()

# 获取路径
source_dir = config.source_directory
output_dir = config.output_root_directory
filter_script = config.filter_script_path

# 方式2: 使用类方法（单例模式）
source_dir = PathConfig.get_source_directory()
output_dir = PathConfig.get_output_root_directory()
```

### 实际示例

原来的代码（硬编码）：
```python
# ❌ 不推荐
SOURCE_DIRECTORY = "/media/xl/T7/1204/rosbag2_2025_12_04-10_42_08/"
FILTER_SCRIPT = "./move_file_new.py"
```

现在的代码（使用配置）：
```python
# ✅ 推荐
from config_paths import PathConfig

path_config = PathConfig()
SOURCE_DIRECTORY = path_config.source_directory
FILTER_SCRIPT = path_config.filter_script_path
```

## 🔧 配置优先级

系统按以下优先级加载配置（从高到低）：

1. **环境变量** - 最高优先级，适合临时覆盖
2. **配置文件** (`paths_config.json`) - 项目级配置
3. **默认值** - 代码中定义的默认值

### 示例场景

假设三个地方都配置了源目录：
- 环境变量：`XL_SOURCE_DIRECTORY=/env/source`
- 配置文件：`"source_directory": "/config/source"`
- 默认值：`DEFAULT_SOURCE_DIRECTORY = "/default/source"`

最终使用：`/env/source` ✅

## 📂 路径配置列表

### 数据路径

| 配置项 | 环境变量 | 说明 |
|--------|----------|------|
| `source_directory` | `XL_SOURCE_DIRECTORY` | ROS2 Bag源数据目录 |
| `output_root_directory` | `XL_OUTPUT_ROOT_DIRECTORY` | 筛选后bag输出根目录 |
| `main_out` | `XL_MAIN_OUT_DIRECTORY` | 预处理主输出目录 |
| `move_record_dir` | `XL_MOVE_RECORD_DIRECTORY` | 移动记录保存目录 |

### 脚本路径（自动计算）

所有脚本路径都相对于项目根目录自动计算，无需手动配置：

- `filter_script_path` - 筛选脚本
- `run_export_script_path` - 预处理脚本
- `check_compress_script_path` - 检查压缩脚本
- `export_camera_script_path` - 相机导出脚本
- `export_lidar_script_path` - 激光雷达导出脚本
- `export_imu_script_path` - IMU导出脚本
- `undistortion_script_path` - 去畸变脚本
- `extract_sample_script_path` - 提取样本脚本

### 配置文件路径（自动计算）

- `time_periods_yaml_path` - 时间段配置YAML
- `camera_config_yaml_path` - 相机配置YAML

### 参数目录路径（自动计算）

- `undistortion_params_dir_path` - 去畸变参数目录
- `camera_intri_dir_path` - 相机内参目录
- `lidar_extrinic_dir_path` - 激光雷达外参目录

## 🔍 常见问题

### Q1: 运行时提示路径不存在怎么办？

**A:** 首先运行路径验证：
```bash
python config_paths.py --validate
```

根据提示修复不存在的路径。

### Q2: 如何在不同服务器间切换配置？

**A:** 推荐使用环境变量方式：

服务器A的 `~/.bashrc`:
```bash
export XL_SOURCE_DIRECTORY="/data/server_a/rosbag"
export XL_OUTPUT_ROOT_DIRECTORY="/data/server_a/output"
```

服务器B的 `~/.bashrc`:
```bash
export XL_SOURCE_DIRECTORY="/mnt/server_b/rosbag"
export XL_OUTPUT_ROOT_DIRECTORY="/mnt/server_b/output"
```

### Q3: 脚本路径配置错误怎么办？

**A:** 脚本路径是相对于项目根目录自动计算的，通常不需要修改。如果项目结构调整，只需确保 `config_paths.py` 在正确的位置即可。

### Q4: 想临时使用不同的配置怎么办？

**A:** 使用环境变量临时覆盖：
```bash
# 临时使用其他源目录
XL_SOURCE_DIRECTORY="/tmp/test_rosbag" python pipeline_batch.py --logtime 20251204
```

### Q5: 配置文件丢失了怎么办？

**A:** 重新初始化即可：
```bash
python config_paths.py --init
```

## 🛠️ 迁移指南

如果你的代码还在使用硬编码路径，按以下步骤迁移：

### 步骤1: 引入配置模块

```python
from config_paths import PathConfig
path_config = PathConfig()
```

### 步骤2: 替换硬编码路径

```python
# 替换前
SOURCE_DIR = "/media/xl/T7/1204/rosbag2_2025_12_04-10_42_08/"
OUTPUT_DIR = "/media/xl/T7/1204_out1/"
FILTER_SCRIPT = "./move_file_new.py"

# 替换后
SOURCE_DIR = path_config.source_directory
OUTPUT_DIR = path_config.output_root_directory
FILTER_SCRIPT = path_config.filter_script_path
```

### 步骤3: 测试验证

```bash
# 验证路径配置
python config_paths.py --validate

# 运行你的脚本
python your_script.py
```

## 📝 最佳实践

1. **初始化项目时立即配置路径**
   ```bash
   python config_paths.py --init
   python config_paths.py --set-source /your/source/path
   python config_paths.py --set-output /your/output/path
   ```

2. **在脚本开头导入配置**
   ```python
   from config_paths import PathConfig
   path_config = PathConfig()
   ```

3. **使用环境变量管理多环境配置**
   ```bash
   # 开发环境
   export XL_SOURCE_DIRECTORY="/dev/rosbag"
   
   # 生产环境
   export XL_SOURCE_DIRECTORY="/prod/rosbag"
   ```

4. **定期验证路径有效性**
   ```bash
   python config_paths.py --validate
   ```

5. **将 `paths_config.json` 加入版本控制**
   ```bash
   git add paths_config.json
   git commit -m "Update path configuration"
   ```

## 🎉 总结

通过使用统一的路径配置管理系统，你可以：

- ✅ 轻松管理所有路径配置
- ✅ 快速适应不同的部署环境
- ✅ 减少因路径错误导致的运行失败
- ✅ 提高代码的可维护性和可移植性

有任何问题，请参考本文档或运行 `python config_paths.py --help` 查看帮助。
