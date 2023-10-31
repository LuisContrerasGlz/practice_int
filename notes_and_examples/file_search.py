# Python program that performs a file search operation within a specified directory and its subdirectories using the os module

import os

def search_files(directory, file_extension):
    found_files = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(file_extension):
                found_files.append(os.path.join(dirpath, filename))
    return found_files

# Set the directory to search and the file extension to look for
directory_to_search = '/path/to/directory'  # Replace with the directory you want to search
file_extension_to_find = '.txt'  # Replace with the file extension you want to search for

# Search for files with the specified extension in the given directory
result = search_files(directory_to_search, file_extension_to_find)

if result:
    print(f"Found {len(result)} files with the extension '{file_extension_to_find}':")
    for file_path in result:
        print(file_path)
else:
    print(f"No files found with the extension '{file_extension_to_find}' in the directory.")

"""

This script uses the os.walk() function to traverse through the directory and its subdirectories, 
searching for files with the specified file extension. 
It then displays the paths of the found files.

"""
