"""ex_5_1.py"""
try:
    from src.ex_5_0 import line_count
except ImportError:
    from ex_5_0 import line_count
    
import argparse

def main(infile):
    """Call line_count with the infile argument."""
    line_count(infile)


if __name__ == "__main__":
    # Create your argument parser object here.
    # Collect the filename argument from the command line
    # pass this argument to the main function above
    # Tests will run your command using a system call.
    # To test your program with arguments, run it from the command line
    # (see README.md for more details)

    
    # Defining the description
    desc = "This program prints the number of lines in infile."
    # create an instance of argparse
    parser = argparse.ArgumentParser(description = desc)
    # add the infile file
    parser.add_argument("infile")
    # parse the args
    args = parser.parse_args()
    # get the line counts
    line_count(args.infile)

    





    

    
