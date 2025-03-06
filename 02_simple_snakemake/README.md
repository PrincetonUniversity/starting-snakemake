# Simple Word Frequency Analysis

> NOTE: You must have Snakemake installed to run this workflow as well as pandas and matplotlib.

A Snakemake workflow that:
1. Downloads webpage HTML
2. Extracts words using bash commands
3. Counts the frequency of each word.  You will need to write this rule
4. Creates word frequency plots using matplotlib

## Usage

```bash
# parse and validate the snakefile.  Will complain about any errors
snakemake -nq
# will additionally print the number of jobs each rule will run
snakemake -nq rule
# run the workflow with a single compute process
snakemake --cores 1
```

## Structure
`Snakefile` contains the workflow definition.  In more complex projects, it's
common to place the snakefile in a `workflow` directory.  Other directories
suggested for best practice include scripts, config, and envs.
See [the documentation](https://snakemake.readthedocs.io/en/stable/snakefiles/deployment.html)
for a full listing of the recommended layout.
