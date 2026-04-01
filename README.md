# ouchn-scrap

国家开放大学学习平台作业批量下载工具。

## 功能

- 批量下载形考作业答案
- 交互式课程选择
- 自动浏览器会话管理

## 技术栈

- Python 3.14+
- Playwright (浏览器自动化)
- questionary (交互式 CLI)

## 项目结构

```
main.py                        # CLI 入口点
src/
  __init__.py                  # 包标记
  session.py                   # 浏览器会话管理
  stealth.py                    # 隐身浏览器初始化
  download_formative/           # 形考作业下载
    __init__.py
    download.py
    index.py
    course_handle.py
pyproject.toml                 # 依赖管理
```

## 快速开始

```bash
# 安装浏览器（首次使用）
uv run playwright install chromium

# 运行
uv run python main.py

# 添加依赖
uv add <package>
```

## 构建

```bash
# 使用 nuitka 打包（含浏览器）
python -m nuitka --mode=onefile \
  --playwright-include-browser=chromium_headless_shell-1208 \
  --windows-company-name="xichen" \
  --windows-product-name="OUCHN SCRAPER" \
  --windows-file-version="1.0.0.0" \
  --windows-product-version="1.0.0.0" \
  --windows-file-description="国家开放大学学习平台自动化工具" \
  main.py
```

## 注意事项

- Python 3.14+ (`.python-version`)
- 虚拟环境: `.venv` (预初始化)
- PyPI 镜像: pypi.tuna.tsinghua.edu.cn
