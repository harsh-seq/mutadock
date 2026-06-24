from core.mutation_classifier import analyze_mutation
from core.property_analyzer import analyze_property_change
from core.grantham_scorer import analyze_grantham
from core.structural_context_analyzer import analyze_structural_context
from core.dynamut2_validator import analyze_dynamut_validation
from core.resistance_risk_scorer import analyze_resistance_risk

import pandas as pd


# ==========================================
# LOAD MUTATION DATABASE
# ==========================================

mutation_db = pd.read_csv(
    "data/mutations.csv"
)


# ==========================================
# USER INPUT
# ==========================================

mutation = input(
    "Enter mutation (e.g. S450L, R176H): "
).strip()


# ==========================================
# LOOKUP MUTATION
# ==========================================

match = mutation_db[
    mutation_db["mutation"] == mutation
]

if match.empty:
    raise ValueError(
        f"{mutation} not found in mutation database"
    )

row = match.iloc[0]

gene = row["gene"]
analysis_type = row["analysis_type"]
validation_status = row["validation_status"]


# ==========================================
# MODULE 1
# ==========================================

module1 = analyze_mutation(mutation)

wild_type = module1["wild_type"]
mutant = module1["mutant"]


# ==========================================
# MODULE 2
# ==========================================

module2 = analyze_property_change(
    wild_type,
    mutant
)


# ==========================================
# MODULE 3
# ==========================================

module3 = analyze_grantham(
    wild_type,
    mutant
)

grantham_score = module3["grantham_score"]


# ==========================================
# FULL ANALYSIS PATHWAY (MurB)
# ==========================================

if analysis_type == "full":

    module4 = analyze_structural_context(
        mutation
    )

    module5 = analyze_dynamut_validation(
        mutation,
        module4["impact_level"]
    )

    structural_impact_level = (
        module4["impact_level"]
    )

    structural_impact_driver = (
        module4["structural_impact_driver"]
    )

    agreement = module5["agreement"]

    conserved = module4["conserved"]

    ddg = module5["ddg"]


# ==========================================
# BASIC ANALYSIS PATHWAY
# ==========================================

else:

    structural_impact_level = "LOW"

    structural_impact_driver = (
        "structural_loop"
    )

    agreement = "PARTIAL"

    conserved = False

    ddg = 0


# ==========================================
# MODULE 6
# ==========================================

module6 = analyze_resistance_risk(
    mutation=mutation,
    mutation_type=module1["mutation_type"],
    grantham_score=grantham_score,
    structural_impact_level=
        structural_impact_level,
    structural_impact_driver=
        structural_impact_driver,
    agreement=agreement,
    conserved=conserved,
    ddg=ddg
)


# ==========================================
# FINAL REPORT
# ==========================================

print("\n")
print("=" * 50)
print("MUTADOCK ANALYSIS REPORT")
print("=" * 50)

print(f"\nGene               : {gene}")
print(f"Mutation           : {mutation}")
print(f"Validation Status  : {validation_status}")

print("\n----- Classification -----")

print(
    f"Mutation Type      : "
    f"{module1['mutation_type']}"
)

print(
    f"Wild Type          : "
    f"{module1['wild_type']}"
)

print(
    f"Mutant             : "
    f"{module1['mutant']}"
)

print("\n----- Grantham -----")

print(
    f"Score              : "
    f"{module3['grantham_score']}"
)

print(
    f"Interpretation     : "
    f"{module3['grantham_interpretation']}"
)


print("\n----- Amino Acid Property Analysis -----")

print(
    f"Wild Type Amino Acid : "
    f"{module2['wild_name']} ({module2['wild_type']})"
)

print(
    f"Mutant Amino Acid    : "
    f"{module2['mutant_name']} ({module2['mutant']})"
)

print(
    f"Charge Change        : "
    f"{module2['charge_change']}"
)

print(
    f"Polarity Change      : "
    f"{module2['polarity_change']}"
)

print(
    f"Hydrophobicity       : "
    f"{module2['hydrophobicity_change']}"
)

print(
    f"Molecular Weight     : "
    f"{module2['molecular_weight_change']}"
)

print(
    f"Size Change          : "
    f"{module2['size_change']}"
)

if analysis_type == "full":

    print("\n----- Structural Context -----")

    print(
        f"Residue Role         : "
        f"{module4['role']}"
    )

    print(
        f"Interaction Type     : "
        f"{module4['interaction_type']}"
    )

    print(
        f"Conserved            : "
        f"{module4['conserved']}"
    )

    print(
        f"Domains              : "
        f"{', '.join(module4['domains'])}"
    )

    print(
        f"Secondary Structure  : "
        f"{module4['secondary_structure']}"
    )

    print(
        f"Structural Relevance : "
        f"{module4['relevance_level']}"
    )

    print(
        f"Structural Impact    : "
        f"{module4['impact_level']}"
    )


if analysis_type == "full":

    print("\n----- Stability Validation -----")

    print(
        f"DDG                  : "
        f"{module5['ddg']} kcal/mol"
    )

    print(
        f"Classification       : "
        f"{module5['ddg_class']}"
    )

    print(
        f"Subtier              : "
        f"{module5['ddg_subtier']}"
    )

    print(
        f"Agreement Status     : "
        f"{module5['agreement']}"
    )

print("\n----- Final Verdict -----")

print(
    f"Unified Risk Score : "
    f"{module6['score']}/10"
)

print(
    f"Verdict            : "
    f"{module6['verdict']}"
)

print(
    f"Confidence         : "
    f"{module6['confidence']}"
)

print(
    f"Primary Driver     : "
    f"{module6['primary_driver']}"
)

print("\n----- Biological Interpretation -----")

print(module6["interpretation"])

print("\n")