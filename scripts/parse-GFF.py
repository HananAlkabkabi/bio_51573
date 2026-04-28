#!/usr/bin/env python3
import argparse


import gff_functions   #call modual 

###------ uncation to parse the command-line  
def get_args():

    parser = argparse.ArgumentParser(description="This script to run fasta file and GFF file")

###------ dd a positional argument, fasta file
    parser.add_argument("fasta_file", help="use input fast file", type=str)

###------ add a positional argument, GFF file
    parser.add_argument("gff_file", help="use input gff file", type=str)


###------ parse the arguments and return in two steps
    args = parser.parse_args()
    return args
###------ define the main() function

def main():
    #read fasta file to get genome seq

    genome_sequence = gff_functions.read_fasta(args.fasta_file)

    # read gff file  (id + sequence)
    features = gff_functions.read_gff(args.gff_file, genome_sequence)

    # write output file

    gff_functions.write_output(features)

    # confirm that script finished
    print("Output written")
    
###------ calling get_args()
args = get_args()

# execute the program by calling main
if __name__ == "__main__":
	main()
      