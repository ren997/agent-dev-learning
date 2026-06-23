# Repository Guidelines

## Project Structure & Module Organization

This repository is a learning workspace for Agent development. Course content lives in `lessons/` as numbered Markdown files such as `0002-call-llm-api.md`. Reusable reference material goes in `reference/`, and durable progress notes go in `learning-records/`. Shared presentation assets belong in `assets/`.

Practice code is organized by implementation stage:
- `02_大模型API调用/`: lesson 0002 chatbot exercise (`simple_chat.py`)
- `04_工具调用Agent/`: lesson 0004 tool-calling agent exercise (`mini_agent.py`)

Keep new code examples in numbered top-level practice folders only when a lesson has hands-on implementation.

## Build, Test, and Development Commands

- `pip install openai`: install the only required Python dependency used by current exercises.
- `python 02_大模型API调用/simple_chat.py`: run the minimal chat client locally.
- `python 04_工具调用Agent/mini_agent.py`: run the minimal tool-calling agent.
- `python -m py_compile 02_大模型API调用/simple_chat.py 04_工具调用Agent/mini_agent.py`: quick syntax validation before committing.

Copy `config.example.json` to `config.json` inside a practice folder before running examples.

## Coding Style & Naming Conventions

Use Python 3 with 4-space indentation, type hints where practical, and small focused functions. Follow the existing naming style:
- `snake_case` for functions and variables
- `UPPER_CASE` for module constants like `DEFAULT_CONFIG`
- numbered lesson and record files such as `0004-build-first-tool-agent.md`

Keep comments brief and explanatory. Match the repository’s existing Markdown-first teaching style.

## Testing Guidelines

There is no formal test suite yet. For now, validate changes with `python -m py_compile` and a manual run of the affected script. When adding tests later, place them in a top-level `tests/` directory and name files `test_<module>.py`.

## Commit & Pull Request Guidelines

Use Conventional Commit-style prefixes such as `feat:`, `fix:`, and `docs:`. Keep subjects short and imperative, for example `feat: add tool-calling example` or `fix: handle API connection errors in simple_chat`.

Pull requests should include:
- a short summary of the learning or code change
- affected paths, for example `lessons/0004-*` or `04_工具调用Agent/`
- terminal output or screenshots for user-facing behavior changes

## Security & Configuration Tips

Do not commit `config.json` files; they are ignored on purpose. Store API keys in local config or environment variables such as `OPENAI_API_KEY`.
