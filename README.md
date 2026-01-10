# LLM Model Evaluation Framework

A comprehensive evaluation suite for testing and understanding the capabilities and limitations of Large Language Models (LLMs).

## 🎯 Purpose

This repository provides a structured approach to evaluate LLMs across multiple dimensions:
- Understand model strengths and weaknesses
- Compare different models objectively
- Identify the right model for specific use cases
- Track model performance over time

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
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install azure-ai-evaluation openai anthropic
```

### Running Evaluations

Each evaluation category contains:
- `*.prompt.yml` - Prompt templates with test data
- `README.md` - Category-specific documentation
- Test cases and expected behaviors

## 📈 Understanding Results

### Metrics Explained

- **Relevance**: How well the response addresses the query
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

1. Create a new folder under `evaluations/`
2. Add a `README.md` describing the evaluation
3. Create prompt files with test cases
4. Define expected outputs or evaluation criteria

## 📊 Model Comparison Template

Use this template to compare models:

| Model | Knowledge | Reasoning | Structured | Tools | Vision | Cost/1K |
|-------|-----------|-----------|------------|-------|--------|---------|
| GPT-4o | - | - | - | - | - | - |
| Claude 3.5 | - | - | - | - | - | - |
| Gemini 1.5 | - | - | - | - | - | - |
| Llama 3 | - | - | - | - | - | - |

## 🤝 Contributing

1. Add new test cases to existing categories
2. Create new evaluation categories
3. Improve evaluation metrics
4. Document findings and insights

## 📚 Resources

- [Azure AI Evaluation SDK](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-sdk)
- [OpenAI Evals](https://github.com/openai/evals)
- [LM Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness)

## 📝 License

MIT License - Feel free to use and modify for your evaluation needs.
