import pandas as pd


# =========================
# INPUTS
# =========================

mutation = "R176H"

# Simulated Module 4 output
structural_impact_level = "MODERATE"


# =========================
# LOAD DYNAMUT2 DATA
# =========================

dynamut_df = pd.read_csv("data/dynamut2_results.csv")


# =========================
# LOOKUP MUTATION
# =========================

match = dynamut_df[dynamut_df["mutation"] == mutation]

if match.empty:
    raise ValueError(f"{mutation} not found in DynaMut2 dataset")


row = match.iloc[0]

ddg = row["ddg_kcal_mol"]


# =========================
# DDG CLASSIFICATION
# =========================

def classify_ddg(ddg):

    if ddg > 0.5:
        return "Stabilizing"

    elif -0.5 <= ddg <= 0.5:
        return "Neutral"

    else:
        return "Destabilizing"


# =========================
# DDG SUBTIER
# =========================

def assign_ddg_subtier(ddg):

    if ddg >= -0.5:
        return "N/A"

    elif -1.5 <= ddg < -0.5:
        return "Mild"

    elif -3.0 <= ddg < -1.5:
        return "Moderate"

    else:
        return "Strong"


# =========================
# AGREEMENT ANALYSIS
# =========================

def check_agreement(structural_impact_level,
                    ddg_class,
                    ddg):

    impact_map = {
        "LOW": 0,
        "MODERATE": 1,
        "HIGH": 2
    }

    impact_score = impact_map[structural_impact_level]

    if ddg_class == "Destabilizing":

        if ddg < -3.0:
            ddg_score = 2
        else:
            ddg_score = 1

    else:
        ddg_score = 0

    difference = abs(impact_score - ddg_score)

    if difference == 0:
        return "CONVERGENT"

    elif difference == 1:
        return "PARTIAL"

    else:
        return "CONTRADICTORY"


# =========================
# INTERPRETATION
# =========================

def generate_interpretation(
        mutation,
        ddg,
        ddg_class,
        ddg_subtier,
        agreement):

    interpretation = []

    interpretation.append(
        f"DynaMut2 predicts a stability change of {ddg:.2f} kcal/mol."
    )

    interpretation.append(
        f"The mutation is classified as {ddg_class.lower()}."
    )

    if ddg_class == "Destabilizing":
        interpretation.append(
            f"The magnitude corresponds to a {ddg_subtier.lower()} destabilizing effect."
        )

    if agreement == "CONVERGENT":
        interpretation.append(
            "Structural-context and stability evidence converge on a similar impact assessment."
        )

    elif agreement == "PARTIAL":
        interpretation.append(
            "Structural-context and stability evidence show partial agreement."
        )

    else:
        interpretation.append(
            "Structural-context and stability evidence provide contrasting signals and may reflect different aspects of mutation impact."
        )

    return "\n\n".join(interpretation)


# =========================
# ANALYSIS
# =========================

ddg_class = classify_ddg(ddg)

ddg_subtier = assign_ddg_subtier(ddg)

agreement = check_agreement(
    structural_impact_level,
    ddg_class,
    ddg
)

interpretation = generate_interpretation(
    mutation,
    ddg,
    ddg_class,
    ddg_subtier,
    agreement
)


# =========================
# OUTPUT
# =========================

print("\n===== DYNAMUT2 VALIDATION =====\n")

print(f"Mutation           : {mutation}")
print(f"DDG                : {ddg}")
print(f"Classification     : {ddg_class}")
print(f"Subtier            : {ddg_subtier}")
print(f"Agreement Status   : {agreement}")

print("\n===== INTERPRETATION =====\n")

print(interpretation)