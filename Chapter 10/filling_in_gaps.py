# filling_in_gaps.py - A program to locate gaps in numbered files and rename them to close gap.
import shutil
import os
import re
import sys


def filling_in_gaps():
    """A program to rename numbered files in order."""
    # Ask user for directory with numbered files to fix.
    while True:
        directory = input('Input path to directory: ')
        if os.path.isdir(directory):
            path = os.path.abspath(directory)
            break
        print('Folder does not exist. Please try again.')

    # Prefix to search for
    prefix = input('Enter file prefix to check: ')
    # Regex to check file names
    file_number_regex = re.compile(r'({})((0*)?\d+)(\..*)'.format(prefix))

    # Lists to store file numbers and extension (assuming all file extensions are the same).
    file_number = []
    extension = ''
    found = False

    # Find files in folder that match the prefix given by user.
    for folder_name, sub_folders, filenames in os.walk(path):
        for file in filenames:
            # Search file name
            match = file_number_regex.search(file)
            if match is not None:
                found = True
                # Add file number to list and set extension
                file_number.append(match.group(2))
                extension = match.group(4)

    # If there are no matches found in the directory
    if not found:
        print('No matching files found. The program will now exit...')
        sys.exit()

    # Sort file number lists; this assumes file extensions are all the same.
    file_number.sort(key= lambda num: len(num))  # Sorted by length of file number string i.e. '001' '0011'
    ordered_file_number = sorted([int(num) for num in file_number])

    # Loop through a number list to rename files.
    for number in range(1, len(file_number)+1):
        # Calculate leading zeroes for file name string.
        leading_zeroes = '0' * (len(file_number[number-1]) - len(str(ordered_file_number[number-1])))
        # Current file name
        current_file = '{}/{}{}{}{}'.format(path, prefix, leading_zeroes, number, extension)
        # If current file does not exist, rename file sequentially.
        if not os.path.exists(current_file):
            next_number = ordered_file_number[number-1]  # Next number in list
            next_zeroes = '0' * (len(file_number[number-1]) - len(str(next_number)))  # Leading zeroes for next number
            # File name of next file in sequential order.
            next_file = ('{}/{}{}{}{}'.format(path, prefix, next_zeroes, next_number, extension))
            # Rename current file to next file in sequential order.
            shutil.move(next_file, current_file)


def main():
    """Main method to test/run filling_in_gaps()"""
    filling_in_gaps()


# If program is run (and not imported), calls main() method.
if __name__ == '__main__':
    main()
