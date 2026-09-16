# A local file containing functions to parse fasta files into dict

def fasta(file_location:str):
    data = open(file_location, "r").readlines()
    x = list()
    info = list()
    data_sorted = list()
    for i in range(len(data)):
        if ">" in data[i]:
            x.append(i)
            info.append(data[i])
        else:
            data_sorted.append(data[i])
    x.append(len(data))
    sequences = [data[x[i]:x[i+1]] for i in range(len(x)-1)]
    return sequences[0]

print(fasta("H_sapiens_HbA1/gene.fna"))