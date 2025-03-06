import sys

import matplotlib.pyplot as plt
import pandas as pd

# Get input/output files from command line
input_file = sys.argv[1]
output_file = sys.argv[2]

# Read the CSV data
df = pd.read_csv(input_file, header=None, names=["word", "frequency"])

# Plot top 20 words
plt.figure(figsize=(12, 6))
plt.bar(df["word"][:20], df["frequency"][:20])
plt.xticks(rotation=90)
plt.title("Top 20 Most Frequent Words")
plt.ylabel("Frequency")
plt.xlabel("Words")
plt.tight_layout()
plt.savefig(output_file)
plt.close()
