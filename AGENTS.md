# AGENTS.md - Guidelines for AI Agents

This document provides instructions for AI agents working with this LLM evaluation repository.

## 🎯 Repository Purpose

This repository evaluates LLM capabilities across multiple dimensions to understand model strengths, weaknesses, and optimal use cases.

## 📁 Project Structure

```
model-eval/
├── evaluations/           # Core evaluation prompts organized by category
│   ├── 01-knowledge-retrieval/  # System 1: Fast, factual responses
│   ├── 02-reasoning/            # System 2: Complex, analytical tasks
│   ├── 03-structured-output/    # Schema/format compliance
│   ├── 04-tool-calling/         # Function calling capabilities
│   ├── 05-web-tools/            # Web search and browsing
│   ├── 06-image-support/        # Vision and image analysis
│   ├── 07-audio-support/        # Audio/speech processing
│   ├── 08-code-generation/      # Coding tasks
│   ├── 09-safety/               # Safety and alignment
│   ├── 10-multilingual/         # Multi-language support
│   ├── 11-context-window/       # Long context handling
│   └── 12-consistency/          # Response stability
├── config/                # Model and evaluator configurations
├── datasets/              # Test data and ground truth
├── results/               # Evaluation outputs
└── scripts/               # Automation and helper scripts
```

## 📝 Prompt File Format

All evaluation prompts use YAML format with this structure:

```yaml
messages:
  - role: system
    content: System prompt defining behavior
  - role: user
    content: User query or task
model: provider/model-name
testData:
  - input: "test input"
    expected: "expected output or criteria"
evaluators:
  - name: EvaluatorName
    uses: evaluator/reference
```

## 🔧 Working with Evaluations

### Adding New Test Cases

1. Navigate to the appropriate category folder
2. Edit the `*.prompt.yml` file
3. Add test cases to the `testData` array
4. Include expected outputs or evaluation criteria

### Creating New Evaluation Categories

1. Create a numbered folder under `evaluations/`
2. Add a `README.md` describing the category
3. Create prompt files for different test scenarios
4. Define appropriate evaluators

### Evaluation Naming Conventions

- **Files**: `category-name.prompt.yml`
- **Folders**: `##-category-name/` (numbered for ordering)
- **Tests**: Descriptive names in test data

## 🏷️ Evaluation Categories Explained

### System 1 vs System 2 Thinking

| Type | Description | Examples |
|------|-------------|----------|
| **System 1** | Fast, intuitive, automatic | Fact recall, simple Q&A, pattern matching |
| **System 2** | Slow, analytical, deliberate | Reasoning, planning, complex analysis |

### Category Details

#### 01-knowledge-retrieval
- Tests: Factual accuracy, data lookup, simple Q&A
- Metrics: Accuracy, relevance, groundedness

#### 02-reasoning
- Tests: Multi-step logic, analysis, inference
- Metrics: Coherence, logical validity, depth

#### 03-structured-output
- Tests: JSON generation, schema compliance, format following
- Metrics: Schema validity, completeness, accuracy

#### 04-tool-calling
- Tests: Function argument preparation, response parsing
- Metrics: Correct parameters, proper types, error handling

#### 05-web-tools
- Tests: Search query formation, URL handling, content extraction
- Metrics: Query quality, information accuracy

#### 06-image-support
- Tests: Image description, object detection, OCR
- Metrics: Accuracy, detail level, relevance

#### 07-audio-support
- Tests: Transcription, audio understanding
- Metrics: WER (Word Error Rate), semantic accuracy

#### 08-code-generation
- Tests: Code writing, debugging, explanation
- Metrics: Correctness, efficiency, readability

#### 09-safety
- Tests: Harmful content rejection, bias detection
- Metrics: Refusal rate, safety compliance

#### 10-multilingual
- Tests: Translation, cross-lingual understanding
- Metrics: BLEU score, semantic preservation

#### 11-context-window
- Tests: Long document Q&A, needle-in-haystack
- Metrics: Recall accuracy, context utilization

#### 12-consistency
- Tests: Same prompt multiple times
- Metrics: Response variance, semantic stability

## 🔄 Running Evaluations

### With Azure AI Evaluation SDK

```python
from azure.ai.evaluation import evaluate

result = evaluate(
    data="path/to/test_data.jsonl",
    evaluators={"relevance": relevance_evaluator},
    evaluator_config={...}
)
```

### Output Format

Results are saved to `results/` in JSONL format:
```json
{"model": "gpt-4o", "category": "reasoning", "score": 0.85, "details": {...}}
```

## 📋 Best Practices

1. **Test Isolation**: Each test case should be independent
2. **Clear Criteria**: Define expected outputs or evaluation rubrics
3. **Version Control**: Track prompt changes over time
4. **Documentation**: Update README files when adding tests
5. **Reproducibility**: Use fixed seeds where possible

## 🚨 Important Notes

- Do not modify `config/` files without updating documentation
- Keep test data in `datasets/` separate from prompts
- Store results in `results/` with timestamps
- Use consistent model naming: `provider/model-name`

## 🔗 Related Tools

- `aitk-get_evaluation_code_gen_best_practices` - For generating evaluation code
- `aitk-evaluation_planner` - For planning new evaluations
- `aitk-evaluation_agent_runner_best_practices` - For collecting model responses
