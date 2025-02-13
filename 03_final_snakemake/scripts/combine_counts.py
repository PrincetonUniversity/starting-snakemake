import json
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

N_WORDS = 20  # Hardcoded parameter


def main():
    # Get arguments
    counts_dir = Path(sys.argv[1])
    output_file = Path(sys.argv[2])

    # Load all count files
    counts_data = {}
    for counts_file in counts_dir.glob("*.json"):
        # Get URL from filename
        url = counts_file.stem.replace("_", "/")

        # Load counts
        with open(counts_file) as f:
            counts_data[url] = json.load(f)

    # Convert to DataFrame
    df = pd.DataFrame(counts_data).fillna(0)

    # Get top N words across all sites
    totals = df.sum(axis=1)
    top_words = totals.nlargest(N_WORDS).index
    df_top = df.loc[top_words]

    # Create plot
    plt.figure(figsize=(15, 8))
    df_top.plot(kind="bar")
    plt.title(f"Top {N_WORDS} Words Across All Sites")
    plt.xlabel("Word")
    plt.ylabel("Frequency")
    plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.savefig(output_file)


if __name__ == "__main__":
    main()
