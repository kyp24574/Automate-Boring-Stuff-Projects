# delete_unneeded_files.py - Finds exceptionally large files/folders and prints path.
import os

MAX_SIZE = 100000  # 100MB (Can be changed)

def delete_unneeded_files(directory):
    """Method to detect files and folders larger than MAX_SIZE"""
    # Creates absolute path of directory to search
    path = os.path.abspath(directory)
    # Walks through directory tree
    for folder_name, sub_folders, filenames in os.walk(path):
        # Prints out folder path if folder is greater than MAX_SIZE
        folder_size = os.path.getsize(folder_name)
        if folder_size > MAX_SIZE:
            # Can replace print statement with send2trash
            print(folder_name + '   Size: {}'.format(folder_size))
        # Prints out file path if file is greater than MAX_SIZE
        for file in filenames:
            file_path = os.path.join(folder_name, file)
            file_size = os.path.getsize(file_path)
            if file_size > MAX_SIZE:
                # Can replace print statement with send2trash
                print(file_path + '   Size: {}'.format(file_size))


def main():
    while True:
        user_path = input('Input directory path to search: ')
        if os.path.isdir(user_path):
            break
        print('Folder does not exist. Please try again.')
    delete_unneeded_files(user_path)


if __name__ == '__main__':
    main()
