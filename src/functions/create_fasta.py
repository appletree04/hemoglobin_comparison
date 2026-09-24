import json
from .paths import ROOT
from pathlib import Path

def generate_fasta(data, file_path:Path, sequence_type, objs):

    with open(file_path, "w") as f:
        for value in data:
            f.write(f">{value} {objs[value]["gene"]} organism={objs[value]["organism"]} gene_id={objs[value]["gene_id"]}\n")
            f.write(objs[value][sequence_type] + "\n")


def create_fasta(fasta_path:Path):
    with open(f"{ROOT}/data/processed_data/data.json") as d:
            objs = json.load(d)

    folders = {}

    for key, value in objs.items():
         folders.setdefault(
              value["organism"], []
         ).append(key)
    
    sequences = ["gene_sequence", "cds", "rna", "aa_sequence"]

    for folder in folders.keys():

        folder_path = Path(f"{fasta_path}/{folder}")
        Path.mkdir(folder_path, parents=True, exist_ok=True)

        for sequence in sequences:
            extension = "faa" if sequence == "aa_sequence" else "fna"
            generate_fasta(
                folders[folder],
                Path(f"{folder_path}/{sequence}.{extension}"),
                sequence,
                objs
            )

    pass