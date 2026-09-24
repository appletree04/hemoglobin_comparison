from functions import (
    organise, create_fasta, align, figures, ROOT, RAW_DATA, FASTA, FIGURES
)

def main():
    organise(RAW_DATA)
    create_fasta(FASTA)
    align(FASTA)
    figures(FIGURES)

main()

# figures()