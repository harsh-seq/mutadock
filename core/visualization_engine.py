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
# FIGURE 02
# GRANTHAM SCORE VS UNIFIED RISK SCORE
# ============================================================

def plot_grantham_vs_risk(df):
    """
    Generate Figure 02.

    Relationship between Grantham Score and Unified Risk Score.
    """

    grantham = df["Grantham Score"]

    risk = df["Unified Risk Score"]

    genes = df["Gene"]

    mutations = df["Mutation"]

    colors = [GENE_COLORS[g] for g in genes]


    # --------------------------------------------------

    plt.figure(figsize=(10, 6))

    plt.scatter(
        grantham,
        risk,
        c=colors,
        s=90,
        edgecolors="black",
        linewidths=0.8,
        alpha=0.9
    )


    # --------------------------------------------------
    # Annotate each mutation
    # --------------------------------------------------

    for x, y, label in zip(grantham, risk, mutations):

        plt.text(
            x + 2,
            y + 0.08,
            label,
            fontsize=8,
            bbox=dict(
                facecolor="white",
                edgecolor="none",
                alpha=0.75,
                pad=1
            )
        )


    # --------------------------------------------------

    plt.title(
        "Grantham Score vs Unified Resistance Risk",
        pad=25
    )

    plt.xlabel("Grantham Score")

    plt.ylabel("Unified Risk Score")

    plt.xlim(0, 170)

    plt.ylim(0, 10.5)

    plt.grid(axis="both")


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


    save_figure(
        "figure02_grantham_vs_risk.png"
    )

    plt.close()


## Although Grantham score quantifies the biochemical severity of an amino acid substitution, mutations with similar Grantham scores can exhibit markedly
## different resistance risks due to differences in functional importance, clinical evidence, structural context, and protein stability. MutaDock
##integrates these complementary sources of evidence into a unified resistance risk score.


# ============================================================
# FIGURE 03
# EVIDENCE CATEGORY DISTRIBUTION
# ============================================================

def plot_evidence_distribution(df):
    """
    Generate Figure 03.

    Distribution of curated mutations across evidence categories.
    """

    evidence_counts = (
        df["Evidence Category"]
        .value_counts()
    )

    categories = evidence_counts.index

    counts = evidence_counts.values


    # --------------------------------------------------
    # Color Palette
    # --------------------------------------------------

    evidence_colors = {

        "WHO Confirmed": "#2ca02c",
        "WHO Discordant": "#ff7f0e",
        "Structural Showcase": "#1f77b4",
        "Negative Control": "#d62728"

    }

    colors = [
        evidence_colors[c]
        for c in categories
    ]


    # --------------------------------------------------
    # Create Figure
    # --------------------------------------------------

    plt.figure(figsize=(8, 6))

    bars = plt.bar(
        categories,
        counts,
        width=0.80,
        color=colors,
        edgecolor="black",
        linewidth=0.8
    )


    # --------------------------------------------------
    # Value Labels
    # --------------------------------------------------

    for bar in bars:

        height = bar.get_height()

        plt.text(
            bar.get_x() + bar.get_width()/2,
            height + 0.08,
            str(height),
            ha="center",
            va="bottom",
            fontsize=11,
            fontweight="bold"
        )


    # --------------------------------------------------
    # Titles & Labels
    # --------------------------------------------------

    plt.title(
        "Distribution of Curated Mutations by Evidence Category",
        pad=20
    )

    plt.xlabel("Evidence Category")

    plt.ylabel("Number of Mutations")


    # --------------------------------------------------
    # Axis
    # --------------------------------------------------

    plt.ylim(0, 9)

    plt.xticks(rotation=10)

    plt.grid(axis="y")


    # --------------------------------------------------
    # Save Figure
    # --------------------------------------------------

    save_figure(
        "figure03_evidence_distribution.png"
    )

    plt.close()


   
# SCIENTIFIC PURPOSE
#
# Figure 03 summarizes the evidence sources represented in the curated mutation panel. The dataset combines clinically validated WHO mutations, discordant variants,
# structural showcase mutations, and a negative control, demonstrating that MutaDock integrates multiple evidence types within a unified framework.
# ============================================================


# ============================================================
# GENERATE ALL FIGURES
# ============================================================

def generate_all_figures():

    df = load_results()

    if df is None:
        return

    print("[1/8] Unified Risk Scores...")
    plot_unified_risk_scores(df)

    print("[2/8] Grantham vs Risk...")
    plot_grantham_vs_risk(df)


    print("[3/8] Evidence Distribution...")
    plot_evidence_distribution(df)

    print("\n✓ Visualization completed successfully.")


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    generate_all_figures()

