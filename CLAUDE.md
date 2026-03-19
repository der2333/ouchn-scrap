# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python web scraper for ouchn.cn (国家开放大学学习平台) using Playwright to batch download homework answers. The CLI uses questionary for interactive prompts.

## Architecture

- `main.py` - CLI entry point; handles user interaction flow via questionary prompts
- `src/browser.py` - Playwright browser automation; `start_browser(username, password)` launches Chromium and navigates to the learning platform
- `src/__init__.py` - Package marker

## Commands

```bash
# Run the application
uv run python main.py

# Add dependencies
uv add <package>
```

## Dependencies

- **playwright** - Browser automation (>=1.58.0)
- **questionary** - Interactive CLI prompts

## Development Notes

- Python 3.14+ required (see `.python-version`)
- Virtual environment: `.venv` (pre-initialized)
- Package index: PyPI mirror at pypi.tuna.tsinghua.edu.cn

