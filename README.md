#  MutaDock

> **An Interpretable Python Framework for Mechanistic Analysis of Drug Resistance Mutations in *Mycobacterium tuberculosis***

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Status](https://img.shields.io/badge/Status-Research%20Prototype-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Overview

MutaDock is a modular computational bioinformatics framework designed for the mechanistic interpretation of drugresistance-associated mutations in *Mycobacterium tuberculosis*.

Unlike conventional black box prediction systems, MutaDock follows an **interpretable, knowledge guided architecture**, integrating multiple biological evidence layers into a unified resistance assessment.

The framework combines:

- Mutation Classification
- Amino Acid Property Analysis
- Grantham Scoring
- Structural Context Analysis
- Protein Stability Validation
- Unified Resistance Risk Scoring
- Publication-quality Visualizations

Every prediction is accompanied by a biologically interpretable explanation rather than a standalone numerical score.

---

# Motivation

Understanding how genetic mutations influence antimicrobial resistance remains one of the major challenges in computational biology.

While numerous computational tools estimate mutation effects, many function as black box predictors that provide limited biological interpretability.

MutaDock was developed to bridge this gap by combining classical bioinformatics, structural biology, and evidence-based reasoning into a transparent computational workflow.

Existing catalogue based resistance annotation tools are primarily designed to recognize previously reported resistance-associated mutations. As a result, novel amino acid substitutions frequently lack detailed mechanistic interpretation when prior clinical or experimental evidence is unavailable.

MutaDock addresses this limitation through a mutation agnostic evidence integration framework, capable of accepting any amino acid substitution as input and generating an interpretable Unified Resistance Risk Score by integrating physicochemical, biochemical, structural, and stability based evidence. While the current version provides detailed structural interpretation only for residues supported by curated structural annotations, its overall architecture remains applicable to both known and previously uncharacterized mutations, providing a scalable foundation for future automated structural feature extraction and AI-assisted evidence integration.

---

# Key Features

✔ Modular Python architecture

✔ Knowledge-guided analysis pipeline

✔ Physicochemical amino acid interpretation

✔ Grantham biochemical substitution scoring

✔ Structural context assessment

✔ Protein stability integration (DynaMut2)

✔ Unified evidence-aware resistance scoring

✔ Publication-quality visualizations

✔ Easily extensible architecture

---

# Workflow

```
Mutation Input
       │
       ▼
Mutation Classification
       │
       ▼
Amino Acid Property Analysis
       │
       ▼
Grantham Scoring
       │
       ▼
Structural Context Analysis
       │
       ▼
Protein Stability Validation
       │
       ▼
Unified Resistance Risk Scoring
       │
       ▼
Biological Interpretation
       │
       ▼
Visualization Engine
```

---

# Project Structure

```text
mutadock/
│
├── core/
│   ├── mutation_classifier.py
│   ├── property_analyzer.py
│   ├── grantham_scorer.py
│   ├── structural_context_analyzer.py
│   ├── resistance_risk_scorer.py
│   └── visualization_engine.py
│
├── data/
│   ├── amino_acid_properties.csv
│   ├── dynamut2_results.csv
│   ├── functional_regions.csv
│   ├── grantham_full.csv
│   ├── mutations.csv
│   ├── pocket_residues.csv
│   ├── secondary_structure.csv
│   └── structures/
│       └── 5JZX.pdb
│
├── docs/
│   ├── architecture.md
│   ├── methodology.md
│   └── elite_notes.md
│
├── future/
│   └── README_roadmap.md
│
├── results/
│   ├── mutadock_output.csv
│   ├── summary_statistics.csv
│   └── plots/
│       ├── figure01_unified_risk_scores.png
│       ├── figure02_grantham_vs_risk.png
│       ├── figure03_evidence_distribution.png
│       ├── figure04_gene_distribution.png
│       ├── figure05_murb_structural_summary.png
│       ├── figure06_who_evidence_vs_verdict.png
│       ├── figure07_amino_acid_properties.png
│       └── figure08_workflow_diagram.png
│
├── scripts/
│   └── extract_secondary_structure.py
│
├── tests/
│
├── .gitignore
├── README.md
├── requirements.txt
└── run_pipeline.py
```

---

# Core Modules

| Module | Purpose |
|---------|----------|
| Mutation Classification | Identifies mutation type |
| Property Analyzer | Evaluates amino acid physicochemical changes |
| Grantham Scorer | Calculates biochemical substitution severity |
| Structural Context Analyzer | Determines functional and structural relevance |
| Resistance Risk Scorer | Integrates biological evidence into a unified risk assessment |
| Visualization Engine | Produces publication-quality figures |

---

# Data Sources

The framework integrates curated biological datasets including:

- Amino Acid Physicochemical Properties
- Grantham Distance Matrix
- Functional Region Annotations
- Structural Pocket Residues
- Secondary Structure Information
- DynaMut2 Stability Predictions

---

# Generated Outputs

MutaDock automatically generates:

- Mutation interpretation reports
- Unified resistance scores
- Biological explanations
- Summary statistics
- CSV result tables
- Publication-quality PNG figures
- Publication-quality PDF figures

---

# Visualization Gallery

Current visualizations include:

- Unified Resistance Risk Scores
- Grantham Score vs Risk
- Evidence Distribution
- Gene Distribution
- MurB Structural Summary
- Evidence vs Final Verdict
- Amino Acid Property Distribution
- Computational Workflow

---

# Design Philosophy

The framework was designed around four principles:

- **Interpretability** – Every prediction is biologically explainable.
- **Modularity** – Independent computational modules.
- **Extensibility** – Future computational methods can be incorporated easily.
- **Reproducibility** – Deterministic analyses from structured datasets.

---

# Future Directions

The current version provides a strong interpretable foundation while remaining fully extensible.

Potential future developments include:

- AlphaFold derived structural descriptors
- Protein Language Model features
- Explainable Machine Learning
- Multi-gene expansion
- Automated structural feature extraction
- Large-scale mutation datasets
- Web server implementation

---

# Installation

Clone the repository

```bash
git clone https://github.com/hrsh-seq/mutadock.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the pipeline

```bash
python run_pipeline.py
```

Generate visualizations

```bash
python core/visualization_engine.py
```

---

# Documentation

Additional documentation is available in:

```
docs/
```

including:

- Architecture
- Methodology
- ELITE Project Notes

---

# Current Status

Current Release

**MutaDock v1.0**

Status:

Research Prototype

The framework currently focuses on curated mutations from *Mycobacterium tuberculosis* while maintaining an architecture designed for future expansion.

---

# Citation

If you use MutaDock in academic work, please cite the associated publication (coming soon).

---

# License

This project is released under the MIT License.

---

# Acknowledgements

Developed as part of the **ELITE Summer Internship Programme** under the supervision of **Prof. Pankaj Khanna**, Department of Chemistry, Acharya Narendra Dev College, University of Delhi.

---

# Contact

Harshit Belwal


Gmail : belwalharshit920@gmail.com
GitHub:https://github.com/hrsh-seq
Linkedin : https://www.linkedin.com/in/harshit-belwal/