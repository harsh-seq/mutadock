import pandas as pd
import re

# =========================
# INPUT MUTATION
# =========================
mutation = "S257A"      # Change to Y210F or S257A or R176H

# Extract residue number
residue_id = int(re.search(r"\d+", mutation).group())

# =========================
# LOAD CSV FILES
# =========================
pocket_df = pd.read_csv("data/pocket_residues.csv")
domains_df = pd.read_csv("data/functional_regions.csv")
ss_df = pd.read_csv("data/secondary_structure.csv")

# =========================
# POCKET RESIDUE LOOKUP
# =========================
pocket_match = pocket_df[pocket_df["residue_id"] == residue_id]

if not pocket_match.empty:
    role = pocket_match.iloc[0]["residue_role"]
    interaction = pocket_match.iloc[0]["interaction_type"]
    conserved = pocket_match.iloc[0]["conserved"]
else:
    role = "None"
    interaction = "None"
    conserved = False

# =========================
# DOMAIN LOOKUP
# =========================
domains = []

for _, row in domains_df.iterrows():
    if row["residue_start"] <= residue_id <= row["residue_end"]:
        domains.append(row["region_name"])

# =========================
# SECONDARY STRUCTURE LOOKUP
# =========================
secondary_structure = "Loop"

for _, row in ss_df.iterrows():
    if row["residue_start"] <= residue_id <= row["residue_end"]:
        secondary_structure = row["ss_type"]
        break


def generate_interpretation(context):

    mutation = context["mutation"]
    residue_id = context["residue_id"]
    role = context["role"]
    interaction = context["interaction_type"]
    conserved = context["conserved"]
    domains = context["domains"]
    ss = context["secondary_structure"]

    interpretation = []

    # --------------------------------
    # LOCATION + ROLE
    # --------------------------------
    if role != "None":
        interpretation.append(
            f"Residue {residue_id} ({mutation}) is a literature-validated pocket residue "
            f"with role '{role}', contributing through {interaction} interactions."
        )
    else:
        interpretation.append(
            f"Residue {residue_id} ({mutation}) is not currently annotated as a curated pocket residue."
        )

    # --------------------------------
    # DOMAIN CONTEXT
    # --------------------------------
    if len(domains) > 1:
        interpretation.append(
            f"This position lies within overlapping domains: {', '.join(domains)}, "
            f"suggesting involvement in multiple functional regions."
        )

    elif len(domains) == 1:
        interpretation.append(
            f"This position lies within {domains[0]}."
        )

    else:
        interpretation.append(
            "No functional domain annotation is available."
        )

    # --------------------------------
    # CONSERVATION
    # --------------------------------
    if conserved:
        interpretation.append(
            "This residue is evolutionarily conserved, increasing confidence that disruption here may be biologically significant."
        )
    else:
        interpretation.append(
            "Conservation evidence for this position is currently unavailable."
        )

    # --------------------------------
    # SECONDARY STRUCTURE
    # --------------------------------
    interpretation.append(
        f"Secondary structure context: {ss}."
    )

    # --------------------------------
    # SPECIAL MURB LOGIC
    # --------------------------------
    if role == "proton_donor":
        interpretation.append(
            "Because this residue participates directly in catalytic proton transfer, substitutions here may affect enzymatic activity."
        )

    elif role == "substrate_contact":
        interpretation.append(
            "Because this residue contributes to substrate recognition, substitutions here may alter substrate-binding interactions."
        )

    elif role == "structural_loop":
        interpretation.append(
            "This residue contributes to local structural organization, although the precise functional impact of substitution remains uncertain."
        )


# --------------------------------
    # CLAUDE REVIEW IMPROVEMENTS
    # --------------------------------
    if interaction == "acid_base_catalysis":
        interpretation.append(
            "This residue participates directly in catalytic chemistry; substitutions may disrupt enzymatic proton-transfer mechanisms."
        )

    elif interaction == "electrostatic":
        interpretation.append(
            "This residue contributes electrostatic interactions important for substrate recognition; substitutions may weaken local binding interactions."
        )

    elif interaction == "steric":
        interpretation.append(
            "The residue appears to contribute primarily through steric packing, making functional consequences more difficult to predict with confidence."
        )

    elif interaction == "hydrogen_bond":
        interpretation.append(
            "This residue may participate in hydrogen-bond networks that contribute to structural stability or ligand recognition."
        )


    # --------------------------------
    # FINAL STATEMENT
    # --------------------------------
    interpretation.append(
        "This assessment represents a structural-context prediction and should be interpreted alongside biochemical or experimental validation."
    )

    return "\n\n".join(interpretation)


def calculate_relevance(context):

    score = 0

    if context["role"] != "None":
        score += 2

    if context["conserved"]:
        score += 1

    if len(context["domains"]) > 1:
        score += 1

    if context["role"] != "None":
        score += 3

    if score >= 6:
        level = "HIGH"
    elif score >= 3:
        level = "MODERATE"
    else:
        level = "LOW"

    return score, level


def calculate_impact(context):

    score = 0

    interaction = context["interaction_type"]

    if interaction == "acid_base_catalysis":
        score += 3

    elif interaction == "electrostatic":
        score += 2

    elif interaction == "hydrogen_bond":
        score += 2

    elif interaction == "steric":
        score += 1

    if score >= 3:
        level = "HIGH"
    elif score >= 2:
        level = "MODERATE"
    else:
        level = "LOW"

    return score, level

# =========================
# FINAL CONTEXT
# =========================
context = {
    "mutation": mutation,
    "residue_id": residue_id,
    "role": role,
    "interaction_type": interaction,
    "conserved": conserved,
    "domains": domains,
    "secondary_structure": secondary_structure
}

# =========================
# OUTPUT
# =========================
print("\n===== STRUCTURAL CONTEXT =====\n")

for key, value in context.items():
    print(f"{key}: {value}")


print("\n===== INTERPRETATION =====\n")
print(generate_interpretation(context))

print("\n===== STRUCTURAL RELEVANCE =====\n")

relevance_score, relevance_level = calculate_relevance(context)

print(f"Score : {relevance_score}")
print(f"Level : {relevance_level}")


print("\n===== STRUCTURAL IMPACT =====\n")

impact_score, impact_level = calculate_impact(context)

print(f"Score : {impact_score}")
print(f"Level : {impact_level}")