# A local file containing functions to parse fasta files into dict.

# Totally inefficient and would not recommend.
# Better to use a library like Biopython.
# But I am trying to learn to work with python and fasta files.
# So doing it this way helps.

# Some fasta files, like some of the ones I have chosen, have multiple records
# within them. So, you can't just do "".join(open(file,"r").readlines()[1:])

# Define a function with a string parameter. The paramereter in this case will
# always be the path to the file. For example, for the human HbA1 coding sequence
# the path will be "H_sapiens_HbA1/cds.fna".
def fasta(file_location:str):

    # Variable x records the locations of where the objects with the headerlines(">")
    # thereby detecting where one record starts and, potentially, where one record ends.
    x = list()
    # An empty list variable that will later contain all the records spliced from the
    # fasta file as a nested list.
    sequences = list()

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
        sequences = [data[x[i]:x[i+1]] for i in range(len(x)-1)]
    
    # Return the sequences variable, which is a nested list of records from the fasta
    # file.
    return sequences

print(fasta("H_sapiens_HbA1/gene.fna"))