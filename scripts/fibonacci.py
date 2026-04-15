#!/usr/bin/env python3

import argparse

#--------funcation to parse the command-line  
def get_args():
    ###------------- accept and parse command line arguments
    # create an argument parser object
    parser = argparse.ArgumentParser(description="This script calculates the number at a given position \
                                    in the Fibonacci sequence")

    # add a positional argument, in this case, the position in the Fibonacci sequence
    parser.add_argument("position", help="Position in the Fibonacci sequence", type=int)

    # an optional argument for verbose output or not
    # if 'store_true', this means assign 'True' if the optional argument is specified
    # on the command line, so the default for 'store_true' is actually false
    parser.add_argument("-v", "--verbose", help="Print verbose output", action='store_true')

    # parse the arguments and return in two steps
    args = parser.parse_args()
    return args

# or, parse argument and return in one step 
    #return parser.parse_args()

##------funcation to 
def fin():
    # initialize two integers
    a,b = 0,1

    for i in range(int(beyonce.position)):
        a,b = b,a+b

    fibonacci_number = a
    return fibonacci_number


#------ funcation to print the output 
def print_output(output): #we can calle fibnum or any thing its verible
    if args.verbose:
        print(f"The Fibonacci number for {beyonce.position} is {output}.")
    else:
        print(output)

#------ define the main fucntion
def main():
    fibnum=()
    print_output(fibnum)
#this print statment will not print 





#------ calling get.args() happend out her its on 
beyonce = get_args():

    #set the enviroment for this script
    # is thus nain (i.e, a standalon Python script), or 
    # is this a Python modual being called by another script 
    if __name__ == " __main__":
        main()
