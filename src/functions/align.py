import subprocess
from pathlib import Path
from .paths import ROOT
muscle = Path(f"{ROOT}/tools/muscle.exe")

def run_muscle(folder, file):
    Path.mkdir(Path(f"{ROOT}/data/aligned"), parents=True, exist_ok=True)
    subprocess.run(
        [
            muscle,
            "-in", f"{ROOT}/data/fasta/{folder}/{file}",
            "-out", f"{ROOT}/data/aligned/{folder}/{file}"
        ], check=True
    )

def align(fasta_path:Path):
    folders = [
        p.name
        for p in fasta_path.iterdir()
        if p.is_dir()
    ]
    files = ["gene_sequence.fna", "rna.fna", "cds.fna", "aa_sequence.faa"]

    for folder in folders:
        Path.mkdir(Path(f"{ROOT}/data/aligned/{folder}"), parents=True, exist_ok=True)
        for file in files:
            run_muscle(folder, file)

    pass