#!/usr/bin/env python3

import sys
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def plot_side_by_side_save(
    title,
    image_path_left,
    image_path_right,
    save_path
):
    """
    Plots two images side by side (1×2 format) with a figure-wide title,
    and saves the figure to disk (no GUI display).

    :param title:            The figure-wide title (string).
    :param image_path_left:  Path to the left image.
    :param image_path_right: Path to the right image.
    :param save_path:        Full path (including filename) for saving the output figure.
    """

    # Read images
    img_left = mpimg.imread(image_path_left)
    img_right = mpimg.imread(image_path_right)

    # Create subplots (1 row × 2 columns)
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))

    # Display the left image
    axes[0].imshow(img_left)
    axes[0].axis('off')          # Hide axis lines/ticks
    axes[0].set_title("AAE")     # Subplot title

    # Display the right image
    axes[1].imshow(img_right)
    axes[1].axis('off')
    axes[1].set_title("ACC")

    # Set the figure-wide title
    fig.suptitle(title, fontsize=14)

    # Adjust layout
    plt.tight_layout()

    # Save the figure
    fig.savefig(save_path, dpi=300, bbox_inches='tight')

    # Close the figure (no GUI)
    plt.close(fig)

def main():
    # Check if user provided a title argument
    if len(sys.argv) < 2:
        print("Usage: python combine1*2.py <TITLE>")
        sys.exit(1)

    # Grab the first argument as the title
    title_arg = sys.argv[1]

    # Paths are constructed to use the same directory: ./VisualizeResult
    script_dir = os.path.dirname(os.path.abspath(__file__))
    visualize_result_dir = os.path.join(script_dir, "..", "VisualizeResult")
    os.makedirs(visualize_result_dir, exist_ok=True)

    # Image paths based on the passed title:
    # e.g. "./VisualizeResult/MajorityVoting_AAE.png"
    image_path_left = os.path.join(visualize_result_dir, f"{title_arg}_AAE.png")
    image_path_right = os.path.join(visualize_result_dir, f"{title_arg}_ACC.png")

    # The final saved filename, e.g. "MajorityVoting_1*2.png"
    final_filename = f"{title_arg}_1*2.png"
    save_full_path = os.path.join(visualize_result_dir, final_filename)

    # Run the plotting/saving function
    plot_side_by_side_save(
        title=title_arg,
        image_path_left=image_path_left,
        image_path_right=image_path_right,
        save_path=save_full_path
    )

    print(f"Saved combined figure as: {save_full_path}")

if __name__ == "__main__":
    main()
