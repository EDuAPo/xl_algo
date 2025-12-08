# XL Algo - 自动驾驶算法工具集

自动驾驶数据处理和算法开发工具集合。

## 📦 项目模块

### 🚀 export_ros2bag - ROS2 Bag 数据预处理管道

完整的 ROS2 Bag 数据处理工具链，用于自动驾驶多传感器数据的提取、预处理和打包。

**主要功能：**
- 相机图像导出与去畸变
- 激光雷达点云数据导出
- IMU 数据提取与坐标转换
- 时间段筛选与批量处理
- 数据校验与压缩打包
- 统一路径配置管理

**快速开始：**
```bash
cd export_ros2bag
python setup_paths.py  # 配置路径
python pipeline_batch.py --logtime 20251204_104208 --vehicle vehicle_000
```

**详细文档：** [export_ros2bag/readme.md](export_ros2bag/readme.md)

---

## 🌳 分支说明

- `main` - 主分支，稳定版本
- `feature/ros2bag-preprocessing` - ROS2 Bag 数据预处理功能开发分支

## 🤝 贡献指南

1. 从 `main` 分支创建功能分支
2. 开发并测试新功能
3. 提交 Pull Request
4. 代码审查后合并

## 📝 开发日志

### 2025-12-08
- ✅ 完成 ROS2 Bag 数据预处理管道
- ✅ 统一路径配置管理系统
- ✅ 文件命名规范化优化

## 📄 许可证

待定

## 👥 维护者

XL Team
