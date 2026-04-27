---
name: update-readme
description: Review the project source code, public API, configuration, and CHANGELOG to rewrite or update README.md so it accurately reflects the current state of the project. Use when the user asks to update the readme, refresh documentation, or sync the readme with the current code.
---

# Update README

Reviews the project and rewrites `README.md` to accurately reflect what the project
currently does, how to install it, and how to use it.

## Workflow

### Step 1 — Understand the project

Read these files to build a complete picture:

- `pyproject.toml` — project name, description, version, entry points, dependencies
- `src/` — public modules and their docstrings; focus on `__init__.py` and any top-level functions/classes exposed to users
- `CHANGELOG.md` — recent additions and changes that belong in the readme
- Existing `README.md` — preserve any sections that are still accurate

```bash
# Confirm the package entry points
grep -A5 '\[project.scripts\]' pyproject.toml

# List public source files
find src -name "*.py" | sort
```

### Step 2 — Identify what needs to change

Compare the existing README against what you found and note:

- Outdated or missing feature descriptions
- Installation instructions that no longer match `pyproject.toml`
- Usage examples that reference non-existent functions or flags
- Sections that can be removed because the feature was deleted
- New features from `CHANGELOG.md` that are not yet documented

### Step 3 — Rewrite README.md

Use this structure as a guide; adapt sections to fit the project:

```markdown
# Project Name

One-sentence description of what this project does and who it is for.

## Features

- Key capability 1
- Key capability 2

## Installation

\`\`\`shell
uv add project-name
# or
pip install project-name
\`\`\`

## Usage

\`\`\`python
# Minimal working example
\`\`\`

## Development

\`\`\`shell
uv sync --all-extras
uv run pre-commit install
make lint
make test
\`\`\`

## Publishing

Push a version tag to trigger a GitLab CI release:

\`\`\`shell
git tag vX.Y.Z
git push origin vX.Y.Z
\`\`\`

## License

MIT
```

Rules:
- Keep the tone direct and technical.
- Every code example must be runnable or clearly pseudocode.
- Do not invent features that are not in the source code.
- Preserve any custom sections the user has already written that are still accurate.
- Do not add a changelog summary — link to `CHANGELOG.md` instead if one exists.

### Step 4 — Summarize changes

After writing the file, tell the user:
- Which sections were added, updated, or removed.
- Any gaps you could not fill because source information was missing (e.g. no docstrings, missing usage example).
