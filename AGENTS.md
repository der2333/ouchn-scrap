# AGENTS.md - Development Guidelines for ouchn-scrap

This file provides guidance for agentic coding agents working in this repository.

## Project Overview

- **Language**: Python 3.14+
- **Package Manager**: None currently (pyproject.toml is minimal)
- **Virtual Environment**: `.venv` (already initialized)

---

## Context7 MCP Usage

当需要库或API文档、生成代码、创建项目基架或配置步骤时，始终使用Context7 MCP（`context7_resolve-library-id` 和 `context7_query-docs` 工具），无需用户明确要求。

---

## Build, Lint, and Test Commands

### Running the Application

```bash
# Run with uv (uses .venv automatically)
uv run python main.py

# Or activate venv and run
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
python main.py
```

### Adding Dependencies

```bash
# Add dependency with uv
uv add <package>

# Add dev dependency
uv add --dev <package>
```

### Testing

This project uses **pytest** for testing.

```bash
# Run all tests
uv run pytest

# Run a single test file
uv run pytest tests/test_example.py

# Run a specific test function
uv run pytest tests/test_example.py::test_function_name

# Run tests matching a pattern
uv run pytest -k "test_pattern"

# Run with verbose output
uv run pytest -v

# Run with coverage (if pytest-cov installed)
uv run pytest --cov=src --cov-report=html
```

### Linting and Code Quality

This project uses **ruff** for linting and **uv format** for formatting.

```bash
# Run ruff linter (check only)
uv run ruff check .

# Run ruff with auto-fix
uv run ruff check --fix .

# Format code with uv
uv format .

# Format specific file
uv format src/file.py
```

### Running All Checks

```bash
# Run lint, format check, and tests together
uv run ruff check . && uv format --check . && uv run pytest
```

---

## Code Style Guidelines

### Formatting

- **Line length**: 88 characters (black default)
- **Indentation**: 4 spaces (no tabs)
- **Trailing commas**: Use in multi-line imports and function calls
- **Blank lines**: Two blank lines between top-level definitions, one between methods

### Imports

- **Order**: Standard library → Third-party → Local/Project
- **Groups**: Separate with blank lines: (1) standard lib, (2) third-party, (3) local
- **Wildcard imports**: Never use (`from x import *`)
- **Relative imports**: Prefer absolute imports for clarity
- **Line splitting**: Use parentheses for wrapped imports

```python
# Correct import order
import os
import sys
from collections import defaultdict
from pathlib import Path

import requests
from flask import Flask

from .models import User
from .utils import helpers
```

### Naming Conventions

- **Variables/functions**: `snake_case` (e.g., `user_name`, `get_data`)
- **Classes**: `PascalCase` (e.g., `UserService`, `DataProcessor`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `MAX_RETRIES`, `DEFAULT_TIMEOUT`)
- **Private methods**: Prefix with underscore (e.g., `_internal_method`)
- **Avoid**: Single-letter names except in loops/comprehensions (`i`, `j`, `x`)

### Type Annotations

- **Use type hints** for all function parameters and return values
- **Use `typing` module** for complex types (List, Dict, Optional, Union)
- **Avoid** `Any` unless absolutely necessary

```python
def process_user(user_id: int, name: str) -> Optional[User]:
    """Process user data and return User object."""
    ...
```

### Error Handling

- **Use specific exceptions**: Catch specific errors, not bare `Exception`
- **Reraise with context**: Use `raise ... from original` to preserve stack traces
- **Custom exceptions**: Create specific exception classes for your domain
- **Never swallow errors silently**: Log or reraise

```python
try:
    result = api.call()
except ValueError as e:
    logger.error(f"Invalid input: {e}")
    raise APIError("Failed to process request") from e
```

### Docstrings

- **Format**: Use Google-style or NumPy-style docstrings
- **Required for**: All public functions, classes, and modules
- **Include**: Args, Returns, Raises sections

```python
def calculate_total(items: list[float], tax_rate: float) -> float:
    """Calculate total price including tax.

    Args:
        items: List of item prices.
        tax_rate: Tax rate as decimal (e.g., 0.08 for 8%).

    Returns:
        Total price including tax.

    Raises:
        ValueError: If tax_rate is negative.
    """
    if tax_rate < 0:
        raise ValueError("Tax rate cannot be negative")
    return sum(items) * (1 + tax_rate)
```

### Testing Guidelines

- **Test file naming**: `test_<module_name>.py`
- **Test class naming**: `Test<ClassName>`
- **Test function naming**: `test_<description>`
- **Arrange-Act-Assert**: Use clear AAA pattern
- **Fixtures**: Use pytest fixtures for shared setup
- **Coverage**: Aim for meaningful coverage, not 100%

```python
class TestUserService:
    def test_create_user_success(self, db_fixture):
        # Arrange
        service = UserService(db_fixture)
        
        # Act
        user = service.create_user("test@example.com")
        
        # Assert
        assert user.email == "test@example.com"
        assert user.id is not None
```

### Project Structure

```
ouchn-scrap/
├── src/                  # Source code (recommended)
│   └── ouchn_scrap/
│       ├── __init__.py
│       └── ...
├── tests/                # Test files
│   ├── __init__.py
│   └── test_*.py
├── pyproject.toml        # Project config
├── .python-version        # Python version
└── main.py               # Entry point
```

---

## Dependencies to Add

To enable the commands above, add these to `pyproject.toml`:

```toml
[project]
dependencies = [
    "requests",
    "pytest",
    "ruff",
]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = "test_*.py"

[tool.ruff]
line-length = 88
```