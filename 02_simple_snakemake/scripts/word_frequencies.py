import sys
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from collections import Counter
import re
from typing import Counter as CounterType

def get_page_text(url: str) -> str:
    """Fetch webpage and extract text content.
    
    Args:
        url: URL of webpage to fetch.
        
    Returns:
        str: Plain text content of webpage.
        
    Raises:
        requests.RequestException: If there's an error fetching the page.
    """
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()

def count_words(text: str) -> CounterType:
    """Count word frequencies in text.
    
    Args:
        text: Input text to analyze.
        
    Returns:
        Counter: Dictionary-like object containing word frequencies.
    """
    words = re.findall(r'\w+', text.lower())
    return Counter(words)

def plot_frequencies(counts: CounterType, url: str, output_file: str) -> None:
    """Create bar plot of word frequencies.
    
    Args:
        counts: Dictionary of word frequencies.
        url: URL of the analyzed webpage.
        output_file: Path to save the plot.
        
    Returns:
        None
    """
    labels, values = zip(*counts.most_common(10))
    plt.bar(labels, values)
    plt.title(f'Word Frequencies for {url}')
    plt.savefig(output_file)
    plt.close()

def main() -> None:
    """Main function to analyze webpage word frequencies.
    
    Fetches webpage, counts words, and creates frequency plot.
    
    Args:
        None. Uses sys.argv for URL and output path.
        
    Returns:
        None
        
    Raises:
        Exception: If there's an error processing the webpage.
    """
    # Get URL and output file from command line
    url = sys.argv[1]
    output_file = sys.argv[2]
    
    try:
        # Get and process text
        text = get_page_text(url)
        counts = count_words(text)
        
        # Create plot
        plot_frequencies(counts, url, output_file)
            
    except Exception as e:
        print(f"Error processing {url}: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
