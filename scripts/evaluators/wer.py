"""
Word Error Rate (WER) Evaluator

Calculates Word Error Rate for transcription evaluation.
"""

from typing import Any, Dict, List


def levenshtein_distance(s1: List[str], s2: List[str]) -> int:
    """Calculate the Levenshtein distance between two sequences."""
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


def calculate_wer(reference: str, hypothesis: str) -> float:
    """
    Calculate Word Error Rate.
    
    WER = (S + D + I) / N
    where:
        S = substitutions
        D = deletions
        I = insertions
        N = number of words in reference
    """
    ref_words = reference.lower().split()
    hyp_words = hypothesis.lower().split()
    
    if len(ref_words) == 0:
        return 0.0 if len(hyp_words) == 0 else 1.0
    
    distance = levenshtein_distance(ref_words, hyp_words)
    wer = distance / len(ref_words)
    
    return min(wer, 1.0)  # Cap at 1.0


def evaluate(response: str, expected: str, **kwargs) -> Dict[str, Any]:
    """
    Evaluate transcription accuracy using WER.
    
    Returns:
        dict with 'score' (1-5), 'wer', and 'details'
    """
    wer = calculate_wer(expected, response)
    
    # Convert WER to 1-5 score (lower WER = higher score)
    # WER of 0 = score 5, WER of 0.5+ = score 1
    score = max(1, 5 - (wer * 8))
    score = min(5, score)
    
    return {
        'score': round(score, 2),
        'wer': round(wer, 4),
        'reference_words': len(expected.split()),
        'hypothesis_words': len(response.split()),
        'details': f'WER: {wer:.2%}'
    }


def main():
    # Test the evaluator
    test_cases = [
        ("hello world", "hello world"),
        ("the quick brown fox", "the quick brown dog"),
        ("this is a test", "this is test"),
        ("perfect transcription", "completely different text"),
    ]
    
    for ref, hyp in test_cases:
        result = evaluate(hyp, ref)
        print(f"Reference: '{ref}'")
        print(f"Hypothesis: '{hyp}'")
        print(f"Result: {result}")
        print()


if __name__ == '__main__':
    main()
