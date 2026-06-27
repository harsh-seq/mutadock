"""
MutaDock Visualization Engine

Generates publication quality figures for the MutaDock pipeline.

Author: Harshit Belwal
Version: 1.0
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

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
plt.rcParams["axes.grid"] = False
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

os.makedirs(OUTPUT_DIR, exist_ok=True)

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

# ============================================================
# SAVE FIGURE
# ============================================================

def save_figure(filename):
    """
    Save the current matplotlib figure in both PNG and PDF formats.
    """

    filepath = os.path.join(OUTPUT_DIR, filename)

    pdf_path = filepath.replace(".png", ".pdf")

    plt.tight_layout()

    # High-resolution PNG
    plt.savefig(
        filepath,
        dpi=300,
        bbox_inches="tight"
    )

    # Publication-quality vector PDF
    plt.savefig(
        pdf_path,
        bbox_inches="tight"
    )

    print(f"✓ PNG saved : {filepath}")
    print(f"✓ PDF saved : {pdf_path}")

# ============================================================
# FIGURE 01
# UNIFIED RESISTANCE RISK SCORES
# ============================================================

def plot_unified_risk_scores(df):
    """
    Generate Figure 01.

    Unified Resistance Risk Scores Across Curated Mutations.
    """

    

    mutations = df["Mutation"]
    risk_scores = df["Unified Risk Score"]
    genes = df["Gene"]

    colors = [GENE_COLORS[g] for g in genes]

    # --------------------------------------------------

    plt.figure(figsize=(12,6))

    bars = plt.bar(
        mutations,
        risk_scores,
        color=colors,
        edgecolor="black",
        linewidth=0.8,
        width=0.78
    )

    # --------------------------------------------------

    plt.title(
        "Unified Resistance Risk Scores Across Curated Mutations",
        pad=20
    )

    plt.xlabel("Mutation")

    plt.ylabel("Unified Risk Score")

    plt.ylim(0,10.5)

    plt.xticks(rotation=40)

    # --------------------------------------------------
    # Score Labels
    # --------------------------------------------------

    for bar in bars:

        height = bar.get_height()

        plt.text(
            bar.get_x() + bar.get_width()/2,
            height + 0.12,
            f"{int(height)}",
            ha="center",
            va="bottom",
            fontsize=10,
            fontweight="bold"
        )

    # --------------------------------------------------
    # Legend
    # --------------------------------------------------

    legend_elements = [

        Patch(
            facecolor=GENE_COLORS["rpoB"],
            edgecolor="black",
            label="rpoB"
        ),

        Patch(
            facecolor=GENE_COLORS["katG"],
            edgecolor="black",
            label="katG"
        ),

        Patch(
            facecolor=GENE_COLORS["MurB"],
            edgecolor="black",
            label="MurB"
        )

    ]

    
    plt.legend(
    handles=legend_elements,
    loc="upper left",
    bbox_to_anchor=(1.01, 1)
)

    # --------------------------------------------------

    save_figure(
        "figure01_unified_risk_scores.png"
    )

    plt.close()


# ============================================================
# GENERATE ALL FIGURES
# ============================================================

def generate_all_figures():

    df = load_results()

    if df is None:
        return

    plot_unified_risk_scores(df)

    print("\n✓ Visualization completed successfully.")


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    generate_all_figures()