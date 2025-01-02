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
      python plot_acc.py <data_path> <figure_name>
    EXAMPLE:
      python plot_acc.py data.json MajorityVoting
      -> Saves figure as VisualizeResult/MajorityVoting_ACC.png
    """
    if len(sys.argv) < 3:
        print("ERROR: Missing required arguments.")
        print("USAGE: python plot_acc.py <data_path> <figure_name>")
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
    print("Data Table for ACC Plot (Percent):")
    print(df.to_string(index=False))

    # 5) Convert ACC to percentage (e.g. 0.8 -> 80%)
    df["ACC_percent"] = df["ACC"] * 100

    # 6) Plot ACC (as %) vs. assignment
    plt.figure(figsize=(7, 5))
    bars = plt.bar(df["assignment"], df["ACC_percent"], color="cornflowerblue")
    plt.xlabel("Assignment")
    plt.ylabel("ACC (%)")
    plt.title("ACC vs. Assignment (Percent)")

    # 7) Set y-axis start at 50% (i.e., 50) and go up to 100% or beyond
    plt.ylim([50, 100])

    # 8) Add labels on top of each bar
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.5,         # Slight offset
            f"{height:.1f}%",    # 1 decimal place + '%'
            ha="center",
            va="bottom"
        )

    # 9) Save the figure in the 'VisualizeResult' folder with custom naming
    output_path = os.path.join("VisualizeResult", f"{figure_name}_ACC.png")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

if __name__ == "__main__":
    main()
