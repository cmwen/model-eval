# Context Window Evaluation

**Cognitive Type**: Memory & Attention

## Purpose

Tests the model's ability to handle long contexts:
- Information retrieval from long documents
- Maintaining coherence over extended conversations
- "Needle in a haystack" recall
- Context utilization efficiency

## Test Categories

### 1. Long Document Q&A
- Single document analysis
- Multi-document synthesis
- Specific fact retrieval
- Thematic analysis

### 2. Needle in Haystack
- Finding specific information in long context
- Accuracy at different positions
- Distractor handling

### 3. Extended Conversations
- Multi-turn coherence
- Reference resolution
- Topic tracking
- Memory of earlier context

### 4. Summarization
- Long document summarization
- Key point extraction
- Hierarchical summarization

## Context Length Tiers

| Tier | Token Count | Use Case |
|------|-------------|----------|
| **Short** | 1K-4K | Basic documents |
| **Medium** | 4K-16K | Articles, reports |
| **Long** | 16K-64K | Books, codebases |
| **Ultra-Long** | 64K-200K+ | Enterprise documents |

## Evaluation Metrics

| Metric | Description | Weight |
|--------|-------------|--------|
| **Recall** | Information retrieved | 35% |
| **Accuracy** | Correctness of retrieval | 35% |
| **Position Independence** | Consistent across positions | 20% |
| **Coherence** | Maintains context | 10% |
