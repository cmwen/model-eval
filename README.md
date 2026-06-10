# Promptfoo LLM Benchmarks

This repo is now a promptfoo-first benchmark suite for local and hosted LLMs.

## Layout

- `promptfooconfig.yaml` — root config that aggregates all benchmark test sets
- `datasets/*.yaml` — shared benchmark datasets (tests only)
- `evaluations/*/promptfooconfig.yaml` — promptfoo configs for each benchmark
- `evaluations/*/README.md` — short notes for each category
- `evaluations/13-agent-skill-routing/` — extra routing smoke tests already in promptfoo format

## Run

```bash
promptfoo eval
```

This runs the root config and loads all benchmark datasets.

To run a single benchmark category, keep using the category config path:

```bash
promptfoo eval -c evaluations/01-knowledge-retrieval/promptfooconfig.yaml
```

To run a single model from the shared provider set:

```bash
promptfoo eval --filter-providers gemma4-e4b
```

Change `gemma4-e4b` to another provider label/id (for example `gemma4-e2b`) to switch models without editing benchmark configs.

## Provider files

Text benchmarks now use shared provider definitions:

```yaml
providers/gemma4-e2b.yaml
providers/gemma4-e4b.yaml
```

Edit those files when you need to change endpoint/model wiring globally.

## Categories

1. Knowledge retrieval
2. Reasoning
3. Structured output
4. Tool calling
5. Web tools
6. Image support
7. Audio support
8. Code generation
9. Safety
10. Multilingual
11. Context window
12. Consistency
13. Agent and skill routing
