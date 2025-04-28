# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build and Test Commands
- Install dependencies: `uv sync`
- Run all tests: `uv run pytest`
- Run a single test: `uv run pytest tests/path_to_test.py::test_function_name`
- Lint code: `uv run ruff check .`
- Format code: `uv run ruff format .`

## Code Style Guidelines
- Follow PEP 8 conventions for Python code
- Use type hints for all function parameters and return values
- Organize imports: standard library, third-party, local modules (separated by blank line)
- Use snake_case for variables and functions, PascalCase for classes
- Prefer explicit error handling with try/except blocks
- Include docstrings for all public functions, classes, and modules
- Maximum line length: 88 characters (Black compatible)

## Project Structure
- Main package: `mcp_study`
- Tests go in the `tests/` directory with `test_` prefix
- Use relative imports within the package
