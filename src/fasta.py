 #  A local file containing functions to parse fasta files into dict.

# Totally inefficient and would not recommend.
# Better to use a library like Biopython.
# But I am trying to learn to work with python and fasta files.
# So doing it this way helps.

from re import findall

# Some fasta files, like some of the ones I have chosen, have multiple records
# within them. So, you can't just do "".join(open(file,"r").readlines()[1:])

# Define a function with a string parameter. The paramereter in this case will
# always be the path to the file. For example, for the human HbA1 coding sequence
# the path will be "H_sapiens_HbA1/cds.fna".
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

    # The information should be organised into a dict, so assign an empty dict to the 
    # variable "organised"
    organised = dict()

    # Iterate through each record in records
    for record in records:

        # Information within each record will be put into a dict.
        accession = dict()

        # Preserve the headline of the record as is, just to ensure no loss of data.
        accession["headline"] = record[0]

        # There are a few metadata within the headline organised into [key=value] format
        # so assign them as "key : value" within the dict using the findall function.
        for key, value in findall(r"\[(.*?)=(.*?)\]", record[0]):
            accession[key] = value

        # Isolate the gene name and the accession from the headline
        x = record[0].split("[")[0].split()
        accession["gene"] = x[1]

        # Merge the sequence lines together to produce a single string containing the entire
        # sequence and assign it to the key "sequence" within the accession dict.
        accession["sequence"] = "".join(record[1:]).replace("\n", "")

        # Insert the accession dict containing all the info from the record into the organised
        # variable as a nested dict.
        organised[x[0][1:]] = accession
    return organised

# print(fasta_sorter(fasta_parser("../H_sapiens_HbA1/gene.fna")))

# print(fasta_parser("../H_sapiens_HbA1/gene.fna"))