from .paths import ROOT
from Bio import AlignIO
from pathlib import Path
from pymsaviz import MsaViz

def create_figures(folder, file):

    alignment = AlignIO.read(
        f"{ROOT}/data/aligned/{folder}/{file}.{"faa" if file == "aa_sequence" else "fna"}", "fasta"
    )

    mv = MsaViz(alignment, wrap_length=120, color_scheme="Clustal", show_count=True, show_consensus=True, show_grid=True)
    fig = mv.plotfig()
    fig.savefig(f"{ROOT}/data/figures/{folder}/{file}.png", bbox_inches="tight", pad_inches=0.2)


def figures():

    folders = [
        p.name
        for p in Path(f"{ROOT}/data/aligned").iterdir()
        if p.is_dir()
    ]
    files = ["gene_sequence", "cds", "rna", "aa_sequence"]

    Path.mkdir(Path(f"{ROOT}/data/figures"), parents=True, exist_ok=True)

    for folder in folders:
        Path.mkdir(Path(f"{ROOT}/data/figures/{folder}"), parents=True, exist_ok=True)
        for file in files:
            create_figures(folder, file)
# create_figures("D_rerio", "cds")