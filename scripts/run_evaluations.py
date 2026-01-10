#!/usr/bin/env python3
"""
LLM Evaluation Runner

A simple script to run evaluations defined in prompt.yml files.
"""

import os
import sys
import json
import yaml
import argparse
from datetime import datetime
from pathlib import Path


def load_prompt_file(path: str) -> dict:
    """Load a prompt YAML file."""
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def run_evaluation(prompt_config: dict, model_override: str = None) -> list:
    """
    Run evaluation for a prompt configuration.
    
    This is a placeholder - implement actual model calls and evaluation logic.
    """
    results = []
    model = model_override or prompt_config.get('model', 'openai/gpt-4o')
    
    for test_case in prompt_config.get('testData', []):
        result = {
            'timestamp': datetime.now().isoformat(),
            'model': model,
            'query': test_case.get('query', ''),
            'expected': test_case.get('expected', ''),
            'category': test_case.get('category', 'unknown'),
            'difficulty': test_case.get('difficulty', 'unknown'),
            # Placeholder for actual results
            'response': None,
            'scores': {},
            'passed': None
        }
        results.append(result)
    
    return results


def find_prompt_files(evaluations_dir: str) -> list:
    """Find all prompt.yml files in evaluations directory."""
    prompt_files = []
    for root, dirs, files in os.walk(evaluations_dir):
        for file in files:
            if file.endswith('.prompt.yml'):
                prompt_files.append(os.path.join(root, file))
    return sorted(prompt_files)


def main():
    parser = argparse.ArgumentParser(description='Run LLM Evaluations')
    parser.add_argument('--category', '-c', help='Specific category to run (e.g., 01-knowledge-retrieval)')
    parser.add_argument('--model', '-m', help='Override model for all evaluations')
    parser.add_argument('--output', '-o', default='results', help='Output directory')
    parser.add_argument('--list', '-l', action='store_true', help='List available evaluations')
    args = parser.parse_args()
    
    # Find evaluations directory
    script_dir = Path(__file__).parent.parent
    evaluations_dir = script_dir / 'evaluations'
    
    if not evaluations_dir.exists():
        print(f"Error: Evaluations directory not found: {evaluations_dir}")
        sys.exit(1)
    
    # Find prompt files
    prompt_files = find_prompt_files(str(evaluations_dir))
    
    if args.list:
        print("Available evaluations:")
        for pf in prompt_files:
            rel_path = os.path.relpath(pf, evaluations_dir)
            print(f"  - {rel_path}")
        return
    
    # Filter by category if specified
    if args.category:
        prompt_files = [pf for pf in prompt_files if args.category in pf]
    
    if not prompt_files:
        print("No matching evaluations found.")
        return
    
    print(f"Running {len(prompt_files)} evaluation(s)...")
    
    all_results = []
    for prompt_file in prompt_files:
        print(f"\nProcessing: {prompt_file}")
        config = load_prompt_file(prompt_file)
        results = run_evaluation(config, args.model)
        all_results.extend(results)
        print(f"  Generated {len(results)} test case(s)")
    
    # Save results
    output_dir = Path(args.output)
    output_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    output_file = output_dir / f'evaluation_{timestamp}.jsonl'
    
    with open(output_file, 'w') as f:
        for result in all_results:
            f.write(json.dumps(result) + '\n')
    
    print(f"\nResults saved to: {output_file}")
    print(f"Total test cases: {len(all_results)}")


if __name__ == '__main__':
    main()
