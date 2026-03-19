# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Python web scraper for ouchn.cn (国家开放大学学习平台) using Playwright to batch download homework answers. CLI uses questionary for interactive prompts.

## Structure

```
main.py           # CLI entry point
src/
  browser.py      # Playwright automation
  __init__.py     # Package marker
pyproject.toml    # Dependencies
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

## Notes

- Python 3.14+ (`.python-version`)
- Virtual environment: `.venv` (pre-initialized)
- PyPI mirror: pypi.tuna.tsinghua.edu.cn
