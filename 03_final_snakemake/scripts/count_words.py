import json
import re
import sys
from collections import Counter
from pathlib import Path


def count_words(text: str) -> Counter:
    """Count word frequencies in text.

    Args:
        text: Input text to analyze.

    Returns:
        Counter: Dictionary-like object containing word frequencies.
    """
    words = re.findall(r"\w+", text.lower())
    return Counter(words)


def main() -> None:
    """Main function to count words in text file.

    Reads text file and saves word frequencies as JSON.

    Args:
        None. Uses sys.argv for input/output paths.

    Returns:
        None
    """
    # Get input and output paths from command line
    input_file = Path(sys.argv[1])
    output_file = Path(sys.argv[2])

    # Read input text
    with open(input_file) as f:
        text = f.read()

    # Count words
    counts = count_words(text)

    # Save counts as JSON
    with open(output_file, "w") as f:
        json.dump(counts, f)


if __name__ == "__main__":
    main()
