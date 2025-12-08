# Git 分支管理说明

## 📊 当前仓库状态

**仓库名称**: xl_algo  
**当前位置**: `d:\Project\xl_algo`  
**初始化时间**: 2025-12-08

## 🌳 分支结构

### 主分支
- **`main`** - 主分支，稳定版本
  - 包含完整的 ROS2 Bag 数据预处理管道
  - 所有功能已测试可用
  - commit: `d613624`

### 功能分支
- **`feature/ros2bag-preprocessing`** - ROS2 Bag 数据预处理功能分支 ✨ (当前分支)
  - 基于 `main` 分支创建
  - 用于持续开发和改进 ROS2 Bag 预处理功能
  - 所有新功能先在此分支开发和测试

## 📦 已提交内容

### 初始提交 (d613624)
✅ **完整的 ROS2 Bag 数据预处理管道**

包含以下功能模块：
- 📸 相机图像导出与去畸变
- 📡 激光雷达点云数据导出
- 🧭 IMU 数据提取与坐标转换
- ⏱️ 时间段筛选与批量处理
- ✅ 数据校验与压缩
- ⚙️ 统一路径配置管理
- 📝 完善的文档系统

**主要文件：**
- `pipeline_batch.py` - 批量处理主程序
- `filter_rosbag.py` - ROS2 Bag 筛选工具
- `config_paths.py` - 路径配置管理
- `setup_paths.py` - 配置向导
- 完整的文档和示例

## 🔄 分支工作流程

### 1. 开发新功能

```bash
# 确保在功能分支
git checkout feature/ros2bag-preprocessing

# 进行开发...
# 修改文件、添加功能等

# 提交更改
git add .
git commit -m "feat: 添加新功能描述"
```

### 2. 合并到主分支

当功能开发完成并测试通过后：

```bash
# 切换到 main 分支
git checkout main

# 合并功能分支
git merge feature/ros2bag-preprocessing

# 如果有冲突，解决后继续
git add .
git commit -m "merge: 合并 ROS2 Bag 预处理功能"
```

### 3. 查看历史记录

```bash
# 查看提交历史
git log --oneline --graph --all

# 查看分支状态
git branch -a

# 查看文件变更
git status
```

## 🚀 推送到远程仓库（可选）

如果需要推送到 GitHub 或其他远程仓库：

```bash
# 添加远程仓库
git remote add origin https://github.com/EDuAPo/xl_algo.git

# 推送 main 分支
git push -u origin main

# 推送功能分支
git push -u origin feature/ros2bag-preprocessing
```

## 📋 提交消息规范

使用约定式提交（Conventional Commits）：

- `feat:` - 新功能
- `fix:` - 修复 bug
- `docs:` - 文档更新
- `style:` - 代码格式调整
- `refactor:` - 代码重构
- `perf:` - 性能优化
- `test:` - 测试相关
- `chore:` - 构建/工具链相关

**示例：**
```bash
git commit -m "feat: 添加多线程处理支持"
git commit -m "fix: 修复路径配置读取错误"
git commit -m "docs: 更新 README 使用说明"
```

## 🔍 常用命令速查

| 命令 | 说明 |
|------|------|
| `git status` | 查看当前状态 |
| `git branch` | 查看所有分支 |
| `git checkout <branch>` | 切换分支 |
| `git log --oneline` | 查看提交历史 |
| `git diff` | 查看文件变更 |
| `git add .` | 添加所有更改 |
| `git commit -m "msg"` | 提交更改 |
| `git merge <branch>` | 合并分支 |

## 📝 .gitignore 说明

已配置忽略以下内容：
- Python 缓存文件 (`__pycache__/`, `*.pyc`)
- 虚拟环境 (`venv/`, `venv_ros_export/`)
- 大型数据文件 (`*.db3`, `*.bag`, `*.pcd`, `*.zip`)
- 本地配置 (`paths_config.json`)
- IDE 配置 (`.vscode/`, `.idea/`)
- 构建产物 (`build/`, `install/`, `log/`)

## 🎯 下一步计划

- [ ] 添加单元测试
- [ ] 性能优化和并行处理
- [ ] 支持更多传感器类型
- [ ] 添加 CI/CD 流程
- [ ] 完善错误处理和日志系统

## 💡 提示

1. **定期提交**: 小步快跑，经常提交
2. **清晰消息**: 提交消息要简洁明了
3. **功能分支**: 新功能在功能分支开发
4. **测试后合并**: 确保测试通过再合并到 main
5. **保持同步**: 定期从 main 拉取更新

---

**创建时间**: 2025-12-08  
**维护者**: XL Team
