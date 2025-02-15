import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def main():
    """Combine word frequency counts from multiple files."""
    # Get arguments
    counts_dir = Path(sys.argv[1])
    output_file = sys.argv[2]

    # Load all count files
    counts_data = {}
    for counts_file in counts_dir.glob("*.csv"):
        # Get URL from filename
        url = counts_file.stem.replace("_", "/")

        # Load counts
        df = pd.read_csv(counts_file, header=None, names=["word", "frequency"])
        counts_data[url] = dict(zip(df["word"], df["frequency"]))

    # Convert to DataFrame
    df = pd.DataFrame(counts_data).fillna(0)

    # Get top 20 words across all sites
    totals = df.sum(axis=1)
    top_words = totals.nlargest(20).index
    df_top = df.loc[top_words]

    # Create plot
    plt.figure(figsize=(15, 8))
    df_top.plot(kind="bar")
    plt.title("Top 20 Words Across All Sites")
    plt.xlabel("Word")
    plt.ylabel("Frequency")
    plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.savefig(output_file)


if __name__ == "__main__":
    main()
