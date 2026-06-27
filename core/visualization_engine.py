"""
MutaDock Visualization Engine

Generates publication quality figures for the MutaDock pipeline.

Author: Harshit Belwal
Version: 1.0
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# GLOBAL VISUALIZATION THEME
# ============================================================

plt.style.use("default")

# Figure quality
plt.rcParams["figure.dpi"] = 300
plt.rcParams["savefig.dpi"] = 300

# Figure size
plt.rcParams["figure.figsize"] = (12, 6)

# Fonts
plt.rcParams["font.family"] = "DejaVu Sans"

plt.rcParams["axes.titlesize"] = 16
plt.rcParams["axes.titleweight"] = "bold"

plt.rcParams["axes.labelsize"] = 13
plt.rcParams["axes.labelweight"] = "bold"

plt.rcParams["xtick.labelsize"] = 10
plt.rcParams["ytick.labelsize"] = 10

plt.rcParams["legend.fontsize"] = 10

# Grid appearance
plt.rcParams["axes.grid"] = True
plt.rcParams["grid.linestyle"] = "--"
plt.rcParams["grid.alpha"] = 0.35


# ============================================================
# MUTADOCK COLOR PALETTE
# ============================================================

GENE_COLORS = {
    "rpoB": "#1f77b4",   # Blue
    "katG": "#2ca02c",   # Green
    "MurB": "#ff7f0e"    # Orange
}


# ============================================================
# FILE PATHS
# ============================================================

BASE_RESULTS_DIR = "results"

RESULTS_FILE = os.path.join(BASE_RESULTS_DIR, "mutadock_output.csv")

OUTPUT_DIR = os.path.join(BASE_RESULTS_DIR, "plots")


# ============================================================
# DATA LOADING
# ============================================================

def load_results():
    """
    Load the final MutaDock output CSV.

    Returns
    -------
    pandas.DataFrame
        DataFrame containing mutation analysis results.
    """

    try:

        df = pd.read_csv(RESULTS_FILE)

        print(f"✓ Loaded {len(df)} mutations successfully.")

        return df

    except FileNotFoundError:

        print(f"\nError: {RESULTS_FILE} not found.")

        return None
    



# ============================================================
# SAVE FIGURE
# ============================================================

def save_figure(filename):
    """
    Save the current matplotlib figure.
    """

    filepath = os.path.join(OUTPUT_DIR, filename)

    plt.tight_layout()

    plt.savefig(
        filepath,
        dpi=300,
        bbox_inches="tight"
    )

    print(f"✓ Figure saved: {filepath}")