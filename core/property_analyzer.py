
import pandas as pd


def load_amino_acid_properties():
    """
    Load amino acid property database.

    Returns:
        DataFrame containing amino acid
        biochemical properties.
    """

    df = pd.read_csv("data/amino_acid_properties.csv")

    return df


def get_amino_acid_info(df, amino_acid):
    """
    Retrieve information for a specific amino acid.

    Parameters:
        df : amino acid database
        amino_acid : one-letter amino acid code

    Returns:
        Matching amino acid row
    """

    amino_acid_row = df[df["aa"] == amino_acid]

    return amino_acid_row


def compare_amino_acids(df, wild_type, mutant):
    """
    Compare biochemical properties between wild-type and mutant amino acids.

    Parameters:
        df : amino acid database
        wild_type : original amino acid
        mutant : mutated amino acid

    Returns:
        None
    """

    # Retrieve wild-type information
    wild_info = get_amino_acid_info(df, wild_type)

    # Retrieve mutant information
    mutant_info = get_amino_acid_info(df, mutant)

    # Convert single-row DataFrames into records
    wild_info = wild_info.iloc[0]
    mutant_info = mutant_info.iloc[0]

    print("\n====================================")
    print(" Amino Acid Property Comparison")
    print("====================================")

    print(f"\nWild Type : {wild_info['name']} ({wild_type})")
    print(f"Mutant    : {mutant_info['name']} ({mutant})")

    print("\n----- Property Changes -----")

    print(
        f"Charge             : "
        f"{wild_info['charge']} -> {mutant_info['charge']}"
    )

    print(
        f"Polarity           : "
        f"{wild_info['polarity']} -> {mutant_info['polarity']}"
    )

    print(
        f"Hydrophobicity     : "
        f"{wild_info['hydrophobicity']} -> "
        f"{mutant_info['hydrophobicity']}"
    )

    print(
        f"Molecular Weight   : "
        f"{wild_info['molecular_weight']} -> "
        f"{mutant_info['molecular_weight']}"
    )

    print(
        f"Size               : "
        f"{wild_info['size']} -> {mutant_info['size']}"
    )

    print("\n====================================")



def analyze_property_change(wild_type, mutant):

    df = load_amino_acid_properties()

    wild_info = get_amino_acid_info(df, wild_type).iloc[0]
    mutant_info = get_amino_acid_info(df, mutant).iloc[0]

    return {
        "wild_type": wild_type,
        "mutant": mutant,

        "wild_name": wild_info["name"],
        "mutant_name": mutant_info["name"],

        "charge_change":
            f"{wild_info['charge']} -> {mutant_info['charge']}",

        "polarity_change":
            f"{wild_info['polarity']} -> {mutant_info['polarity']}",

        "hydrophobicity_change":
            f"{wild_info['hydrophobicity']} -> {mutant_info['hydrophobicity']}",

        "molecular_weight_change":
            f"{wild_info['molecular_weight']} -> {mutant_info['molecular_weight']}",

        "size_change":
            f"{wild_info['size']} -> {mutant_info['size']}"
    }


# ==========================================
# Testing Section
# Runs only when file is executed directly
# ==========================================
if __name__ == "__main__":

    # Load amino acid property database
    properties = load_amino_acid_properties()

    # Reference mutation for testing
    # S450L:
    # Serine -> Leucine
    wild_type = "S"
    mutant = "L"

    # Run comparison
    compare_amino_acids(
        properties,
        wild_type,
        mutant
    )