# A local file containing functions to parse fasta files into dict.

# Totally inefficient and would not recommend.
# Better to use a library like Biopython.
# But I am trying to learn to work with python and fasta files.
# So doing it this way helps.

# Some fasta files, like some of the ones I have chosen, have multiple sequences
# within them. So, you can't just do "".join(open(file,"r").readlines()[1:])

# Define a function with a string parameter. The paramereter in this case will
# always be the path to the file. For example, for the human HbA1 coding sequence
# the path will be "H_sapiens_HbA1/cds.fna".
def fasta(file_location:str):

    # Variable x records the locations of list objects that starts with ">"
    x = list()
    # An 
    sequences = list()
    with open(file_location, "r") as file:
        data = file.readlines()
        for i in range(len(data)):
            if data[i].startswith(">"):
                x.append(i)
        x.append(len(data))
        sequences = [data[x[i]:x[i+1]] for i in range(len(x)-1)]
    return sequences

print(fasta("H_sapiens_HbA1/gene.fna"))