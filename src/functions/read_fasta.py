#  A local file containing functions to parse fasta files into a list of dicts.

# Totally inefficient and would not recommend.
# Better to use a library like Biopython.
# But I am trying to learn to work with python and fasta files.
# So doing it this way helps.
# I hope.

from re import findall

# Some fasta files, like some of the ones I have chosen, have multiple records
# within them. So, you can't just do "".join(open(file,"r").readlines()[1:])

# Define a function with a string parameter. The paramereter in this case will
# always be the path to the file. For example, for the human HbA1 coding sequence
# the path will be "../raw_data/H_sapiens_HbA1/cds.fna".
def fasta_parser(file_location:str):

    # Variable x records the locations of where the objects with the headerlines(">")
    # thereby detecting where one record starts and, potentially, where one record ends.
    x = list()
    # An empty list variable that will later contain all the records spliced from the
    # fasta file as a nested list.
    records = list()

    # Open the fasta file and define variable data as a list containing everything in 
    # the file.
    with open(file_location, "r") as file:
        data = file.readlines()

        # Iterate through data and find the locations of where each record starts. At the
        # end, add the length of the list "data" as that's the location which the final
        # record ends.
        for i in range(len(data)):
            if data[i].startswith(">"):
                x.append(i)
        x.append(len(data))

        # Redefine the sequence variable as a nested list of records from the fasta file.
        records = [data[x[i]:x[i+1]] for i in range(len(x)-1)]
    
    # Return the sequences variable, which is a nested list of records from the fasta
    # file.
    return records

# fasta_parser opens the file and separates all records in the file into nested lists.
# This data should be better organised, a list of nested records is just messy.

# Define the function fasta_sorter which takes in a list as a parameter.
def fasta_sorter(records:list):

    # The records will be returned as a list so define "organised" variable as an empty
    # list.
    organised = list()

    # Iterate through each record in records
    for record in records:

        # Information within each record will be put into a dict.
        record_dict = dict()

        # Isolate the gene name and the accession from the headline
        x = record[0].split("[")[0].split()
        record_dict["Gene"] = x[1]
        record_dict["Accession"] = x[0][1:]

        # Merge the sequence lines together to produce a single string containing the entire
        # sequence and assign it to the key "sequence" within the accession dict.
        record_dict["Sequence"] = "".join(record[1:]).replace("\n", "")

        # Preserve the headline of the record as is, just to ensure no loss of data.
        record_dict["Headline"] = record[0][:len(record[0])-1]

        # There are a few metadata within the headline organised into [key=value] format
        # so assign them as "key : value" within the dict using the findall function.
        for key, value in findall(r"\[(.*?)=(.*?)\]", record[0]):
            record_dict[key] = value

        # Apend the organised dict to the "organised" list
        organised.append(record_dict)

    # Return the list of records
    return organised

# Some files could have multiple records within so we need to clean the duplicates.
def clean_duplicates(records:list):

    # Initiate two variables, one set and one list
    key_set = set()
    unique = list()

    # Iterate through the records
    for record in records:

        # I've decided to identify duplicates by comparing the gene ID and the sequence.
        # So, create a tuple with those two values.
        key = (
            record["GeneID"],
            record["Sequence"]
        )

        # Check if the gene ID and sequence match any that are already recorded.
        # If not, record the values and append the record to a list of unique
        # records.
        if key not in key_set:
            key_set.add(key)
            unique.append(record)

    # Return a list of unique records with no duplicates
    return unique[0]

# Example output:
# {
#     'Gene': 'HBA1',
#     'Accession': 'NC_000016.10:176680-177522',
#     'Sequence': 'ACTCTTCTGGTCCCCACAGACTCAGAGAGAACCCACCATGGTGCTGTCTCCTGCCGACAAGACCAACGTCAAGGCCGCCTGGGGTAAGGTCGGCGCGCACGCTGGCGAGTATGGTGCGGAGGCCCTGGAGAGGTGAGGCTCCCTCCCCTGCTCCGACCCGGGCTCCTCGCCCGCCCGGACCCACAGGCCACCCTCAACCGTCCTGGCCCCGGACCCAAACCCCACCCCTCACTCTGCTTCTCCCCGCAGGATGTTCCTGTCCTTCCCCACCACCAAGACCTACTTCCCGCACTTCGACCTGAGCCACGGCTCTGCCCAGGTTAAGGGCCACGGCAAGAAGGTGGCCGACGCGCTGACCAACGCCGTGGCGCACGTGGACGACATGCCCAACGCGCTGTCCGCCCTGAGCGACCTGCACGCGCACAAGCTTCGGGTGGACCCGGTCAACTTCAAGGTGAGCGGCGGGCCGGGAGCGATCTGGGTCGAGGGGCGAGATGGCGCCTTCCTCGCAGGGCAGAGGATCACGCGGGTTGCGGGAGGTGTAGCGCAGGCGGCGGCTGCGGGCCTGGGCCCTCGGCCCCACTGACCCTCTTCTCTGCACAGCTCCTAAGCCACTGCCTGCTGGTGACCCTGGCCGCCCACCTCCCCGCCGAGTTCACCCCTGCGGTGCACGCCTCCCTGGACAAGTTCCTGGCTTCTGTGAGCACCGTGCTGACCTCCAAATACCGTTAAGCTGGAGCCTCGGTGGCCATGCTTCTTGCCCCTTGGGCCTCCCCCCAGCCCCTCCTCCCCTTCCTGCACCCGTACCCCCGTGGTCTTTGAATAAAGTCTGAGTGGGCGGCA',
#     'Headline': '>NC_000016.10:176680-177522 HBA1 [organism=Homo sapiens] [GeneID=3039] [chromosome=16]',
#     'organism': 'Homo sapiens',
#     'GeneID': '3039',
#     'chromosome': '16'
# }


def read_fasta(file_path):
    return clean_duplicates(
        fasta_sorter(
            fasta_parser(
                file_path
            )
        )
    )

# def table(result:list):
#     table = pd.DataFrame(
#         result
#     )
#     return table

# print(
#     clean_duplicates(
#         fasta_sorter(
#             fasta_parser(
#                 "../raw_data/H_sapiens_HbA1/gene.fna"
#             )
#         )
#     )
# )

# print(
#     table(
#         clean_duplicates(
#             fasta_sorter(
#                 fasta_parser(
#                     "../raw_data/H_sapiens_HbA1/gene.fna"
#                 )
#             )
#         )
        
#     )
# )

# print(fasta_sorter(fasta_parser("../raw_data/H_sapiens_HbA1/gene.fna")))

# print(fasta_parser("../raw_data/H_sapiens_HbA1/gene.fna"))