# Simple Word Frequency Analysis

> NOTE: You must have Snakemake installed to run this workflow as well as pandas and matplotlib.

A Snakemake workflow that:
1. Downloads webpage HTML
2. Extracts and counts words using bash commands
3. Creates word frequency plots using matplotlib

## Usage

```bash
snakemake --cores 1
```

## Structure
- `Snakefile`: Workflow definition
- `scripts/word_frequencies.py`: Python script that handles the plotting