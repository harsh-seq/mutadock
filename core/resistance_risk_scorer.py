# ==========================================
# MutaDock Phase 6
# Resistance Risk Scorer
# ==========================================



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
# PIPELINE FUNCTION
# =========================

def analyze_resistance_risk(
        mutation,
        gene,
        evidence_category,
        mutation_type,
        grantham_score,
        structural_impact_level,
        structural_impact_driver,
        agreement,
        conserved,
        ddg):

    # ======================================
    # RPOB / KATG CLINICAL SCORING
    # ======================================

    if gene in ["rpoB", "katG"]:

        if evidence_category == "WHO Confirmed":

            score = 9
            verdict = "Clinically Confirmed Resistance"
            confidence = "VERY HIGH"
            primary_driver = "WHO Clinical Evidence"

            interpretation = (
                "Clinical evidence strongly supports "
                "this mutation as a drug-resistance determinant."
            )

        elif evidence_category == "Associated with Resistance":

            score = 8
            verdict = "Clinically Supported Resistance"
            confidence = "HIGH"
            primary_driver = "WHO Clinical Evidence"

            interpretation = (
                "Clinical evidence supports an association "
                "with drug resistance."
            )

        elif evidence_category == "Uncertain Significance":

            if grantham_score >= 100:
                score = 6
            else:
                score = 4

            verdict = "Uncertain Clinical Significance"
            confidence = "MODERATE"
            primary_driver = "WHO Clinical Classification"

            interpretation = (
                "Current clinical evidence is insufficient "
                "for definitive classification."
            )

        elif evidence_category == "Not Associated with Resistance":

            score = 2
            verdict = "Not Associated with Resistance"
            confidence = "HIGH"
            primary_driver = "WHO Clinical Evidence"

            interpretation = (
                "Available clinical evidence does not support "
                "an association with drug resistance."
            )

        else:

             raise ValueError(
                f"Unknown evidence category: {evidence_category}"
    )

        return {

            "mutation": mutation,
            "mutation_type": mutation_type,

            "score": score,
            "verdict": verdict,
            "confidence": confidence,

            "primary_driver": primary_driver,

            "grantham_score": grantham_score,

            "structural_impact": "N/A",

            "ddg": "N/A",

            "agreement": "Clinical Evidence",

            "interpretation": interpretation
        }

    # ======================================
    # MURB STRUCTURAL SCORING
    # ======================================

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

    return {

        "mutation": mutation,
        "mutation_type": mutation_type,

        "score": score,

        "verdict": verdict,

        "confidence": confidence,

        "primary_driver":
            driver_map[structural_impact_driver],

        "grantham_score": grantham_score,

        "structural_impact":
            structural_impact_level,

        "ddg": ddg,

        "agreement": agreement,

        "interpretation":
            interpretation
    }



# =========================
# OUTPUT
# =========================

if __name__ == "__main__":

    results = analyze_resistance_risk(
        mutation="Y210F",
        gene="MurB",
        evidence_category="Structural Showcase",
        mutation_type="Missense",
        grantham_score=22,
        structural_impact_level="LOW",
        structural_impact_driver="structural_loop",
        agreement="PARTIAL",
        conserved=True,
        ddg=-0.70
    )

    print("\n===== FINAL VERDICT =====\n")

    print(f"Mutation : {results['mutation']}")

    print(
        f"\nUnified Resistance Score : "
        f"{results['score']}/10"
    )

    print("\nVerdict :")
    print(results["verdict"])

    print("\nConfidence :")
    print(results["confidence"])

    print("\nPrimary Driver :")
    print(results["primary_driver"])

    print("\nSupporting Evidence :")

    print(
        f"Grantham Score     = "
        f"{results['grantham_score']}"
    )

    print(
        f"Structural Impact  = "
        f"{results['structural_impact']}"
    )

    print(
        f"DDG                = "
        f"{results['ddg']}"
    )

    print(
        f"Agreement          = "
        f"{results['agreement']}"
    )

    print("\nFINAL INTERPRETATION :\n")

    print(results["interpretation"])