# AGENTS.md - Promptfoo repo notes

This repository is a promptfoo benchmark suite.

## What changed

- Evaluation logic now lives in `evaluations/*/promptfooconfig.yaml`
- Each category has a short README with the exact promptfoo command
- The old Python runner, configs, datasets, and results files were removed

## Working in this repo

- Prefer editing promptfoo configs directly rather than adding custom runners
- Keep provider settings explicit in each config
- Use `npx promptfoo eval -c <config>` when you need to run a benchmark
- Keep new tests self-contained unless a category intentionally depends on external assets

