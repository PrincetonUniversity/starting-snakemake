import json
import sys
from pathlib import Path

import matplotlib.pyplot as plt

N_WORDS = 20  # Hardcoded parameter


def plot_frequencies(counts: dict[str, int], url: str) -> None:
    """Create bar plot of most frequent words.

    Args:
        counts: Dictionary of word frequencies.
        url: URL of the webpage being analyzed.
    """
    # Get top N words
    top_words = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:N_WORDS]
    words, freqs = zip(*top_words)

    # Create plot
    plt.figure(figsize=(12, 6))
    plt.bar(words, freqs)
    plt.xticks(rotation=90)
    plt.title(f"Top {N_WORDS} Words in {url}")
    plt.ylabel("Frequency")
    plt.tight_layout()


def main() -> None:
    """Main function to create word frequency plot from counts file.

    Reads JSON counts file and creates bar plot of top N frequent words.
    Uses sys.argv for input/output paths.
    """
    # Get arguments
    counts_file = Path(sys.argv[1])
    plot_file = Path(sys.argv[2])

    # Load counts
    with open(counts_file) as f:
        counts = json.load(f)

    # Extract URL from filename
    url = counts_file.stem.replace("_", "/")
    if not url.startswith("http"):
        url = "https://" + url

    # Create plot
    plot_frequencies(counts, url)
    plt.savefig(plot_file)


if __name__ == "__main__":
    main()
