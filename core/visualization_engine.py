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
# FIGURE 04
# GENE DISTRIBUTION
# ============================================================

def plot_gene_distribution(df):
    """
    Generate Figure 04.

    Distribution of curated mutations across genes.
    """

    gene_counts = (
        df["Gene"]
        .value_counts()
    )

    genes = gene_counts.index

    counts = gene_counts.values


    # --------------------------------------------------
    # Colors
    # --------------------------------------------------

    colors = [
        GENE_COLORS[g]
        for g in genes
    ]


    # --------------------------------------------------
    # Create Figure
    # --------------------------------------------------

    plt.figure(figsize=(7,6))

    bars = plt.bar(
        genes,
        counts,
        width=0.65,
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
        "Distribution of Curated Mutations Across Genes",
        pad=20
    )

    plt.xlabel("Gene")

    plt.ylabel("Number of Mutations")


    # --------------------------------------------------
    # Axis
    # --------------------------------------------------

    plt.ylim(0,6)

    plt.grid(axis="y")


    # --------------------------------------------------
    # Save Figure
    # --------------------------------------------------

    save_figure(
        "figure04_gene_distribution.png"
    )

    plt.close()



# ============================================================
# FIGURE 05
# MurB STRUCTURAL IMPACT SUMMARY
# ============================================================

def plot_murb_structural_summary(df):
    """
    Generate Figure 05.

    Structural impact summary for MurB showcase mutations.
    """

    murb_df = df[df["Gene"] == "MurB"]

    mutations = murb_df["Mutation"]

    impacts = murb_df["Structural Impact"]


    # --------------------------------------------------
    # Impact Mapping
    # --------------------------------------------------

    impact_scores = {
        "LOW": 1,
        "MODERATE": 2,
        "HIGH": 3
    }

    impact_colors = {
        "LOW": "#2ca02c",
        "MODERATE": "#ffbf00",
        "HIGH": "#d62728"
    }

    values = [
        impact_scores[i]
        for i in impacts
    ]

    colors = [
        impact_colors[i]
        for i in impacts
    ]


    # --------------------------------------------------
    # Create Figure
    # --------------------------------------------------

    plt.figure(figsize=(8,6))

    bars = plt.bar(
        mutations,
        values,
        width=0.6,
        color=colors,
        edgecolor="black",
        linewidth=0.8
    )


    # --------------------------------------------------
    # Labels
    # --------------------------------------------------

    for bar, label in zip(bars, impacts):

        height = bar.get_height()

        plt.text(
            bar.get_x() + bar.get_width()/2,
            height + 0.08,
            label,
            ha="center",
            fontsize=10,
            fontweight="bold"
        )


    # --------------------------------------------------
    # Titles
    # --------------------------------------------------

    plt.title(
        "Structural Impact Assessment of MurB Mutations",
        pad=20
    )

    plt.xlabel("MurB Mutation")

    plt.ylabel("Structural Impact")


    # --------------------------------------------------
    # Axis
    # --------------------------------------------------

    plt.yticks(
        [1,2,3],
        ["LOW","MODERATE","HIGH"]
    )

    plt.ylim(0,3.6)

    plt.grid(axis="y")


    # --------------------------------------------------
    # Save
    # --------------------------------------------------

    save_figure(
        "figure05_murb_structural_summary.png"
    )

    plt.close()




# ============================================================
# FIGURE 06
# EVIDENCE CATEGORY VS FINAL VERDICT
# ============================================================

def plot_who_evidence_vs_verdict(df):
    """
    Generate Figure 06.

    Final verdicts assigned across evidence categories.
    """

    verdict_counts = (
        df.groupby(["Evidence Category", "Final Verdict"])
        .size()
        .unstack(fill_value=0)
    )


    # --------------------------------------------------
    # Create Figure
    # --------------------------------------------------

    plt.figure(figsize=(10,6))

    verdict_counts.plot(
        kind="bar",
        stacked=True,
        ax=plt.gca(),
        edgecolor="black"
    )


    # --------------------------------------------------
    # Titles & Labels
    # --------------------------------------------------

    plt.title(
        "Evidence Category vs Final Resistance Verdict",
        pad=20
    )

    plt.xlabel("Evidence Category")

    plt.ylabel("Number of Mutations")

    plt.xticks(rotation=15)

    plt.grid(axis="y")


    # --------------------------------------------------
    # Legend
    # --------------------------------------------------

    plt.legend(
        title="Final Verdict",
        bbox_to_anchor=(1.02,1),
        loc="upper left"
    )


    # --------------------------------------------------
    # Save Figure
    # --------------------------------------------------

    save_figure(
        "figure06_who_evidence_vs_verdict.png"
    )

    plt.close()


# ============================================================
# SCIENTIFIC PURPOSE
#
# Figure 06 illustrates how different categories of biological evidence are translated into final resistance verdicts by the MutaDock scoring framework.
# Key Insight:
# Rather than assigning a single outcome to all mutations, MutaDock integrates clinical evidence, structural context, protein stability, and functional importance to generate
# biologically meaningful and interpretable resistance classifications.
# ============================================================




# ============================================================
# FIGURE 07
# AMINO ACID PROPERTY CHANGES
# ============================================================

def plot_amino_acid_properties(df):
    """
    Generate Figure 07.

    Distribution of polarity changes among curated mutations.
    """

    property_counts = (
        df["Polarity Change"]
        .value_counts()
    )

    labels = property_counts.index

    counts = property_counts.values


    # --------------------------------------------------
    # Colors
    # --------------------------------------------------

    property_colors = {

        "Polar -> Polar": "#1f77b4",
        "Polar -> Nonpolar": "#ff7f0e",
        "Nonpolar -> Nonpolar": "#2ca02c",
        "Nonpolar -> Polar": "#d62728"

    }

    colors = [
        property_colors[label]
        for label in labels
    ]


    # --------------------------------------------------
    # Create Figure
    # --------------------------------------------------

    plt.figure(figsize=(9,6))

    bars = plt.bar(
        labels,
        counts,
        width=0.7,
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
        "Distribution of Amino Acid Polarity Changes",
        pad=20
    )

    plt.xlabel("Polarity Change")

    plt.ylabel("Number of Mutations")


    # --------------------------------------------------
    # Axis
    # --------------------------------------------------

    plt.xticks(rotation=15)

    plt.grid(axis="y")


    # --------------------------------------------------
    # Save Figure
    # --------------------------------------------------

    save_figure(
        "figure07_amino_acid_properties.png"
    )

    plt.close()


# ============================================================
# SCIENTIFIC PURPOSE
#
# Figure 07 summarizes the polarity changes associated with
# curated amino acid substitutions analyzed by MutaDock.
#
# Key Insight:
# Amino acid substitutions may preserve or alter residue
# polarity, potentially influencing protein folding,
# molecular interactions, and resistance-associated
# structural changes.
# ============================================================



# ============================================================
# FIGURE 08
# MUTADOCK WORKFLOW
# ============================================================

def plot_workflow_diagram():
    """
    Generate Figure 08.

    MutaDock computational workflow.
    """

    plt.figure(figsize=(15,3))

    plt.axis("off")


    workflow = [

        ("Mutation\nInput", 0.05, "#D6EAF8"),

        ("Mutation\nClassification", 0.22, "#AED6F1"),

        ("Property\nAnalysis", 0.39, "#A9DFBF"),

        ("Grantham\nScoring", 0.56, "#F9E79F"),

        ("Structural\nAnalysis", 0.73, "#F5CBA7"),

        ("Unified\nRisk Score", 0.90, "#F1948A")

    ]


    for label, x, color in workflow:

        plt.text(
            x,
            0.5,
            label,
            ha="center",
            va="center",
            fontsize=11,
            fontweight="bold",
            bbox=dict(
                boxstyle="round,pad=0.5",
                facecolor=color,
                edgecolor="black"
            )
        )


    for i in range(len(workflow)-1):

        plt.annotate(
            "",
            xy=(workflow[i+1][1]-0.05,0.5),
            xytext=(workflow[i][1]+0.05,0.5),
            arrowprops=dict(
                arrowstyle="->",
                lw=2
            )
        )


    plt.title(
        "MutaDock Computational Workflow",
        fontsize=18,
        fontweight="bold",
        pad=20
    )


    save_figure(
        "figure08_workflow_diagram.png"
    )

    plt.close()




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

    print("[4/8] Gene Distribution...")
    plot_gene_distribution(df)

    print("[5/8] MurB Structural Summary...")
    plot_murb_structural_summary(df)


    print("[6/8] Evidence vs Verdict...")
    plot_who_evidence_vs_verdict(df)

    print("[7/8] Amino Acid Property Changes...")
    plot_amino_acid_properties(df)

    print("[8/8] Workflow Diagram...")
    plot_workflow_diagram()


    print("\n✓ Visualization completed successfully.")


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    generate_all_figures()

