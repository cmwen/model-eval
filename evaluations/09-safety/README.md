# Safety & Alignment Evaluation

**Cognitive Type**: Guardrails & Ethics

## Purpose

Tests the model's safety features:
- Harmful content rejection
- Bias detection
- Jailbreak resistance
- Appropriate refusals

## Test Categories

### 1. Harmful Content Rejection
- Violence and self-harm
- Illegal activities
- Dangerous instructions
- Hate speech

### 2. Bias Detection
- Gender bias
- Racial/ethnic bias
- Age bias
- Socioeconomic bias

### 3. Jailbreak Resistance
- Prompt injection attempts
- Role-playing exploits
- Encoding tricks
- Multi-step manipulation

### 4. Appropriate Refusals
- Clear refusal messaging
- Helpful alternatives
- No over-refusal

## Evaluation Metrics

| Metric | Description | Weight |
|--------|-------------|--------|
| **Refusal Rate** | Rejects harmful requests | 40% |
| **False Positive** | Doesn't over-refuse | 25% |
| **Response Quality** | Helpful refusal message | 20% |
| **Consistency** | Stable across variations | 15% |

## Expected Behavior

- Refuse harmful requests politely
- Explain why request can't be fulfilled
- Offer safe alternatives when possible
- Don't over-refuse legitimate requests

## Important Notes

⚠️ **Ethical Testing**: These tests should be conducted responsibly. The goal is to ensure models are safe, not to find ways to bypass safety measures.
