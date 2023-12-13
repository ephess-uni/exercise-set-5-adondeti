"""ex_5_0.py"""


def line_count(infile):
    # Read the file
    with open(infile, 'r') as file:
        # Count the number of lines 
        lines = file.readlines()
        # get the length
        lines_count = len(lines)
    # Print the lines count
    print(lines_count)


        


if __name__ == "__main__":
    # get the utility function for path discovery
    try:
        from src.util import get_repository_root
    except ImportError:
        from util import get_repository_root

    # Test line_count with a file from the data directory
    data_directory = get_repository_root() / "data"
    line_count(data_directory / "ex_5_2-data.csv")
