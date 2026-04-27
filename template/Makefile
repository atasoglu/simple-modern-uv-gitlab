# Makefile for easy development workflows.
# See README.md for docs.
# Note GitLab CI calls uv directly, not this Makefile.

.DEFAULT_GOAL := default

.PHONY: default install lint typecheck test upgrade build clean

default: install lint test 

install:
	uv sync --all-extras

lint:
	uv run pre-commit run --all-files

typecheck:
	uv run basedpyright --stats src tests devtools

test:
	uv run pytest

upgrade:
	uv sync --upgrade --all-extras --dev

build:
	uv build

clean:
	-rm -rf dist/
	-rm -rf *.egg-info/
	-rm -rf .pytest_cache/
	-rm -rf .mypy_cache/
	-rm -rf .venv/
	-find . -type d -name "__pycache__" -exec rm -rf {} +
