# 路径配置快速参考 🚀

## 🎯 首次使用（必做）

```bash
# 方式1: 交互式配置向导（推荐新手）
python setup_paths.py

# 方式2: 命令行快速配置
python config_paths.py --init
python config_paths.py --set-source /path/to/rosbag
python config_paths.py --set-output /path/to/output
python config_paths.py --validate
```

## 📋 常用命令

| 命令 | 说明 |
|------|------|
| `python config_paths.py --show` | 查看当前配置 |
| `python config_paths.py --validate` | 验证路径是否存在 |
| `python config_paths.py --set-source /path` | 设置源目录 |
| `python config_paths.py --set-output /path` | 设置输出目录 |
| `python setup_paths.py` | 运行配置向导 |
| `python check_hardcoded_paths.py` | 检查硬编码路径 |

## 🔧 在代码中使用

```python
from config_paths import PathConfig

# 创建配置实例
config = PathConfig()

# 获取路径
source = config.source_directory
output = config.output_root_directory
script = config.filter_script_path
```

## 🌍 环境变量（多环境切换）

```bash
# 临时覆盖
XL_SOURCE_DIRECTORY="/tmp/rosbag" python pipeline_batch.py --logtime 20251204

# 永久设置（添加到 ~/.bashrc）
export XL_SOURCE_DIRECTORY="/path/to/source"
export XL_OUTPUT_ROOT_DIRECTORY="/path/to/output"
export XL_MAIN_OUT_DIRECTORY="/path/to/main_out"
```

## 🎨 配置优先级

```
环境变量 > 配置文件 > 默认值
   ↑           ↑          ↑
最高优先级   推荐使用   兜底方案
```

## 📂 配置文件位置

- `paths_config.json` - 用户配置（不提交到git）
- `paths_config.json.example` - 配置模板
- `config_paths.py` - 配置管理模块

## ⚠️ 常见问题

**Q: 运行时提示找不到路径？**
```bash
python config_paths.py --validate  # 检查配置
python setup_paths.py              # 重新配置
```

**Q: 如何在不同服务器切换？**
```bash
# 使用环境变量，每个服务器配置不同的 ~/.bashrc
export XL_SOURCE_DIRECTORY="/server_a/data"
```

**Q: 如何检查项目中还有哪些硬编码路径？**
```bash
python check_hardcoded_paths.py --save
```

## 📖 完整文档

详细说明请查看：[PATH_CONFIG_README.md](PATH_CONFIG_README.md)

---

**记住：首次使用必须配置路径！** ⭐
