
import pandas as pd


def load_grantham_matrix():
    """
    Load Grantham substitution matrix.

    Returns:
        DataFrame containing Grantham scores
        between amino acid pairs.
    """

    matrix = pd.read_csv(
        "data/grantham_full.csv",
        index_col=0
    )

    return matrix


def get_grantham_score(matrix, wild_type, mutant):
    """
    Retrieve Grantham score for an amino acid substitution.

    Parameters:
        matrix : Grantham matrix DataFrame
        wild_type : original amino acid
        mutant : mutated amino acid

    Returns:
        Integer Grantham score
    """

    score = matrix.loc[wild_type, mutant]

    return int(score)


def interpret_grantham_score(score):
    """
    Interpret biological significance
    of a Grantham score.

    Grantham Categories:
    0-50   : Conservative
    51-100 : Moderately Conservative
    101-150: Moderately Radical
    >150   : Radical
    """

    if score <= 50:
        return "Conservative Substitution"

    elif score <= 100:
        return "Moderately Conservative Substitution"

    elif score <= 150:
        return "Moderately Radical Substitution"

    else:
        return "Radical Substitution"


def analyze_grantham_change(matrix, wild_type, mutant):
    """
    Perform complete Grantham analysis.

    Parameters:
        matrix : Grantham matrix
        wild_type : original amino acid
        mutant : mutated amino acid
    """

    score = get_grantham_score(
        matrix,
        wild_type,
        mutant
    )

    interpretation = interpret_grantham_score(score)

    print("\n====================================")
    print(" Grantham Score Analysis")
    print("====================================")

    print(f"\nWild Type : {wild_type}")
    print(f"Mutant    : {mutant}")

    print(f"\nGrantham Score : {score}")

    print(
        f"Interpretation : {interpretation}"
    )

    print("\n====================================")



def analyze_grantham(wild_type, mutant):

    matrix = load_grantham_matrix()

    score = get_grantham_score(
        matrix,
        wild_type,
        mutant
    )

    interpretation = interpret_grantham_score(score)

    return {
        "wild_type": wild_type,
        "mutant": mutant,
        "grantham_score": score,
        "grantham_interpretation": interpretation
    }




# ==========================================
# Testing Section
# Runs only when file is executed directly
# ==========================================
if __name__ == "__main__":

    # Test Mutation:
    # S = Serine
    # L = Leucine
    # Expected Grantham Score = 145

    wild_type = "S"
    mutant = "L"

    grantham_matrix = load_grantham_matrix()

    analyze_grantham_change(
        grantham_matrix,
        wild_type,
        mutant
    )