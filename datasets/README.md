# Datasets Directory

This directory contains test data for evaluations.

## Structure

```
datasets/
├── images/          # Test images for vision evaluations
├── audio/           # Test audio for audio evaluations
├── contexts/        # Long documents for context window tests
├── queries/         # Query datasets
└── ground_truth/    # Expected outputs for validation
```

## Adding Test Data

1. Place files in appropriate subdirectory
2. Update corresponding prompt.yml with file paths
3. Document any licensing or attribution requirements

## Data Formats

- **Images**: JPG, PNG, WebP
- **Audio**: MP3, WAV, M4A
- **Text**: TXT, MD, JSON, JSONL
- **Structured**: JSON, JSONL, CSV
