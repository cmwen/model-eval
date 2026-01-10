# Tool Calling Evaluation

**Cognitive Type**: Agent Capability

## Purpose

Tests the model's ability to:
1. Correctly identify when to use tools/functions
2. Prepare proper input arguments
3. Handle tool responses appropriately
4. Chain multiple tool calls when needed

## Test Categories

### 1. Single Tool Calls
- Correct tool selection
- Proper argument formatting
- Type compliance

### 2. Multi-Tool Chains
- Sequential tool usage
- Passing results between tools
- Dependency handling

### 3. Error Handling
- Graceful degradation
- Retry logic
- User communication

### 4. Edge Cases
- Optional parameters
- Complex nested arguments
- Ambiguous requests

## Evaluation Metrics

| Metric | Description | Weight |
|--------|-------------|--------|
| **Tool Selection** | Correct tool chosen | 25% |
| **Argument Accuracy** | Correct parameters | 35% |
| **Type Compliance** | Proper data types | 20% |
| **Response Handling** | Proper use of results | 20% |

## Expected Behavior

- Select appropriate tools
- Format arguments correctly
- Handle responses gracefully
- Communicate clearly about tool usage

## Common Failure Modes

1. **Wrong Tool**: Selecting incorrect function
2. **Missing Arguments**: Forgetting required params
3. **Type Mismatch**: Wrong data types
4. **Hallucinated Tools**: Calling non-existent functions
5. **Poor Error Handling**: Not recovering from failures
