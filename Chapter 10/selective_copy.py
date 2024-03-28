# selective_copy.py - copies files with certain extensions to a new destination.
import shutil
import os

def selective_copy():
    """Method to selectively copy files with a certain extension from one directory to another."""
    # Asks for user input for starting folder, destination folder, and file extension.
    while True:
        directory = input('Input path to directory: ')  # starting folder
        destination = input('Input path to destination: ')  # destination folder
        extension = input('Input file extension to copy: ')  # file extension
        # Checks if both starting and destination folders exists
        if os.path.isdir(directory) and os.path.isdir(destination):
            # Confirms destination folder
            response = input('Confirm destination?')
            if response.lower().startswith('y'):
                break
        # Checks if starting folder exists.
        elif not os.path.isdir(directory):
            print('Path to directory does not exist. Please try again.')
            continue
        # Checks if destination folder does not exist.
        elif not os.path.isdir(destination):
            # Asks user if they wish to create this folder.
            response = input('This destination does not exist. Would you like to create this folder?: ')
            if response.lower().startswith('y'):
                os.makedirs(destination)
                break

    # Creates absolute paths for path(starting folder) and destination folder
    path = os.path.abspath(directory)
    destination = os.path.abspath(destination)
    # Walks through directory and finds files with matching extensions
    for foldername, subfolders, filenames in os.walk(path):
        for filename in filenames:
            # If file with extension is found
            if filename.endswith(extension):
                # Copies from starting folder to destination
                shutil.copy(os.path.join(foldername, filename), destination)
                print(f'Copied {filename} to {destination}.')

    # Notifies user that process is complete.
    print('Copying complete.')


def main():
    """Main Method to test/run selective_copy()"""
    selective_copy()

# If program is run (and not imported), calls main() method.
if __name__ == '__main__':
    main()
