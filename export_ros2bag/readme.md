# ROS2 Bag 数据处理管道

自动驾驶多传感器数据处理工具链，用于从 ROS2 bag 文件中提取、处理和打包相机、激光雷达、IMU数据。

## 🚀 快速开始

### 1. 配置路径（重要！⭐）

**第一次使用前，必须先配置路径：**

```bash
# 初始化配置文件
python config_paths.py --init

# 设置您的数据路径
python config_paths.py --set-source /path/to/your/rosbag
python config_paths.py --set-output /path/to/output
python config_paths.py --set-main-out /path/to/main_out

# 验证路径配置
python config_paths.py --validate
```

详细说明请查看 [PATH_CONFIG_README.md](PATH_CONFIG_README.md)

### 2. 运行完整流程

```bash
# 批量处理（推荐）
python pipeline_batch.py --logtime 20251204_104208 --vehicle vehicle_000

# 单次处理
python run_export.py --bag /path/to/rosbag --out /path/to/output --vehicle vehicle_000 --logtime 20251204
```

## 📖 使用说明

### 独立模块使用

#### 导出相机图像
```bash
python3 ./export_camera.py --bag /path/to/rosbag/ --out /path/to/output/
```

#### 导出激光雷达点云
```bash
python3 ./export_lidar.py --bag /path/to/rosbag/ --out /path/to/output/ --format pcd_binary
```

#### 导出IMU数据
```bash
python3 ./export_imu/export_imu.py --bag /path/to/rosbag/ --out /path/to/output/ins.json
```

#### 图像去畸变
```bash
python3 ./undistortion/undistortion.py --images /path/to/images --params ./undistortion/intrinsic_param --vehicle vehicle_000 --out /path/to/undistorted --scale_min 0.2 --logtime 20251104_160012
```

## 🔧 路径配置管理

### 为什么需要路径配置？

项目中有多个硬编码路径，在不同环境运行时容易出错。现在使用 `config_paths.py` 统一管理所有路径。

### 三种配置方式

1. **配置文件**（推荐）
   ```bash
   python config_paths.py --set-source /your/path
   ```

2. **环境变量**（适合多环境切换）
   ```bash
   export XL_SOURCE_DIRECTORY="/path/to/source"
   export XL_OUTPUT_ROOT_DIRECTORY="/path/to/output"
   ```

3. **直接编辑** `paths_config.json`

### 查看当前配置

```bash
python config_paths.py --show
```

## 📂 项目结构

详见项目框架说明。主要模块：

- **pipeline_batch.py** - 批量自动化流程（主入口）
- **run_export.py** - 单次完整流程
- **filter_rosbag.py** - ROS2 Bag时间段筛选
- **export_camera.py** - 相机图像导出
- **export_lidar.py** - 激光雷达点云导出
- **export_imu/** - IMU数据导出
- **undistortion/** - 图像去畸变
- **extract_sample_undistorted.py** - 关键帧提取
- **check_and_compress.py** - 数据校验与压缩
- **config_paths.py** - 路径配置管理 ⭐
- **setup_paths.py** - 路径配置向导

## ⚠️ 注意事项

1. **首次使用必须配置路径**，否则会使用默认路径可能导致失败
2. 所有脚本已更新为使用统一路径配置，无需手动修改代码中的路径
3. 如果遇到路径相关错误，运行 `python config_paths.py --validate` 检查配置

## 📚 更多文档

- [路径配置详细说明](PATH_CONFIG_README.md)
- [配置文件示例](paths_config.json.example)