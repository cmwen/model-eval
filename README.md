# Promptfoo LLM Benchmarks

This repo is now a promptfoo-first benchmark suite for local and hosted LLMs.

## Layout

- `evaluations/*/promptfooconfig.yaml` — promptfoo configs for each benchmark
- `evaluations/*/README.md` — short notes for each category
- `evaluations/13-agent-skill-routing/` — extra routing smoke tests already in promptfoo format

## Run

```bash
npx promptfoo eval -c evaluations/01-knowledge-retrieval/promptfooconfig.yaml
npx promptfoo eval -c evaluations/02-reasoning/promptfooconfig.yaml
npx promptfoo eval -c evaluations/03-structured-output/promptfooconfig.yaml
```

Swap the config path for any other category. The configs use promptfoo assertions instead of the old Python evaluator stack.

## Local Ollama

Most text benchmarks target an OpenAI-compatible local endpoint such as Ollama:

```yaml
providers:
  - id: openai:chat:gpt-oss:20b
    config:
      apiBaseUrl: http://localhost:11434/v1
      temperature: 0
```

Adjust the provider block in a config to match the model you want to score.

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

