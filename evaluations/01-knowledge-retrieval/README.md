# Knowledge Retrieval Evaluation

**Cognitive Type**: System 1 (Fast Thinking)

## Purpose

Tests the model's ability to quickly retrieve and present factual information. These are "lookup" tasks that don't require complex reasoning.

## Test Categories

### 1. General Knowledge
- Historical facts
- Scientific concepts
- Geographic information
- Cultural references

### 2. Current Events (with context)
- News summaries
- Recent developments
- Temporal awareness

### 3. Domain-Specific Knowledge
- Technical terminology
- Industry standards
- Specialized vocabulary

## Evaluation Metrics

| Metric | Description | Weight |
|--------|-------------|--------|
| **Accuracy** | Factual correctness | 40% |
| **Relevance** | Addresses the question | 30% |
| **Completeness** | Covers key points | 20% |
| **Conciseness** | No unnecessary info | 10% |

## Expected Behavior

- Quick, direct answers
- Factually accurate
- Appropriate level of detail
- Acknowledgment when uncertain

## Common Failure Modes

1. **Hallucination**: Making up facts
2. **Outdated Information**: Training cutoff issues
3. **Over-elaboration**: Adding unnecessary context
4. **Hedging**: Excessive uncertainty on clear facts
