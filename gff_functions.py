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






###------ function to read gff file

#def read_gff as gff:



###------ function to rwrite output file

#def write_output as out:






#set the enviroment for this script 
# is it the main(), 
if __name__ == '__main__':
    main()