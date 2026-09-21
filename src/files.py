# json library is a built in library with functions to manipulate json files.
# We also need to import the fasta function from the fasta.py file
import json
from fasta import fasta

# Define a function that loads the data from the FASTA files and returns
# the data that we want in a structured dict format.
# The parameter is the name of the folder that the data is in.
def load_data(folder:str):

    # The folders contain four files each and we need the data from each of them.
    cds = fasta(f"../raw_data/{folder}/cds.fna")
    gene = fasta(f"../raw_data/{folder}/gene.fna")
    rna = fasta(f"../raw_data/{folder}/rna.fna")
    aa = fasta(f"../raw_data/{folder}/protein.faa")

    # Once we have the data, we return the name of the folder and a dict with
    # the data organised as shown below.
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
        "source": f"../raw_data/{folder}",
        "alpha_globin": folder[-1]
    }

# We are creating a single json file with data from all the files.
# So, make a function for that. We pass in a list of names of the folders
# that the files are in as a list parameter.
def create_json(folders:list):

    # all_dicts variable will hold the data from all the files as a nested dict.
    all_dicts = dict()

    # For each folder, we load the data and insert it into the all_dict with the
    # folder name as the key to the data
    for folder in folders:
        key, record = load_data(folder)
        all_dicts[key] = record

    # Then we open the location and file into which the data is to be inserted into
    # and dump the data into the json file in JSON format.
    with open("../processed_data/data.json", "w") as file:
        json.dump(all_dicts, file, indent=4)

# List of the names of all the folders
all_folders = [
    "D_rerio_hbaa1",
    "D_rerio_hbaa2",
    "H_sapiens_HbA1",
    "H_sapiens_HbA2",
    "M_musculus_Hba-a1",
    "M_musculus_Hba-a2",
    "P_troglodytes_HbA1",
    "P_troglodytes_HbA2"
]

# Call the create_json function with a list of all the folders
create_json(all_folders)

# print(load_data("../raw_data/H_sapiens_HbA1", "H_sapiens_HbA1"))
# print(create_json(["H_sapiens_HbA1", "H_sapiens_HbA2"]))