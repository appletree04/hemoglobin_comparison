import subprocess
from pathlib import Path

muscle = Path("../tools/muscle.exe")

def run_muscle(folder, file):
    subprocess.run(
        [
            muscle,
            "-in", f"../data/fasta/{folder}/{file}",
            "-out", f"../data/aligned/{folder}/{file}"
        ], check=True
    )

def generate_alignment():
    folders = ["alpha1", "alpha2", "D_rerio", "H_sapiens", "M_musculus", "P_troglodytes"]
    files = ["gene_sequence.fna", "rna.fna", "cds.fna", "aa_sequence.faa"]

    for folder in folders:
        for file in files:
            run_muscle(folder, file)

    pass

generate_alignment()