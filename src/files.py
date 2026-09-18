import json
from fasta import fasta

def load_data(folder):

    cds = fasta(f"../raw_data/{folder}/cds.fna")
    gene = fasta(f"../raw_data/{folder}/gene.fna")
    rna = fasta(f"../raw_data/{folder}/rna.fna")
    aa = fasta(f"../raw_data/{folder}/protein.faa")


    return folder, {
        "organism": gene["organism"],
        "gene": gene["Gene"],
        "gene_id": gene["GeneID"],
        "chromosome": gene["chromosome"],
        "gene_sequence": gene["Sequence"],
        "cds": cds["Sequence"],
        "rna": rna["Sequence"],
        "aa_sequence": aa["Sequence"],
        "gene_accession": gene["Accession"],
        "cds_accession": cds["Accession"],
        "rna_accession": rna["Accession"],
        "aa_accession": aa["Accession"],
        "source": f"../raw_data/{folder}"
    }

def create_json(folders:list):

    all_dicts = dict()
    for folder in folders:
        key, record = load_data(folder)
        all_dicts[key] = record

    with open("../processed_data/data.json", "w") as file:
        json.dump(all_dicts, file, indent=4)

all_folders = [
    "D_rerio_hbaa1",
    "D_rerio_hbaa2",
    "H_sapiens_HbA1",
    "H_sapiens_HbA2",
    "M_musculus_Hba-a1",
    "M_musculus_Hba-a2",
    "P_troglodyes_HbA1",
    "P_troglodyes_HbA2"
]

create_json(all_folders)

# print(load_data("../raw_data/H_sapiens_HbA1", "H_sapiens_HbA1"))
# print(create_json(["H_sapiens_HbA1", "H_sapiens_HbA2"]))