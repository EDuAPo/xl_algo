# 文件重命名记录

## 📝 重命名清单

为了提升代码规范性和可维护性，以下文件已重命名：

| 旧文件名 | 新文件名 | 说明 |
|---------|---------|------|
| `move_file_new.py` | `filter_rosbag.py` | 更准确地描述功能：ROS2 Bag文件按时间段筛选 |
| `pipline_new1.py` | `pipeline_batch.py` | 去除临时字眼"new1"，修正拼写错误"pipline" → "pipeline" |

## 🔄 影响的文件

以下文件已自动更新引用：

- ✅ `config_paths.py` - 脚本路径配置
- ✅ `readme.md` - 主文档和示例命令
- ✅ `PATH_CONFIG_README.md` - 路径配置文档
- ✅ `setup_paths.py` - 配置向导提示
- ✅ `QUICK_REFERENCE.md` - 快速参考

## 🎯 迁移指南

### 如果你之前使用 `move_file_new.py`

**旧命令：**
```bash
python move_file_new.py --source /path/to/rosbag --output /path/to/output --start 111428 --end 111812
```

**新命令（相同功能）：**
```bash
python filter_rosbag.py --source /path/to/rosbag --output /path/to/output --start 111428 --end 111812
```

### 如果你之前使用 `pipline_new1.py`

**旧命令：**
```bash
python pipline_new1.py --logtime 20251204_104208 --vehicle vehicle_000
```

**新命令（相同功能）：**
```bash
python pipeline_batch.py --logtime 20251204_104208 --vehicle vehicle_000
```

## ⚠️ 注意事项

1. **功能完全相同**：只是文件名改变，所有功能、参数、行为都保持不变
2. **自动更新**：配置文件 `config_paths.py` 已自动更新，无需手动修改
3. **向后兼容**：如果你的脚本或文档中引用了旧文件名，请手动更新
4. **Git 历史**：使用 `git mv` 可以保留文件历史，但这里使用了普通重命名

## 📚 文件功能说明

### `filter_rosbag.py`（原 move_file_new.py）
- **功能**：按时间段筛选和转移 ROS2 Bag (.db3) 文件
- **主要特性**：
  - 支持移动/复制模式
  - 自动生成 metadata.yaml
  - 时间范围交集匹配
  - 移动记录保存与恢复

### `pipeline_batch.py`（原 pipline_new1.py）
- **功能**：批量处理多个时间段的完整数据流程
- **主要特性**：
  - 读取 YAML 配置的时间段列表
  - 自动筛选、导出、去畸变、压缩
  - 支持移动模式节省磁盘空间
  - 异常恢复机制

## 🎉 优化收益

1. **更清晰的命名**：文件名直接反映其功能
2. **更专业的代码**：去除临时性质的命名（new、1等）
3. **更好的可维护性**：新人更容易理解项目结构
4. **符合命名规范**：遵循 Python 社区最佳实践

---

**重命名完成时间**：2025-12-08

如有任何问题，请查看主文档 `readme.md` 或运行 `python config_paths.py --help`
