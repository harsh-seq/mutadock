import pandas as pd
import re

# =========================
# INPUT MUTATION
# =========================
mutation = "R176H"      # Change to Y210F or S257A

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