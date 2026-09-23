import json

def create_fasta(data, file_path, sequence_type):

    with open("../data/processed_data/data.json") as d:
        objs = json.load(d)

    with open(file_path, "w") as f:
        for value in data:
            f.write(f">{value} {objs[value]["gene"]} organism={objs[value]["organism"]} gene_id={objs[value]["gene_id"]}\n")
            f.write(objs[value][sequence_type] + "\n")


def generate_files():
    
    folders = {
        "alpha1" : ["H_sapiens_HbA1", "P_troglodytes_HbA1", "M_musculus_Hba-a1", "D_rerio_hbaa1"],
        "alpha2" : ["H_sapiens_HbA2", "P_troglodytes_HbA2", "M_musculus_Hba-a2", "D_rerio_hbaa2"],
        "H_sapiens" : ["H_sapiens_HbA1", "H_sapiens_HbA2"],
        "P_troglodytes" : ["P_troglodytes_HbA1", "P_troglodytes_HbA2"],
        "M_Musculus" : ["M_musculus_Hba-a1", "M_musculus_Hba-a2"],
        "D_rerio" : ["D_rerio_hbaa1", "D_rerio_hbaa2"]
    }
    
    sequences = ["gene_sequence", "cds", "rna", "aa_sequence"]

    for folder in folders.keys():
        for sequence in sequences:
            extension = "faa" if sequence == "aa_sequence" else "fna"
            create_fasta(
                folders[folder],
                f"../data/fasta/{folder}/{sequence}.{extension}",
                sequence
            )

    pass
