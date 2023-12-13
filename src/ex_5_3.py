""" ex_5_3.py
This module contains an entry point that:

- creates a CLi that accepts an input file of data to be processed
- shifts and scales the data to a mean of 0 and a standard deviation 1
- writes the file to the output file argument
"""
import numpy as np
from argparse import ArgumentParser
import argparse

if __name__ == "__main__":
    # Create your argument parser object here.
    # Collect the filename arguments from the command line
    # Rewrite your 5_3 logic here so that it utilizes the arguments passed from the command line.

    # Tests will run your command using a system call.
    # To test your program with arguments, run it from the command line
    # (see README.md for more details)

    # description 
    desc = "This program applies a standard scale transform to the data in infile and writes it to outfile."
    # instance of the parser 
    parser = ArgumentParser(description = desc)
    # add the argument 
    parser.add_argument("infile")
    parser.add_argument("outfile")
    # pass the args
    args = parser.parse_args()
    # load the data 
    data = np.loadtxt(args.infile)
    # get the mean 
    data_mean = data - np.mean(data)
    # Standardize the data
    data_std = data_mean / np.std(data_mean)
    # save the data to the output file 
    np.savetxt(args.outfile, data_std, fmt = "%.2e")

    

    
