"""
Custom JSON Validator Evaluator

Validates that model output is valid JSON.
"""

import json
from typing import Any, Dict


def evaluate(response: str, **kwargs) -> Dict[str, Any]:
    """
    Evaluate if the response is valid JSON.
    
    Returns:
        dict with 'score' (1-5) and 'details'
    """
    try:
        # Try to parse as JSON
        parsed = json.loads(response)
        
        return {
            'score': 5,
            'valid': True,
            'parsed_type': type(parsed).__name__,
            'details': 'Valid JSON'
        }
    except json.JSONDecodeError as e:
        return {
            'score': 1,
            'valid': False,
            'error': str(e),
            'details': f'Invalid JSON: {e}'
        }


def main():
    # Test the evaluator
    test_cases = [
        '{"name": "John", "age": 30}',
        'not valid json',
        '[1, 2, 3]',
        '{"nested": {"key": "value"}}',
    ]
    
    for case in test_cases:
        result = evaluate(case)
        print(f"Input: {case[:50]}...")
        print(f"Result: {result}")
        print()


if __name__ == '__main__':
    main()
