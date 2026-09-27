from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
RAW_DATA = Path(f"{ROOT}/data/raw_data")
FASTA = Path(f"{ROOT}/data/fasta")
FIGURES = Path(f"{ROOT}/data/figures")