# Starting Snakemake

The workshop slides are available here:  [Supercharge Your Analyses with Snakemake](https://docs.google.com/presentation/d/11zLDHJCo-uzm7rmrxpHZJNgTg9Zss_rsuWbO1lkb_EI/edit?usp=sharing)

This repository provides a simple multi-folder tutorial:
1. **01_jupyter** – Jupyter-based example that fetches Wikipedia data and plots a histogram.
2. **02_simple_snakemake** – Minimal Snakefile demonstrating a single rule.
3. **03_wildcards** – More complex pipeline that processes multiple links and combines results.

## Installation
To install snakemake and the dependencies for jupyter and matplotlib:
```bash
hostname
# della8.princeton.edu
module load anaconda3/2024.6
conda create -n snake -y
conda activate snake
conda config --env --add channels bioconda
conda config --env --add channels conda-forge
conda install snakemake jupyterlab matplotlib -y
snakemake --version
# 8.28.0
```

We will use the snake environment for the rest of the material.
