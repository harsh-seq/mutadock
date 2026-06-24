# ==========================================
# MutaDock Phase 6
# Resistance Risk Scorer
# ==========================================

# =========================
# INPUTS
# =========================

mutation = "Y210F"

# Simulated outputs from previous modules

mutation_type = "Missense"

grantham_score = 22

structural_impact_level = "LOW"

structural_impact_driver = "structural_loop"

agreement = "PARTIAL"

conserved = True

ddg = -0.70

# =========================
# DRIVER DISPLAY NAMES
# =========================

driver_map = {
    "proton_donor": "Catalytic Proton Donor",
    "substrate_contact": "Substrate Recognition Residue",
    "structural_loop": "Structural Organization Residue"
}


# =========================
# VERDICT ENGINE
# =========================

def determine_verdict(
        driver,
        impact_level,
        agreement):

    # Mechanistic Rule

    if driver == "proton_donor":
        return "Mechanistically Disruptive"

    # Evidence Convergence

    if impact_level == "HIGH" and agreement == "CONVERGENT":
        return "Convergent High Risk"

    elif impact_level == "MODERATE" and agreement == "CONVERGENT":
        return "Convergent Moderate Risk"

    elif agreement == "PARTIAL":
        return "Indeterminate"

    else:
        return "Low Risk"


# =========================
# CONFIDENCE
# =========================

def determine_confidence(
        verdict,
        agreement,
        conserved):

    if verdict == "Mechanistically Disruptive":

        if conserved:
            return "HIGH"

        return "MODERATE"

    if agreement == "CONVERGENT":
        return "MODERATE"

    return "LOW"


# =========================
# UNIFIED SCORE
# =========================

def calculate_score(
        verdict,
        grantham_score):

    if verdict == "Mechanistically Disruptive":
        return 9

    elif verdict == "Convergent High Risk":
        return 8

    elif verdict == "Convergent Moderate Risk":
        return 6

    elif verdict == "Indeterminate":

        if grantham_score >= 100:
            return 5

        return 4

    else:
        return 2


# =========================
# INTERPRETATION
# =========================

def generate_interpretation(
        verdict,
        driver):

    if verdict == "Mechanistically Disruptive":

        return (
            "Loss of a catalytic proton donor residue "
            "may significantly affect enzymatic activity."
        )

    elif verdict == "Convergent High Risk":

        return (
            "Multiple independent evidence sources "
            "support a high-risk interpretation."
        )

    elif verdict == "Convergent Moderate Risk":

        return (
            "Structural and stability evidence "
            "converge on a moderate functional impact."
        )

    elif verdict == "Indeterminate":

        return (
            "Available evidence remains mixed and "
            "additional experimental validation is recommended."
        )

    else:

        return (
            "Current evidence suggests limited "
            "functional impact."
        )


# =========================
# ANALYSIS
# =========================

verdict = determine_verdict(
    structural_impact_driver,
    structural_impact_level,
    agreement
)

confidence = determine_confidence(
    verdict,
    agreement,
    conserved
)

score = calculate_score(
    verdict,
    grantham_score
)

interpretation = generate_interpretation(
    verdict,
    structural_impact_driver
)


# =========================
# OUTPUT
# =========================

print("\n===== FINAL VERDICT =====\n")

print(f"Mutation : {mutation}")

print(f"\nUnified Resistance Score : {score}/10")

print("\nVerdict :")
print(verdict)

print("\nConfidence :")
print(confidence)


print("\nPrimary Driver :")
print(driver_map[structural_impact_driver])

print("\nSupporting Evidence :")
print(f"Grantham Score     = {grantham_score}")
print(f"Structural Impact  = {structural_impact_level}")
print(f"DDG                = {ddg}")
print(f"Agreement          = {agreement}")

print("\nFINAL INTERPRETATION :\n")

print(interpretation)