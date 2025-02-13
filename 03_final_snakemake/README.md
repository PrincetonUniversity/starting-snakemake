# Word Frequency Analysis Workflow

This Snakemake workflow analyzes word frequencies across multiple web pages.


## Overview

The workflow:
1. Downloads and extracts text from specified URLs
2. Counts word frequencies in each text
3. Creates frequency plots for each URL
4. Combines results into a comparative visualization

## Usage

> NOTE: You must have Snakemake installed to run this workflow as well as beautifulsoup4 and matplotlib.


1. Add URLs to analyze in `links.txt`, one per line
2. Adjust parameters in `config.yaml` if needed
3. Run the workflow:
```bash
snakemake --cores 1
```

## Output

Results are stored in the `results/` directory:
- `text/`: Raw extracted text from each URL
- `counts/`: Word frequency counts in JSON format
- `plots/`: Individual frequency plots for each URL
- `combined_frequencies.png`: Comparative plot across all URLs
