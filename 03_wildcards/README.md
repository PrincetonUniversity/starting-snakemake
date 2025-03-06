# Word Frequency Analysis Workflow

This Snakemake workflow analyzes word frequencies across multiple web pages.

## Overview

The workflow:
1. Downloads HTML from specified URLs
2. Extracts words using bash commands
3. Counts the frequency of each word
4. Creates frequency plots for each URL
5. Combines results into a comparative bar plot

## Usage

1. Add URLs to analyze in the Snakefile
2. You need to update the `count_princeton` rule to utilize wildcards.
3. Run the workflow:
```bash
snakemake --cores 1
```

## Output

Results are stored in the two directories:
- `data/`: Raw and extracted text from each URL
- `results/`: Word frequency counts in csv format, and plots
