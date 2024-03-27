"""File Search - A program to search through .txt files in a directory using regex."""
from pathlib import Path
import re

def main():
    # Ask the user for phrase/regular expression they would like to find
    user_input = input('Enter what you would like to find: ')
    user_regex = re.compile(user_input)
    # Ask the user for a valid path to search
    while True:
        user_path = input('Enter a path to search: ')
        curr_folder = Path(user_path)
        if curr_folder.is_dir():
            break
        else:
            print('Path not found. Please try again.')

    # List of .txt files in that directory
    txt_files = list(curr_folder.glob('*.txt'))
    found = False
    # Searches each .txt file for pattern/phrase
    for file_path in txt_files:
        with open(file_path, 'r') as file:
            text = file.read()
            match = re.findall(user_regex, text)
            # If found, prints to the terminal
            if match:
                found = True
                for m in match:
                    print(m)

    # If not found, notifies the user that no matches were found
    if not found:
        print('No matches found.')


if __name__ == "__main__":
    main()
