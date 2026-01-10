# LLM Model Evaluation Framework

A comprehensive evaluation suite for testing and comparing Large Language Models, with primary focus on **local Ollama models** running on your machine.

## 🎯 Purpose

Evaluate and compare LLMs running locally via Ollama, with support for cloud models through LiteLLM or AI proxies:
- **Primary Focus**: Ollama local models (gpt-oss, ministral-3, qwen3, gemma3, llama3.2, etc.)
- **Default Model**: `gpt-oss:20b` (OpenAI's open-weight model with excellent reasoning)
- **Flexible Integration**: Works with LiteLLM for OpenAI, Anthropic, Google, and custom endpoints
- Understand model strengths and weaknesses objectively
- Compare different models across standardized benchmarks
- Identify the right model for specific use cases

## 🚀 Quick Start

### Prerequisites

1. **Install Ollama** (required for local models)
   ```bash
   # Linux
   curl -fsSL https://ollama.com/install.sh | sh
   
   # macOS
   brew install ollama
   
   # Or download from https://ollama.com
   ```

2. **Pull the default model**
   ```bash
   ollama pull gpt-oss:20b
   ```

3. **Install Python dependencies**
   ```bash
   # Create virtual environment (recommended)
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

### Running Evaluations

```bash
# Start Ollama service (if not already running)
ollama serve

# Run all evaluations with default model (gpt-oss:20b)
python scripts/run_evaluations.py

# Run specific category
python scripts/run_evaluations.py -c 01-knowledge-retrieval

# Test different model
python scripts/run_evaluations.py -m ollama/llama3.2:3b

# Test multiple models in sequence
for model in gpt-oss:20b gpt-oss:120b ministral-3:8b qwen3:14b gemma3:12b llama3.2:3b; do
    python scripts/run_evaluations.py -m ollama/$model
done

# List available evaluations
python scripts/run_evaluations.py --list
```

## 📦 Tested Models

### Ollama Models (Local - Zero Cost)

| Model ID | Name | Size | Best For | Notes |
|----------|------|------|----------|-------|
| `gpt-oss:20b` | GPT-OSS 20B | 20B | Reasoning, general | **Default** - OpenAI's open-weight |
| `gpt-oss:120b` | GPT-OSS 120B | 120B | Complex reasoning | Larger variant with enhanced capabilities |
| `ministral-3:3b` | Ministral 3 3B | 3B | Edge deployment | Compact reasoning model |
| `ministral-3:8b` | Ministral 3 8B | 8B | Fast inference | Good reasoning/speed tradeoff |
| `ministral-3:14b` | Ministral 3 14B | 14B | Advanced reasoning | Powerful reasoning model |
| `qwen3:4b` | Qwen 3 4B | 4B | General purpose | Lightweight Qwen3 |
| `qwen3:8b` | Qwen 3 8B | 8B | General tasks | Fast and capable |
| `qwen3:14b` | Qwen 3 14B | 14B | Balanced | Good balance of speed/capability |
| `qwen3:30b` | Qwen 3 30B | 30B | Code & reasoning | Powerful Qwen3 variant |
| `gemma3:2b` | Gemma 3 2B | 2B | Ultra-lightweight | Google's efficient model |
| `gemma3:4b` | Gemma 3 4B | 4B | Lightweight | Google's compact model |
| `gemma3:12b` | Gemma 3 12B | 12B | General purpose | Mid-sized Google model |
| `gemma3:27b` | Gemma 3 27B | 27B | Advanced | Larger Google model |
| `gemma3-nano:2b` | Gemma 3 Nano 2B | 2B | Edge devices | Optimized for efficiency |
| `gemma3-nano:4b` | Gemma 3 Nano 4B | 4B | Mobile/edge | Fast execution on limited hardware |
| `llama3.2:1b` | Llama 3.2 1B | 1B | Ultra-lightweight | Meta's minimal model |
| `llama3.2:3b` | Llama 3.2 3B | 3B | General chat | Meta's compact model with tools |

### Cloud Models (via LiteLLM)

Configured in [config/models.yml](config/models.yml) - requires API keys:
- OpenAI: GPT-4o, GPT-4o-mini, O1
- Anthropic: Claude 3.5 Sonnet, Claude 3 Opus  
- Google: Gemini 1.5 Pro, Gemini 1.5 Flash

## 🔧 Configuration

### Environment Variables

Create a `.env` file for custom configurations:

```bash
# Ollama Configuration
OLLAMA_BASE_URL=http://localhost:11434  # Default

# For cloud models (optional)
OPENAI_API_KEY=your-key-here
ANTHROPIC_API_KEY=your-key-here
GOOGLE_API_KEY=your-key-here

# Custom AI Proxy
LITELLM_API_BASE=http://your-proxy:8000
```

### Model Configuration

Edit [config/models.yml](config/models.yml) to add models or modify settings:

```yaml
models:
  - id: ollama/your-model:tag
    name: Your Model Name
    provider: ollama
    capabilities:
      - text
      - code_generation
    context_window: 8192
```

## 📊 Evaluation Categories

### Core Capabilities

| Category | Description | Cognitive Type |
|----------|-------------|----------------|
| **Knowledge Retrieval** | Simple factual questions, data lookup | System 1 (Fast) |
| **Reasoning** | Complex analysis, multi-step logic | System 2 (Slow) |
| **Structured Output** | JSON, YAML, schema-compliant responses | Instruction Following |
| **Tool Calling** | Function preparation and response handling | Agent Capability |

### Modality Support

| Category | Description |
|----------|-------------|
| **Web Tools** | Web search, URL fetching, browsing |
| **Image Support** | Vision understanding, image analysis |
| **Audio Support** | Speech-to-text, audio understanding |

### Advanced Evaluations

| Category | Description |
|----------|-------------|
| **Code Generation** | Writing, debugging, explaining code |
| **Safety & Alignment** | Harmful content rejection, bias detection |
| **Multilingual** | Performance across different languages |
| **Context Window** | Long document handling, recall accuracy |
| **Consistency** | Response stability across runs |
| **Latency & Cost** | Response time and token efficiency |

## 📁 Project Structure

```
model-eval/
├── README.md                    # This file
├── AGENTS.md                    # Guidelines for AI agents
├── config/
│   ├── models.yml               # Model configurations
│   └── evaluators.yml           # Evaluator settings
├── evaluations/
│   ├── 01-knowledge-retrieval/  # System 1: Simple Q&A
│   ├── 02-reasoning/            # System 2: Complex thinking
│   ├── 03-structured-output/    # Format compliance
│   ├── 04-tool-calling/         # Function calling
│   ├── 05-web-tools/            # Web interaction
│   ├── 06-image-support/        # Vision capabilities
│   ├── 07-audio-support/        # Audio processing
│   ├── 08-code-generation/      # Coding tasks
│   ├── 09-safety/               # Safety guardrails
│   ├── 10-multilingual/         # Language support
│   ├── 11-context-window/       # Long context handling
│   └── 12-consistency/          # Response stability
├── datasets/                    # Test data files
├── results/                     # Evaluation outputs
└── scripts/                     # Automation scripts
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Azure AI Evaluation SDK (recommended)
- API keys for models you want to evaluate

### Installation

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Pull Ollama models you want to test
ollama pull gpt-oss:20b
ollama pull ministral-3
ollama pull llama3.2:3b
```

### Running Evaluations

```bash
# Make sure Ollama is running
ollama serve

# Run evaluations (see Quick Start section above for more examples)
python scripts/run_evaluations.py
```

## 📈 Understanding Results

Results are saved as JSONL files in the `results/` directory with the following structure:

```json
{
  "timestamp": "2026-01-10T...",
  "model": "ollama/gpt-oss:20b",
  "query": "What year did World War II end?",
  "expected": "1945",
  "response": "World War II ended in 1945.",
  "category": "history",
  "difficulty": "easy",
  "latency_seconds": 1.23,
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

### Metrics Explained

- **exact_match**: Response exactly matches expected output (case-insensitive)
- **contains_answer**: Response contains the expected answer
- **length_appropriate**: Response length is reasonable (not too verbose)
- **overall_score**: Average of all metric scores (0.0 to 1.0)
- **passed**: Boolean indicating if test passed (based on contains_answer)
- **latency_seconds**: Time taken to generate response

## 🔌 Using Custom AI Proxies / LiteLLM

This framework is designed to work with any AI proxy that implements OpenAI-compatible APIs:

### With LiteLLM Proxy

```bash
# Start LiteLLM proxy (separate terminal)
litellm --config litellm_config.yml

# Point to proxy
export LITELLM_API_BASE=http://localhost:8000

# Run evaluations
python scripts/run_evaluations.py -m openai/gpt-4o
```

### With Custom Endpoints

```bash
# Set custom endpoint
export OLLAMA_BASE_URL=http://your-server:11434

# Or edit config/models.yml to add custom endpoints
```

### Using Native Ollama Client

```bash
# Bypass LiteLLM and use native Ollama client
python scripts/run_evaluations.py --no-litellm
```
- **Groundedness**: Factual accuracy based on provided context
- **Coherence**: Logical flow and readability
- **Fluency**: Language quality and naturalness
- **Similarity**: Semantic match to expected output

### Interpreting System 1 vs System 2

| Aspect | System 1 (Fast) | System 2 (Slow) |
|--------|-----------------|-----------------|
| **Tasks** | Fact recall, simple lookup | Analysis, reasoning |
| **Expected Speed** | Near-instant | May need more tokens |
| **Accuracy** | High for trained data | Varies by complexity |

## 🧪 Adding New Evaluations

1. Create a new folder under `evaluations/` (e.g., `13-your-category/`)
2. Add a `README.md` describing the evaluation category
3. Create prompt files with test cases (e.g., `your-test.prompt.yml`)
4. Define expected outputs or evaluation criteria

Example prompt file structure:

```yaml
messages:
  - role: system
    content: You are a helpful assistant.
  - role: user
    content: "{{query}}"
model: ollama/gpt-oss:20b
testData:
  - query: "Your test question"
    expected: "Expected answer"
    category: "your_category"
    difficulty: "easy"
```

## 📊 Model Comparison

After running evaluations, compare model performance:

| Model | Avg Score | Pass Rate | Avg Latency | Total Tokens |
|-------|-----------|-----------|-------------|--------------|
| gpt-oss:20b | 0.85 | 92% | 2.3s | 15,234 |
| ministral-3 | 0.78 | 85% | 1.8s | 12,456 |
| llama3.2:3b | 0.72 | 78% | 0.9s | 9,876 |
| gemma2:9b | 0.76 | 81% | 1.4s | 11,234 |

*Example data - run your own evaluations for actual results*

## 🤝 Contributing

Contributions welcome! You can:
1. Add new test cases to existing categories
2. Create new evaluation categories
3. Improve evaluation metrics and logic
4. Test additional Ollama models
5. Document findings and insights

## 🐛 Troubleshooting

### Ollama Connection Issues

```bash
# Check if Ollama is running
curl http://localhost:11434/api/tags

# Start Ollama service
ollama serve

# Check available models
ollama list
```

### Model Not Found

```bash
# Pull the model first
ollama pull gpt-oss:20b

# Verify it's available
ollama list
```

### LiteLLM Import Errors

```bash
# Reinstall with all dependencies
pip install --upgrade litellm

# Or use native Ollama client
python scripts/run_evaluations.py --no-litellm
```

## 📚 Resources

- [Ollama Documentation](https://ollama.com/docs)
- [LiteLLM Documentation](https://docs.litellm.ai/)
- [Azure AI Evaluation SDK](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-sdk)
- [Model Evaluation Best Practices](https://platform.openai.com/docs/guides/evaluation)

## 📝 License

MIT License - Feel free to use and modify for your evaluation needs.
