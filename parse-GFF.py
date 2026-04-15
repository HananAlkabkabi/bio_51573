#!/usr/bin/env python3
import argparse

#import gff_funcations.py    #call modual 

#--------funcation to parse the command-line  
def get_args():

    parser = argparse.ArgumentParser(description="This script to run fasta file and GFF file")

     #add a positional argument, fasta file
    parser.add_argument("Fasta file", help="use input fast file", type=str)

    #add a positional argument, GFF file
    parser.add_argument("GFF file", help="use input fast file", type=str)


    # parse the arguments and return in two steps
    args = parser.parse_args()
    return args

def main():
      print("script works!")

# execute the program by calling main
if __name__ == "__main__":
	main()
      