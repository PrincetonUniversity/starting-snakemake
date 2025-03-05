# Word Frequency Analysis Workflow

This Snakemake workflow analyzes word frequencies across multiple web pages.

The workshop slides are available here:  [Supercharge Your Analyses with Snakemake](https://docs.google.com/presentation/d/11zLDHJCo-uzm7rmrxpHZJNgTg9Zss_rsuWbO1lkb_EI/edit?usp=sharing)

## Overview

The workflow:
1. Downloads HTML from specified URLs
2. Extracts and counts words using bash commands
3. Creates frequency plots for each URL
4. Combines results into a comparative visualization

## Usage

1. Add URLs to analyze in the Snakefile
2. Run the workflow:
```bash
snakemake --cores 1
```

## Output

Results are stored in the `results/` directory:
- `text/`: Raw extracted text from each URL
- `counts/`: Word frequency counts in JSON format
- `plots/`: Individual frequency plots for each URL
- `combined_frequencies.png`: Comparative plot across all URLs
