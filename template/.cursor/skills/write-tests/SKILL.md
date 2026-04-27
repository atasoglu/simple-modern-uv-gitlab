---
name: write-tests
description: Write or improve pytest tests for a Python module by reading the source code, identifying untested behavior, and generating focused test cases. Use when the user asks to write tests, add test coverage, test a function or module, or when coverage is low.
---

# Write Tests

Reads source code and existing tests to write focused pytest tests that improve
coverage and catch real bugs.

## Workflow

### Step 1 — Identify what to test

If the user specified a file or function, start there. Otherwise find the gaps:

```bash
# Run coverage and show missing lines
uv run pytest --cov --cov-report=term-missing 2>&1 | tail -30
```

Read the source file(s) with low or missing coverage. Focus on:
- Public functions and methods (skip private `_helpers` unless asked)
- Edge cases: empty input, `None`, zero, negative numbers, empty collections
- Error paths: what should raise exceptions and what error type
- Boundary conditions: off-by-one, max/min values

### Step 2 — Read existing tests

Before writing anything, read `tests/` to understand:
- Existing conventions (fixtures, conftest.py, helpers)
- What is already covered so you don't duplicate it
- The naming pattern in use (`test_<function>_<scenario>`)

### Step 3 — Write the tests

Place new tests in `tests/test_<module_name>.py` (create the file if it does not
exist).

Follow these rules:

**Structure**
```python
import pytest
from package_name.module import function_under_test


def test_function_returns_expected_value():
    result = function_under_test(input)
    assert result == expected


def test_function_raises_on_invalid_input():
    with pytest.raises(ValueError, match="descriptive pattern"):
        function_under_test(bad_input)


@pytest.mark.parametrize("input,expected", [
    (case_1_in, case_1_out),
    (case_2_in, case_2_out),
])
def test_function_parametrized(input, expected):
    assert function_under_test(input) == expected
```

**Rules**
- One assertion per test where practical; use `pytest.approx` for floats.
- Prefer `parametrize` over repetitive similar tests.
- Use fixtures in `conftest.py` only for shared setup needed by 3+ tests.
- Do not mock unless the code calls external I/O (network, filesystem, time).
- Test names must describe the scenario: `test_parse_empty_string_returns_none`,
  not `test_parse_1`.

### Step 4 — Verify

```bash
uv run pytest tests/test_<module_name>.py -v
```

All new tests must pass. If any fail, fix them before finishing.

Then check coverage improved:

```bash
uv run pytest --cov --cov-report=term-missing 2>&1 | grep "^src/"
```

### Step 5 — Summarize

Tell the user:
- Which file(s) were created or modified.
- How many test cases were added and what scenarios they cover.
- The new coverage percentage for the tested module (if available).
- Any behavior that could not be tested due to missing information (e.g. no
  docstring, unclear expected output).
