# MutaDock Architecture

## Overview

MutaDock is a modular Python based computational bioinformatics framework developed for the mechanistic interpretation of drug resistance associated mutations in *Mycobacterium tuberculosis*. 

The current framework integrates mutation classification, amino acid physicochemical property analysis, biochemical substitution scoring, structural context analysis, protein stability assessment, and an evidence-aware resistance scoring system into a unified, interpretable pipeline.

Unlike conventional black box prediction systems, MutaDock follows a knowledge guided architecture where each module performs a well defined biological task and contributes explainable evidence toward the final resistance interpretation.

Machine Learning part was delibrately avoided in current framework because of small dataset of just 13 snps for builiding a prototype and and can easily work on who confirmed resistances and also 3 structural interpretations of MurB (A structural enzyme)
---

# Design Philosophy

The architecture was designed with four guiding principles:

- **Modularity** – Each biological task is implemented as an independent Python module.

- **Interpretability** – Every prediction is supported by biologically meaningful evidence.

- **Extensibility** – New genes, mutations, datasets, and future computational methods can be integrated without redesigning the framework.

- **Reproducibility** – All analyses are performed from structured CSV datasets using deterministic algorithms.

---

# High-Level Pipeline

```text
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
│   ├── mutations.csv
│   ├── amino_acid_properties.csv
│   ├── grantham_full.csv
│   ├── pocket_residues.csv
│   ├── functional_regions.csv
│   ├── secondary_structure.csv
│   └── dynamut2_results.csv
│
├── results/
│
├── docs/
│
├── scripts/
│
└── run_pipeline.py
```

---

# Core Modules

## 1. Mutation Classification

**Purpose**

Identifies the mutation type and compares wild type and mutant amino acids.

**Responsibilities**

- Parse mutation notation
- Determine mutation class
- Prepare downstream analyses

---

## 2. Amino Acid Property Analysis

**Purpose**

Evaluates physicochemical differences introduced by amino acid substitution.

**Analyzed Properties**

- Charge
- Polarity
- Hydrophobicity
- Molecular Weight
- Amino Acid Size

---

## 3. Grantham Scoring

**Purpose**

Quantifies biochemical severity of amino acid substitutions using the Grantham distance matrix.

**Outputs**

- Numerical Grantham Score
- Conservative / Moderate / Radical classification

---

## 4. Structural Context Analysis

**Purpose**

Determines the structural and functional relevance of the mutated residue.

**Evidence Sources**

- Functional regions
- Binding pocket annotations
- Secondary structure
- Residue role
- Interaction type
- Conservation

---

## 5. Stability Validation

**Purpose**

Integrates experimentally validated or computationally predicted protein stability changes.

**Current Source**

- DynaMut2 ΔΔG predictions - values calculated manually independent of web server ( as the dataset is small)

---

## 6. Unified Resistance Risk Scoring

**Purpose**

Combines evidence from all previous modules into an interpretable resistance assessment.

**Evidence Considered**

- Mutation severity
- Physicochemical change
- Structural relevance
- Stability effect
- Literature evidence

---

## 7. Visualization Engine

Generates publication-quality figures summarizing:

- Unified Risk Scores
- Grantham vs Risk
- Evidence Distribution
- Gene Distribution
- Structural Summary
- Evidence vs Verdict
- Amino Acid Property Changes
- Computational Workflow

---

# Data Flow

```text
CSV Files
      │
      ▼
Core Analysis Modules
      │
      ▼
Integrated Results
      │
      ▼
Visualization
      │
      ▼
CSV + Figures + Biological Interpretation
```

---

# Architectural Characteristics

| Property | Description |
|-----------|-------------|
| Programming Language | Python |
| Architecture | Modular Pipeline |
| Analysis Type | Knowledge-guided Bioinformatics |
| Input | Mutation datasets |
| Output | Interpretable resistance assessment |
| Visualization | Matplotlib |
| Data Storage | CSV |

---

# Future Extensibility

The modular architecture enables straightforward integration of future computational approaches without altering the existing workflow.

Potential extensions include:

- AlphaFold derived structural descriptors
- Protein language model features
- Explainable machine learning
- Multi gene expansion
- Automated structural annotation
- Large-scale mutation datasets

The current version intentionally emphasizes biological interpretability and deterministic reasoning while providing a foundation for future AI assisted evidence integration.