# Simple Snakemake Word Frequency Analysis

> NOTE: You must have Snakemake installed to run this workflow as well as beautifulsoup4 and matplotlib.

A Snakemake workflow that:
1. Downloads text from specified URLs
2. Creates word frequency visualization plots

## Usage

```bash
snakemake --cores 1
```

## Structure
- `Snakefile`: Workflow definition with URLs
- `scripts/word_frequencies.py`: Script that handles all processing