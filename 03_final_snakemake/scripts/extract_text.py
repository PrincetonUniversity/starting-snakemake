import sys
from pathlib import Path

from bs4 import BeautifulSoup


def extract_text_from_html(html_content: str) -> str:
    """Extract plain text from HTML content.

    Args:
        html_content: Raw HTML content as string.

    Returns:
        str: Extracted plain text from HTML.
    """
    soup = BeautifulSoup(html_content, "html.parser")

    return soup.get_text()


def main() -> None:
    """Main function to extract text from HTML file.

    Reads HTML file and saves extracted plain text.

    Args:
        None. Uses sys.argv for input/output paths.

    Returns:
        None

    Raises:
        Exception: If there's an error processing the file.
    """
    try:
        input_file = Path(sys.argv[1])
        output_file = Path(sys.argv[2])

        # Read downloaded HTML file
        html_content = input_file.read_text(encoding="utf-8", errors="ignore")
        text = extract_text_from_html(html_content)

        # Write extracted text
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(text, encoding="utf-8")

    except Exception as e:
        print(f"Error processing file: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
