# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Python web scraper for ouchn.cn (国家开放大学学习平台) using Playwright to batch download homework answers. CLI uses questionary for interactive prompts.

## Structure

```
main.py                        # CLI entry point
src/
  __init__.py                  # Package marker
  session.py                   # Browser session management
  stealth.py                    # Stealth browser initialization
  download_formative/           # Formative homework download
    __init__.py
    download.py
    index.py
    course_handle.py
pyproject.toml                 # Dependencies
```

## Commands

```bash
# Install browser (first time only)
uv run playwright install chromium

# Run
uv run python main.py

# Add dependencies
uv add <package>
```

## Build

```bash
# Package with nuitka (includes browser)
python -m nuitka --mode=onefile \
  --playwright-include-browser=chromium_headless_shell-1208 \
  --windows-company-name="xichen" \
  --windows-product-name="OUCHN SCRAPER" \
  --windows-file-version="1.0.0.0" \
  --windows-product-version="1.0.0.0" \
  --windows-file-description="国家开放大学学习平台自动化工具" \
  main.py
```

## Notes

- Python 3.14+ (`.python-version`)
- Virtual environment: `.venv` (pre-initialized)
- PyPI mirror: pypi.tuna.tsinghua.edu.cn
