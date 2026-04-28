#!/usr/bin/env python3


###------ function to read FASTA file


def read_fasta(fasta_file):

    # open fasta file
    with open(fasta_file, "r") as fasta:

        # skip header line
        header = next(fasta)

        # create empty string to store DNA
        genome_sequence = ""

        # read file line by line
        for line in fasta:

            # remove newline "/"
            line = line.strip()

            # add line to genome sequence
            genome_sequence += line

    # return full DNA sequence
    return genome_sequence


###------ function to read GFF file
def read_gff(gff_file, genome_sequence):

    # create list to store results (id, sequence)
    features = []

  # open gff file
with open(gff_file, "r") as gff:
    
    # read file line by line
    for line in gff:

        # remove newline
        line = line.strip()

        # ignore empty lines
        if not line or line.startswith("#"):
            continue

        # split line into columns (tab-separated)
        columns = line.split("\t")

        if len(columns) < 9:
            continue

        # get start (col 4) and end (col 5)
        start = int(columns[3])
        end = int(columns[4])

        # extract DNA sequence (python is 0-based)
        sequence = genome_sequence[start-1:end]

        # get last column (info column)
        info = columns[8]

            # extract ID after "ID="
            seq_id = info.split("ID=")[1]

            # remove anything after ;
            seq_id = seq_id.split(";")[0]

            # remove anything after :
            seq_id = seq_id.split(":")[0]

            # store result
            features.append((seq_id, sequence))

    # return all features
    return features



###------ function to rwrite output file

def write_output(features):

    # open output file
    with open("covid_genes.fasta", "w") as out:

        # loop through each feature
        for seq_id, sequence in features:

            # write header
            out.write(">" + seq_id + "\n")

            # write sequence
            out.write(sequence + "\n")


###------define the main function
def main():

    # read the fasta file
    genome = read_fasta("fasta")

    # read the gff file
    features = read_gff("gff3", genome)

    # write the output
    write_output(features)

    # confirm output is done
    print("Output written")


# set the environment for this script
if __name__ == "__main__":
    main()