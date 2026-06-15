
# MutaDock Phase 1
# Mutation Classification Module
# ==========================================

# Import Regular Expression module
import re


def parse_mutation(mutation):
    """
    Parse mutation format like:

    S450L
    A123T
    G78D

    Returns a dictionary containing:
    - wild_type amino acid
    - position
    - mutant amino acid
    """

    # Regex pattern:
    # Letter + Number + Letter
    pattern = r"^([A-Z])(\d+)([A-Z*])$"

    # Check if mutation follows the pattern
    match = re.match(pattern, mutation)



    # If mutation format is invalid
    if not match:
        raise ValueError("Invalid mutation format")

    # Return parsed mutation information
    return {
        "wild_type": match.group(1),
        "position": int(match.group(2)),
        "mutant": match.group(3)
    }



def classify_mutation(parsed):

    if parsed["mutant"] == "*":
        return "Nonsense"

    elif parsed["wild_type"] == parsed["mutant"]:
        return "Silent"

    else:
        return "Missense"


# ==========================================
# Test Block
# Runs only when file is executed directly
# ==========================================
if __name__ == "__main__":

    #  reference mutation for testing
    mutation = "S450L"

    # Parse mutation
    result = parse_mutation(mutation)

    
    # Classify mutation
    mutation_type = classify_mutation(result)

    # Display parsed information
    print("Wild Type Residue :", result["wild_type"])
    print("Position          :", result["position"])
    print("Mutant Residue    :", result["mutant"])
    print("Mutation Type     :", mutation_type)