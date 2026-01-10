# AGENTS.md - Guidelines for AI Agents

This document provides instructions for AI agents working with this LLM evaluation repository.

## 🎯 Repository Purpose

This repository evaluates LLM capabilities with a **primary focus on local Ollama models**, using standardized tests to understand model strengths, weaknesses, and optimal use cases.

### Key Focus
- **Primary Target**: Ollama models running locally (zero cost inference)
- **Default Model**: `gpt-oss:20b` - OpenAI's open-weight model with excellent reasoning
- **Secondary Support**: Cloud models via LiteLLM (OpenAI, Anthropic, Google, etc.)
- **Flexibility**: Configurable for any AI proxy or custom endpoint

## 🏗️ Architecture

### Inference Layer
- **LiteLLM (Default)**: Unified interface supporting 100+ LLM providers
- **Native Ollama Client**: Direct connection to Ollama API (use `--no-litellm` flag)
- **Custom Proxies**: Configurable via environment variables

### Model Configuration
- Primary: `config/models.yml` - Model definitions and capabilities
- Runtime: Environment variables (`.env` file)
- Override: Command-line arguments (`-m model_name`)

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
│   ├── models.yml         # Ollama and cloud model definitions
│   └── evaluators.yml     # Evaluation metrics configuration
├── datasets/              # Test data and ground truth
├── results/               # Evaluation outputs (JSONL format)
├── scripts/
│   ├── run_evaluations.py  # Main evaluation runner
│   └── evaluators/         # Custom evaluation logic
└── .env                   # Configuration (not in git)
```

## � Running Evaluations

### Command-Line Interface

```bash
# Basic usage - all evaluations, default model
python scripts/run_evaluations.py

# Specific category
python scripts/run_evaluations.py -c 01-knowledge-retrieval

# Different model
python scripts/run_evaluations.py -m ollama/ministral-3

# Native Ollama client (bypass LiteLLM)
python scripts/run_evaluations.py --no-litellm

# List available evaluations
python scripts/run_evaluations.py --list

# Custom output directory
python scripts/run_evaluations.py -o my_results/
```

### Batch Evaluation (Multiple Models)

```bash
# Test all configured Ollama models
for model in gpt-oss:20b gpt-oss:120b ministral-3:8b ministral-3:14b qwen3:14b qwen3:30b gemma3:12b gemma3:27b llama3.2:3b; do
    echo "Testing $model..."
    python scripts/run_evaluations.py -m ollama/$model
done
```

## 🔌 Model Configuration

### Adding Ollama Models

Edit `config/models.yml`:

```yaml
models:
  - id: ollama/your-model:tag
    name: Your Model Name
    provider: ollama
    capabilities:
      - text
      - code_generation  # or reasoning, tool_calling, vision, audio
    context_window: 32768
    cost_per_1k_input: 0.0    # Local = free
    cost_per_1k_output: 0.0
    notes: "Description of model characteristics"
```

### Configuring API Proxies

Create or edit `.env`:

```bash
# Ollama (default: http://localhost:11434)
OLLAMA_BASE_URL=http://your-ollama-server:11434

# LiteLLM Proxy
LITELLM_API_BASE=http://localhost:8000

# Cloud Provider Keys (optional)
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
GOOGLE_API_KEY=...
```

## 📊 Evaluation Script Details

### Flow
1. **Load Configuration**: Read prompt files (`.prompt.yml`) from `evaluations/`
2. **Model Selection**: Use CLI override, or file default, or system default
3. **Message Construction**: Build messages from template + test data
4. **Model Invocation**: Call via LiteLLM or native Ollama client
5. **Response Evaluation**: Score against expected outputs
6. **Result Storage**: Save to `results/` as JSONL with timestamps

### Evaluation Metrics

Current implementation provides:
- `exact_match`: Exact string match (case-insensitive)
- `contains_answer`: Expected answer is present in response
- `length_appropriate`: Response not excessively verbose
- `overall_score`: Average of all metrics (0.0-1.0)
- `passed`: Boolean (based on contains_answer)

### Extending Evaluation Logic

To add custom evaluators, edit `scripts/run_evaluations.py`:

```python
def evaluate_response(response: str, expected: str, test_case: Dict) -> Dict:
    scores = {}
    
    # Add your custom metric
    scores['your_metric'] = compute_your_score(response, expected)
    
    # ... rest of evaluation logic
    return {'scores': scores, 'passed': passed, 'overall_score': avg}
```

## 📝 Prompt File Format

All evaluation prompts use YAML format:

```yaml
messages:
  - role: system
    content: System prompt defining assistant behavior
  - role: user
    content: "{{query}}"  # Template variable replaced at runtime
model: ollama/qwen2.5-coder:20b  # Default model for this evaluation
testData:
  - query: "What is 2+2?"
    expected: "4"
    category: "math"
    difficulty: "easy"
  - query: "Explain quantum entanglement"
    expected: "description of quantum correlation phenomena"
    category: "physics"
    difficulty: "hard"
```

### Key Fields

- `messages`: Array of message objects (system, user, assistant)
- `model`: Default model ID (can be overridden via CLI)
- `testData`: Array of test cases with:
  - `query`: The question/prompt to evaluate
  - `expected`: Expected answer or description of correct response
  - `category`: Test category (e.g., "math", "history", "code")
  - `difficulty`: "easy", "medium", or "hard"

### Adding Test Cases

1. Navigate to the appropriate category folder (e.g., `evaluations/01-knowledge-retrieval/`)
2. Edit the `*.prompt.yml` file
3. Add entries to the `testData` array
4. Include clear expected outputs

### Creating New Evaluation Categories

1. Create numbered folder: `evaluations/13-your-category/`
2. Add `README.md` describing the evaluation purpose
3. Create prompt file: `your-category.prompt.yml`
4. Follow the YAML structure above

## 🔄 Output Format

Results are saved to `results/` in JSONL format (one JSON object per line):

```json
{
  "timestamp": "2026-01-10T15:30:45.123456",
  "model": "ollama/qwen2.5-coder:20b",
  "query": "What year did World War II end?",
  "expected": "1945",
  "response": "World War II ended in 1945.",
  "category": "history",
  "difficulty": "easy",
  "latency_seconds": 1.234,
  "usage": {
    "prompt_tokens": 50,
    "completion_tokens": 15,
    "total_tokens": 65
  },
  "scores": {
    "exact_match": 0.0,
    "contains_answer": 1.0,
    "length_appropriate": 1.0
  },
  "passed": true,
  "overall_score": 0.67
}
```

### Result Analysis

You can analyze results using standard JSONL tools:

```bash
# Count total tests
wc -l results/eval_*.jsonl

# Count passed tests
grep '"passed":true' results/eval_*.jsonl | wc -l

# Extract specific fields
jq -r '[.model, .overall_score, .latency_seconds] | @csv' results/eval_*.jsonl

# Average score by category
jq -r '[.category, .overall_score] | @csv' results/eval_*.jsonl | \
  awk -F, '{sum[$1]+=$2; count[$1]++} END {for(c in sum) print c, sum[c]/count[c]}'
```

### System 1 vs System 2 Thinking

| Type | Description | Examples |
|------|-------------|----------|
| **System 1** | Fast, intuitive, automatic | Fact recall, simple Q&A, pattern matching |
| **System 2** | Slow, analytical, deliberate | Reasoning, planning, complex analysis |

### Category Details

#### 01-knowledge-retrieval (System 1)
- **Tests**: Factual accuracy, data lookup, simple Q&A
- **Metrics**: Accuracy, relevance, groundedness
- **Best Models**: All Ollama models perform well on factual questions

#### 02-reasoning (System 2)
- **Tests**: Multi-step logic, analysis, inference, complex problem solving
- **Metrics**: Coherence, logical validity, depth
- **Best Models**: Larger models (20B+) like qwen2.5-coder:20b perform better

#### 03-structured-output
- **Tests**: JSON generation, schema compliance, format following
- **Metrics**: Schema validity, completeness, accuracy
- **Best Models**: Code-focused models excel (qwen2.5-coder)

#### 04-tool-calling
- **Tests**: Function argument preparation, response parsing, tool selection
- **Metrics**: Correct parameters, proper types, error handling
- **Best Models**: Models with explicit tool_calling capability

#### 05-web-tools
- **Tests**: Search query formation, URL handling, content extraction
- **Metrics**: Query quality, information accuracy
- **Best Models**: General-purpose models work well

#### 06-image-support
- **Tests**: Image description, object detection, OCR, visual reasoning
- **Metrics**: Accuracy, detail level, relevance
- **Best Models**: Vision-capable models only (most Ollama models don't support vision yet)

#### 07-audio-support
- **Tests**: Transcription, audio understanding, speech analysis
- **Metrics**: WER (Word Error Rate), semantic accuracy
- **Best Models**: Audio-capable models only (most Ollama models don't support audio yet)

#### 08-code-generation
- **Tests**: Code writing, debugging, explanation, refactoring
- **Metrics**: Correctness, efficiency, readability
- **Best Models**: qwen2.5-coder:20b excels at code tasks

#### 09-safety
- **Tests**: Harmful content rejection, bias detection, alignment
- **Metrics**: Refusal rate, safety compliance
- **Best Models**: All models should have safety guardrails

#### 10-multilingual
- **Tests**: Translation, cross-lingual understanding, cultural awareness
- **Metrics**: BLEU score, semantic preservation
- **Best Models**: Multilingual models (qwen, gemma)

#### 11-context-window
- **Tests**: Long document Q&A, needle-in-haystack, context retention
- **Metrics**: Recall accuracy, context utilization
- **Best Models**: Models with larger context windows (32K+)

#### 12-consistency
- **Tests**: Same prompt multiple times, response variance
- **Metrics**: Response variance, semantic stability
- **Best Models**: All models; use temperature=0 for better consistency

## 📋 Best Practices

1. **Test Isolation**: Each test case should be independent
2. **Clear Criteria**: Define expected outputs or evaluation rubrics
3. **Version Control**: Track prompt changes over time
4. **Documentation**: Update README files when adding tests
5. **Reproducibility**: Use fixed seeds where possible (temperature=0)
6. **Model Naming**: Use consistent format `ollama/model-name:tag`
7. **Results Storage**: Always save results with timestamps for tracking

## 🚨 Important Notes

- Default model is `ollama/gpt-oss:20b` - OpenAI's open-weight model with excellent reasoning
- Make sure Ollama service is running: `ollama serve`
- Pull models before testing: `ollama pull gpt-oss:20b`
- Do not modify `config/` files without updating documentation
- Keep test data in `datasets/` separate from prompts
- Store results in `results/` with timestamps
- Use consistent model naming: `ollama/model-name:tag`

## 🔗 Related Tools

- `aitk-get_evaluation_code_gen_best_practices` - For generating evaluation code
- `aitk-evaluation_planner` - For planning new evaluations
- `aitk-evaluation_agent_runner_best_practices` - For collecting model responses
