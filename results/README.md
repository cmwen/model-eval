# Results Directory

This directory contains evaluation results.

## Output Format

Results are saved in JSONL format:

```json
{"timestamp": "2024-01-10T12:00:00Z", "model": "gpt-4o", "category": "reasoning", "test_id": "logic_puzzle_1", "score": 4.5, "details": {...}}
```

## File Naming Convention

`{date}_{model}_{category}.jsonl`

Example: `2024-01-10_gpt-4o_reasoning.jsonl`

## Summary Reports

Aggregate summaries are generated in the `summaries/` subdirectory.
