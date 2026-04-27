---
name: bump-version
description: Bump the project version by analyzing git changes since the last tag, deciding the next semver version, updating CHANGELOG.md in Keep a Changelog format, and regenerating uv.lock. Use when the user asks to bump the version, cut a release, update the changelog, or tag a new version.
---

# Bump Version

Analyzes changes since the last git tag, determines the next semver version, updates
`CHANGELOG.md`, and regenerates `uv.lock`.

## Workflow

### Step 1 — Gather changes

Run these commands to collect the context you need:

```bash
# Find the latest tag (empty output means no tags yet)
git tag -l | sort -V | tail -1

# List commits since the last tag (or all commits if no tag exists)
LAST_TAG=$(git tag -l | sort -V | tail -1)
if [ -n "$LAST_TAG" ]; then
  git log "${LAST_TAG}..HEAD" --oneline
else
  git log --oneline
fi

# Summarize changed files
git diff "${LAST_TAG}..HEAD" --stat 2>/dev/null || git diff --stat HEAD
```

### Step 2 — Decide the next version

If the user specified a version, use it exactly.

Otherwise apply these semver rules based on the changes:

| Change type | Bump |
|-------------|------|
| Breaking API change, incompatible behavior | **major** (X+1.0.0) |
| New feature, backward-compatible | **minor** (X.Y+1.0) |
| Bug fix, refactor, docs, chore | **patch** (X.Y.Z+1) |

Default to `0.1.0` when there are no previous tags.

Present the chosen version to the user and ask for confirmation before proceeding.

### Step 3 — Update CHANGELOG.md

Read `CHANGELOG.md`, then prepend a new release section under `## [Unreleased]`.

Required format (Keep a Changelog):

```markdown
## [X.Y.Z] - YYYY-MM-DD

### Added
- ...

### Changed
- ...

### Fixed
- ...

### Removed
- ...
```

Rules:
- Use today's date in `YYYY-MM-DD` format.
- Only include sections (`Added`, `Changed`, `Fixed`, `Removed`) that have entries.
- Keep the `## [Unreleased]` heading at the top with empty content.
- Write entries from the user's perspective (what changed, not how).

### Step 4 — Regenerate uv.lock

```bash
uv lock
```

### Step 5 — Summarize

After completing all steps, tell the user:
- The new version number.
- Which sections were written to `CHANGELOG.md`.
- That `uv.lock` has been updated.
- The next manual step: `git add CHANGELOG.md uv.lock && git commit -m "chore: release vX.Y.Z" && git tag vX.Y.Z && git push origin main --tags`
