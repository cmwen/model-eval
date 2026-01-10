# Structured Output Evaluation

**Cognitive Type**: Instruction Following

## Purpose

Tests the model's ability to generate responses in specific formats (JSON, YAML, XML, Markdown tables, etc.) that conform to schemas and follow structural requirements.

## Test Categories

### 1. JSON Generation
- Simple objects
- Nested structures
- Arrays and lists
- Schema compliance

### 2. Data Extraction
- Entity extraction to structured format
- Information parsing
- Format conversion

### 3. Schema Compliance
- Required fields
- Data types
- Constraints and validation

### 4. Format Following
- Markdown tables
- CSV generation
- XML structures
- Custom formats

## Evaluation Metrics

| Metric | Description | Weight |
|--------|-------------|--------|
| **Parsability** | Valid syntax | 30% |
| **Schema Compliance** | Matches schema | 30% |
| **Completeness** | All required fields | 25% |
| **Accuracy** | Correct values | 15% |

## Expected Behavior

- Valid, parseable output
- All required fields present
- Correct data types
- No extra formatting (like markdown code blocks when not requested)

## Common Failure Modes

1. **Invalid Syntax**: Malformed JSON/YAML
2. **Missing Fields**: Incomplete objects
3. **Type Errors**: Wrong data types
4. **Extra Formatting**: Unnecessary markdown/text
5. **Hallucinated Fields**: Adding unrequested fields
