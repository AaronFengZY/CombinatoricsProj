import sys
import os
import json
import pandas as pd
import matplotlib
# Use Agg backend for headless environments (no GUI)
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def main():
    # -------------------------------------------------------------------------
    # 1. Parse command line argument for naming
    #    Example: "python compare.py TheBest_MajorityVoting"
    # -------------------------------------------------------------------------
    if len(sys.argv) < 2:
        print("Usage: python compare.py <Method1_Method2>")
        print("Example: python compare.py TheBest_MajorityVoting")
        sys.exit(1)
    
    param = sys.argv[1]
    if "_" not in param:
        print("ERROR: Parameter must contain an underscore, e.g. 'TheBest_MajorityVoting'.")
        sys.exit(1)
    
    # Split into two names
    model1, model2 = param.split("_", 1)  # in case there is more than one underscore

    # Construct the final output file name and title
    plot_title = f"{model1} compared to {model2}"
    output_filename = f"improvement_{model1}ComparedTo{model2}.png"
    output_path = os.path.join("./VisualizeResult", output_filename)

    # -------------------------------------------------------------------------
    # 2. Define paths for JSON data (update if your paths differ)
    # -------------------------------------------------------------------------
    thebest_path = f"./results/result_{model1}/data.json"
    voting_path  = f"./results/result_{model2}/data.json"

    # -------------------------------------------------------------------------
    # 3. Load JSON data
    # -------------------------------------------------------------------------
    with open(thebest_path, "r") as f:
        thebest_data = json.load(f)
    with open(voting_path, "r") as f:
        voting_data = json.load(f)

    # -------------------------------------------------------------------------
    # 4. Convert to pandas DataFrames and merge
    # -------------------------------------------------------------------------
    df_thebest = pd.DataFrame(thebest_data)
    df_voting  = pd.DataFrame(voting_data)

    df_merged = pd.merge(
        df_thebest,
        df_voting,
        on="assignment",
        suffixes=("_thebest", "_voting")
    )

    # -------------------------------------------------------------------------
    # 5. Calculate improvements
    #    - ACC: bigger is better => ((ACC_thebest - ACC_voting)/ACC_voting)*100
    #    - AAE: smaller is better => ((AAE_voting - AAE_thebest)/AAE_voting)*100
    # -------------------------------------------------------------------------
    df_merged["ACC_improvement_%"] = (
        (df_merged["ACC_thebest"] - df_merged["ACC_voting"])
        / df_merged["ACC_voting"]
    ) * 100

    df_merged["AAE_improvement_%"] = (
        (df_merged["AAE_voting"] - df_merged["AAE_thebest"])
        / df_merged["AAE_voting"]
    ) * 100

    # -------------------------------------------------------------------------
    # 6. Extract columns & compute mean improvements
    # -------------------------------------------------------------------------
    df_display = df_merged[[
        "assignment", 
        "ACC_improvement_%", 
        "AAE_improvement_%"
    ]]

    mean_acc_improvement = df_display["ACC_improvement_%"].mean()
    mean_aae_improvement = df_display["AAE_improvement_%"].mean()

    # Create a one-row DataFrame for the mean
    mean_row = pd.DataFrame({
        "assignment":        ["Mean"],
        "ACC_improvement_%": [mean_acc_improvement],
        "AAE_improvement_%": [mean_aae_improvement]
    })

    # Append the mean row at the bottom
    df_display = pd.concat([df_display, mean_row], ignore_index=True)

    # -------------------------------------------------------------------------
    # 7. Plot the improvements using a grouped bar chart
    # -------------------------------------------------------------------------
    assignments = df_display["assignment"].tolist()
    acc_values  = df_display["ACC_improvement_%"].tolist()
    aae_values  = df_display["AAE_improvement_%"].tolist()

    x = range(len(assignments))
    width = 0.4

    fig, ax = plt.subplots(figsize=(10, 6))

    # Bar for ACC improvements
    acc_bars = ax.bar(
        [i - width/2 for i in x],
        acc_values,
        width=width,
        label="ACC Improvement (%)",
        color="skyblue"
    )

    # Bar for AAE improvements
    aae_bars = ax.bar(
        [i + width/2 for i in x],
        aae_values,
        width=width,
        label="AAE Improvement (%)",
        color="salmon"
    )

    # Add numeric labels on top of each bar
    for i, bar in enumerate(acc_bars):
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width()/2,
            height,
            f"{acc_values[i]:.2f}%",
            ha="center",
            va="bottom",
            fontsize=8
        )

    for i, bar in enumerate(aae_bars):
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width()/2,
            height,
            f"{aae_values[i]:.2f}%",
            ha="center",
            va="bottom",
            fontsize=8
        )

    # Customize the plot
    ax.set_xticks(list(x))
    ax.set_xticklabels(assignments, rotation=45, ha="right")
    ax.set_ylabel("Improvement (%)")
    ax.set_title(plot_title)
    ax.legend()

    plt.tight_layout()

    # -------------------------------------------------------------------------
    # 8. Save to file
    # -------------------------------------------------------------------------
    os.makedirs("./VisualizeResult", exist_ok=True)
    plt.savefig(output_path, dpi=300)
    print(f"Plot saved to: {output_path}")

if __name__ == "__main__":
    main()
