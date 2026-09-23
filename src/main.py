from files import call_create_json
from data import generate_files
from align import generate_alignment

def main():
    call_create_json()
    generate_files()
    generate_alignment()

if __name__ == "__main__":
    main()