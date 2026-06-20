import csv

PDB_FILE = "data/structures/5JZX.pdb"
OUTPUT_FILE = "data/secondary_structure.csv"

rows = []

with open(PDB_FILE, "r") as pdb:

    for line in pdb:

        if line.startswith("HELIX"):

            start_residue = int(line[21:25].strip())
            end_residue = int(line[33:37].strip())

            rows.append([
                start_residue,
                end_residue,
                "Helix"
            ])

        elif line.startswith("SHEET"):

            start_residue = int(line[22:26].strip())
            end_residue = int(line[33:37].strip())

            rows.append([
                start_residue,
                end_residue,
                "Sheet"
            ])

with open(OUTPUT_FILE, "w", newline="") as csvfile:

    writer = csv.writer(csvfile)

    writer.writerow([
        "residue_start",
        "residue_end",
        "ss_type"
    ])

    writer.writerows(rows)

print(f"Successfully generated {len(rows)} entries")
print(f"Saved to: {OUTPUT_FILE}")