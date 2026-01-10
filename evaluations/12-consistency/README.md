# Consistency Evaluation

**Cognitive Type**: Reliability & Stability

## Purpose

Tests the model's response consistency:
- Same question, same answer (when appropriate)
- Semantic consistency across phrasings
- Temperature sensitivity
- Reproducibility

## Test Categories

### 1. Factual Consistency
- Same facts across runs
- No contradictions in repeated queries
- Stable numerical answers

### 2. Semantic Stability
- Similar meaning with different phrasings
- Paraphrase handling
- Synonym consistency

### 3. Temperature Analysis
- Response variation at different temperatures
- Quality vs creativity tradeoff
- Determinism at temp=0

### 4. Multi-Turn Consistency
- Consistent information across turns
- No self-contradiction
- Stable persona/style

## Evaluation Metrics

| Metric | Description | Weight |
|--------|-------------|--------|
| **Self-BLEU** | Response similarity | 30% |
| **Semantic Similarity** | Meaning preservation | 30% |
| **Contradiction Rate** | Self-contradictions | 25% |
| **Variance** | Response variability | 15% |

## Testing Methodology

1. Run same prompt N times (typically 5-10)
2. Compare responses for consistency
3. Test at multiple temperature settings
4. Use semantic similarity metrics

## Expected Behavior

- Factual answers should be consistent
- Creative tasks may vary appropriately
- No self-contradictions
- Stable core information
