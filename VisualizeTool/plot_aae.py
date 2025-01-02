#!/usr/bin/env python3
import os
import sys
import json
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for headless environments
import matplotlib.pyplot as plt

def main():
    """
    USAGE:
      python plot_aae.py <data_path> <figure_name>
    EXAMPLE:
      python plot_aae.py data.json MajorityVoting
      -> Saves figure as VisualizeResult/MajorityVoting_AAE.png
    """
    if len(sys.argv) < 3:
        print("ERROR: Missing required arguments.")
        print("USAGE: python plot_aae.py <data_path> <figure_name>")
        sys.exit(1)

    data_path    = sys.argv[1]
    figure_name  = sys.argv[2]

    # 1) Ensure the output folder 'VisualizeResult' exists
    os.makedirs("VisualizeResult", exist_ok=True)

    # 2) Load data from the JSON file
    with open(data_path, "r") as f:
        data = json.load(f)  # data is a list of dicts

    # 3) Create a DataFrame
    df = pd.DataFrame(data)

    # 4) Print the table in the terminal
    print("Data Table for AAE Plot:")
    print(df.to_string(index=False))

    # 5) Plot AAE vs. assignment
    plt.figure(figsize=(7, 5))
    bars = plt.bar(df["assignment"], df["AAE"], color="salmon")
    plt.xlabel("Assignment")
    plt.ylabel("AAE")
    plt.title("AAE vs. Assignment")

    # 6) Add labels on top of each bar (2 decimals)
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.2,
            f"{height:.2f}",
            ha="center",
            va="bottom"
        )

    # 7) Save the figure in the 'VisualizeResult' folder with custom naming
    output_path = os.path.join("VisualizeResult", f"{figure_name}_AAE.png")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

if __name__ == "__main__":
    main()
