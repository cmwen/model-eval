#!/usr/bin/env python3
"""
LLM Evaluation Runner - Ollama/LiteLLM Edition

Evaluates local models (primarily Ollama) and cloud models through unified API.
Supports LiteLLM for flexible provider support.
"""

import os
import sys
import json
import yaml
import argparse
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

try:
    from litellm import completion
    LITELLM_AVAILABLE = True
except ImportError:
    LITELLM_AVAILABLE = False
    print("Warning: litellm not installed. Install with: pip install litellm")

try:
    import ollama
    OLLAMA_AVAILABLE = True
except ImportError:
    OLLAMA_AVAILABLE = False


def load_yaml_file(path: str) -> dict:
    """Load a YAML file."""
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def load_model_config(models_file: str = None) -> dict:
    """Load model configurations."""
    if models_file is None:
        script_dir = Path(__file__).parent.parent
        models_file = script_dir / 'config' / 'models.yml'
    return load_yaml_file(str(models_file))


def call_model_litellm(model_id: str, messages: List[Dict], **kwargs) -> Dict:
    """Call model using LiteLLM (supports Ollama, OpenAI, Anthropic, etc.)."""
    if not LITELLM_AVAILABLE:
        raise ImportError("litellm is required. Install with: pip install litellm")
    
    try:
        # LiteLLM automatically handles different providers
        # For Ollama: model_id should be "ollama/model-name"
        # For OpenAI: "gpt-4o" or "openai/gpt-4o"
        # For custom endpoints: set OLLAMA_API_BASE or custom env vars
        
        base_url = os.getenv('OLLAMA_BASE_URL', 'http://localhost:11434')
        if 'ollama/' in model_id:
            # Set base URL for Ollama
            kwargs['api_base'] = base_url
        
        response = completion(
            model=model_id,
            messages=messages,
            **kwargs
        )
        
        return {
            'content': response.choices[0].message.content,
            'model': response.model,
            'usage': {
                'prompt_tokens': response.usage.prompt_tokens,
                'completion_tokens': response.usage.completion_tokens,
                'total_tokens': response.usage.total_tokens
            },
            'finish_reason': response.choices[0].finish_reason
        }
    except Exception as e:
        return {
            'error': str(e),
            'content': None
        }


def call_model_ollama(model_name: str, messages: List[Dict], **kwargs) -> Dict:
    """Call model using native Ollama client."""
    if not OLLAMA_AVAILABLE:
        raise ImportError("ollama is required. Install with: pip install ollama")
    
    try:
        # Remove 'ollama/' prefix if present
        model_name = model_name.replace('ollama/', '')
        
        response = ollama.chat(
            model=model_name,
            messages=messages,
            **kwargs
        )
        
        return {
            'content': response['message']['content'],
            'model': response.get('model', model_name),
            'usage': {
                'prompt_tokens': response.get('prompt_eval_count', 0),
                'completion_tokens': response.get('eval_count', 0),
                'total_tokens': response.get('prompt_eval_count', 0) + response.get('eval_count', 0)
            },
            'finish_reason': 'stop'
        }
    except Exception as e:
        return {
            'error': str(e),
            'content': None
        }


def call_model(model_id: str, messages: List[Dict], use_litellm: bool = True, **kwargs) -> Dict:
    """
    Unified model calling interface.
    
    Args:
        model_id: Model identifier (e.g., "ollama/gpt-oss:20b")
        messages: List of message dicts with 'role' and 'content'
        use_litellm: Whether to use LiteLLM (default) or native client
        **kwargs: Additional parameters for the model
    
    Returns:
        Dict with 'content', 'model', 'usage', and optionally 'error'
    """
    start_time = time.time()
    
    if use_litellm and LITELLM_AVAILABLE:
        result = call_model_litellm(model_id, messages, **kwargs)
    elif 'ollama/' in model_id and OLLAMA_AVAILABLE:
        result = call_model_ollama(model_id, messages, **kwargs)
    else:
        result = {'error': 'No compatible client available', 'content': None}
    
    result['latency_seconds'] = time.time() - start_time
    return result


def evaluate_response(response: str, expected: str, test_case: Dict) -> Dict:
    """
    Simple evaluation logic. Can be extended with custom evaluators.
    
    Returns dict with scores and pass/fail status.
    """
    scores = {}
    
    # Basic exact match (case-insensitive)
    exact_match = response.lower().strip() == expected.lower().strip()
    scores['exact_match'] = 1.0 if exact_match else 0.0
    
    # Containment check (does response contain expected answer?)
    contains_answer = expected.lower().strip() in response.lower()
    scores['contains_answer'] = 1.0 if contains_answer else 0.0
    
    # Length check (not too short, not too verbose)
    response_len = len(response.split())
    expected_len = len(expected.split())
    if response_len == 0:
        scores['length_appropriate'] = 0.0
    elif response_len <= expected_len * 3:  # Allow 3x verbosity
        scores['length_appropriate'] = 1.0
    else:
        scores['length_appropriate'] = 0.5
    
    # Overall pass (if contains answer)
    passed = scores['contains_answer'] >= 1.0
    
    return {
        'scores': scores,
        'passed': passed,
        'overall_score': sum(scores.values()) / len(scores) if scores else 0.0
    }


def run_evaluation(prompt_config: dict, model_id: str = None, use_litellm: bool = True) -> List[Dict]:
    """
    Run evaluation for a prompt configuration.
    
    Args:
        prompt_config: Loaded prompt.yml configuration
        model_id: Model to use (overrides config file)
        use_litellm: Whether to use LiteLLM
    
    Returns:
        List of result dictionaries
    """
    results = []
    model = model_id or prompt_config.get('model', 'ollama/gpt-oss:20b')
    
    # Get base messages (system prompt, etc.)
    base_messages = prompt_config.get('messages', [])
    
    print(f"  Using model: {model}")
    
    for idx, test_case in enumerate(prompt_config.get('testData', []), 1):
        print(f"    Running test {idx}/{len(prompt_config.get('testData', []))}...", end=' ')
        
        # Build messages for this test case
        messages = []
        for msg in base_messages:
            # Replace {{query}} placeholder with actual query
            content = msg.get('content', '')
            if '{{query}}' in content:
                content = content.replace('{{query}}', test_case.get('query', ''))
            
            # Skip if no content
            if content.strip():
                messages.append({
                    'role': msg.get('role', 'user'),
                    'content': content
                })
        
        # Call the model
        response_data = call_model(model, messages, use_litellm=use_litellm)
        
        # Evaluate the response
        evaluation = {}
        if response_data.get('content'):
            evaluation = evaluate_response(
                response_data['content'],
                test_case.get('expected', ''),
                test_case
            )
        
        # Build result object
        result = {
            'timestamp': datetime.now().isoformat(),
            'model': model,
            'query': test_case.get('query', ''),
            'expected': test_case.get('expected', ''),
            'response': response_data.get('content', ''),
            'category': test_case.get('category', 'unknown'),
            'difficulty': test_case.get('difficulty', 'unknown'),
            'latency_seconds': response_data.get('latency_seconds', 0),
            'usage': response_data.get('usage', {}),
            'error': response_data.get('error'),
            **evaluation
        }
        
        results.append(result)
        
        status = "✓" if result.get('passed', False) else "✗"
        print(f"{status} (score: {result.get('overall_score', 0):.2f})")
    
    return results


def find_prompt_files(evaluations_dir: str, category: str = None) -> List[str]:
    """Find all prompt.yml files in evaluations directory."""
    prompt_files = []
    eval_path = Path(evaluations_dir)
    
    if category:
        # Search only in specific category
        category_path = eval_path / category
        if category_path.exists():
            prompt_files = list(category_path.glob('*.prompt.yml'))
    else:
        # Search all categories
        prompt_files = list(eval_path.glob('*/*.prompt.yml'))
    
    return sorted([str(f) for f in prompt_files])


def print_summary(all_results: List[Dict]):
    """Print evaluation summary statistics."""
    if not all_results:
        print("\nNo results to summarize.")
        return
    
    total = len(all_results)
    passed = sum(1 for r in all_results if r.get('passed', False))
    failed = total - passed
    
    avg_score = sum(r.get('overall_score', 0) for r in all_results) / total
    avg_latency = sum(r.get('latency_seconds', 0) for r in all_results) / total
    total_tokens = sum(r.get('usage', {}).get('total_tokens', 0) for r in all_results)
    
    print("\n" + "="*60)
    print("EVALUATION SUMMARY")
    print("="*60)
    print(f"Total Tests:      {total}")
    print(f"Passed:           {passed} ({passed/total*100:.1f}%)")
    print(f"Failed:           {failed} ({failed/total*100:.1f}%)")
    print(f"Average Score:    {avg_score:.3f}")
    print(f"Average Latency:  {avg_latency:.2f}s")
    print(f"Total Tokens:     {total_tokens:,}")
    print("="*60)


def main():
    parser = argparse.ArgumentParser(
        description='Run LLM Evaluations (Ollama/LiteLLM)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run all evaluations with default model (gpt-oss:20b)
  python run_evaluations.py
  
  # Run specific category
  python run_evaluations.py -c 01-knowledge-retrieval
  
  # Test specific model
  python run_evaluations.py -m ollama/llama3.2:3b
  
  # Use native Ollama client instead of LiteLLM
  python run_evaluations.py --no-litellm
  
  # List available evaluations
  python run_evaluations.py --list
        """
    )
    
    parser.add_argument('--category', '-c', help='Specific category to run (e.g., 01-knowledge-retrieval)')
    parser.add_argument('--model', '-m', help='Model to use (e.g., ollama/gpt-oss:20b)')
    parser.add_argument('--output', '-o', default='results', help='Output directory (default: results)')
    parser.add_argument('--list', '-l', action='store_true', help='List available evaluations')
    parser.add_argument('--no-litellm', action='store_true', help='Use native Ollama client instead of LiteLLM')
    parser.add_argument('--models-file', help='Path to models.yml file')
    
    args = parser.parse_args()
    
    # Find evaluations directory
    script_dir = Path(__file__).parent.parent
    evaluations_dir = script_dir / 'evaluations'
    
    if not evaluations_dir.exists():
        print(f"Error: Evaluations directory not found: {evaluations_dir}")
        sys.exit(1)
    
    # Find prompt files
    prompt_files = find_prompt_files(str(evaluations_dir), args.category)
    
    if args.list:
        print("Available evaluations:")
        for pf in prompt_files:
            rel_path = os.path.relpath(pf, evaluations_dir)
            print(f"  - {rel_path}")
        return
    
    if not prompt_files:
        print(f"No evaluations found{' for category: ' + args.category if args.category else ''}.")
        return
    
    # Set up model
    use_litellm = not args.no_litellm
    model = args.model or 'ollama/gpt-oss:20b'
    
    print(f"\n{'='*60}")
    print(f"LLM EVALUATION RUNNER")
    print(f"{'='*60}")
    print(f"Model:            {model}")
    print(f"Client:           {'LiteLLM' if use_litellm else 'Native Ollama'}")
    print(f"Evaluations:      {len(prompt_files)}")
    print(f"{'='*60}\n")
    
    # Run evaluations
    all_results = []
    
    for prompt_file in prompt_files:
        rel_path = os.path.relpath(prompt_file, evaluations_dir)
        print(f"Processing: {rel_path}")
        
        try:
            config = load_yaml_file(prompt_file)
            results = run_evaluation(config, model, use_litellm)
            all_results.extend(results)
        except Exception as e:
            print(f"  Error: {e}")
            continue
    
    # Save results
    if all_results:
        output_dir = Path(args.output)
        output_dir.mkdir(exist_ok=True)
        
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        model_slug = model.replace('/', '_').replace(':', '_')
        output_file = output_dir / f'eval_{model_slug}_{timestamp}.jsonl'
        
        with open(output_file, 'w') as f:
            for result in all_results:
                f.write(json.dumps(result) + '\n')
        
        print(f"\n✓ Results saved to: {output_file}")
        
        # Print summary
        print_summary(all_results)
    else:
        print("\nNo results generated.")


if __name__ == '__main__':
    main()
