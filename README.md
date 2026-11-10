# aoc-boilerplate-py

Python boilerplate project for Advent of Code

## ⚠️ AI-Free Coding Zone

**This repository is designated as an AI-free coding zone.** All AI coding assistants are explicitly disabled and must refuse to provide coding assistance. See [AGENTS.md](./AGENTS.md) for the complete policy.

This is intentional - Advent of Code is about learning and problem-solving, not having AI write the solutions for you.

# Features
 * Python 3.14 managed by [uv](https://docs.astral.sh/uv/) (`.python-version`, `uv.lock`)
 * [ruff](https://docs.astral.sh/ruff/) for formatting and linting
 * `mypy --strict`
 * `pytest`
 * GitHub Actions CI and Dependabot
 * Configuration for VSCode
    * **No AI Assistants** (`chat.disableAIFeatures`, Copilot, IntelliCode, Claude, Gemini, Codeium, TabNine, etc.)
    * ruff as formatter, fix-all and import sorting on save
 * Configuration for PyCharm
    * **JetBrains AI Assistant disabled** via [`.noai`](./.noai)
    * See [.idea/INTELLIJ_AI_SETUP.md](./.idea/INTELLIJ_AI_SETUP.md) for disabling third-party AI plugins

# Usage

```sh
uv sync
uv run pytest                                # all days
uv run pytest -k day0                        # one day
uv run python -m aoc.day0 day0.input.txt     # run against inputs/day0.input.txt
uv run ruff format . && uv run ruff check --fix .
uv run mypy src tests
```

One module per day in `src/aoc/` with `part1`/`part2(text: str)`. Puzzle files go in `inputs/` and are read with `read_input("dayN.input.txt")`.
