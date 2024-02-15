"""
rename-files.py: A script that renames files within a given directory.

Version: 1.0
Author: Melissa Li
Email: melissa@makingtheimpact.com
License: GPL 2.0 or later
Credits: Thanks to Jane Doe for the math formula
Dependencies: os module
Requirements: Python 3.6 or higher
Date: 2024-02-13
History: 
    - 2024-02-13: Initial version

Notes: 
This script is designed to rename optimized image files, to trim unnecessary characters from the file name. 

To Do: 
Modify script to work with any file type (not just png files) and to support automatic renaming of files.

""" 

import os

def rename_files(directory):
    """
    Renames all the files inside the specified directory.
    
    Args: 
        directory (string): Path to the directory where the files to be renamed are located.
        
    Returns: 
        none
    """
    
    # Check if the directory exists
    if not os.path.isdir(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return
    
    # Flag to check if any PNG files are found
    found_png_files = False
    
    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            found_png_files = True
            # Split the filename on "0px" and take the first part, then add "0px.png" to it
            new_name = filename.split("0px")[0] + "0px.png"
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_name)
            try:
                os.rename(old_file, new_file)
                print(f'Renamed "{filename}" to "{new_name}"')
            except Exception as e:
                print(f"Error renaming file {filename}: {e}")
    # If no PNG files were found, inform the user
    if not found_png_files:
        print(f"No PNG files found in the directory '{directory}'.")

def main():
    """
    This function prompts the user for the root directory where the files are located, then asks for the child directory where the files are located. It calls the rename_files function, giving it the full directory path. 
    
    Args: 
        none
        
    Returns: 
        none
    """
    
    print('*** Image Rename Script ***')
    root_path = str(input('Root path where the directories are located: '))
    do_repeat = True
    while (do_repeat == True):
        folder = str(input('Directory Name: '))
        dir_path = os.path.join(root_path,folder)
        rename_files(dir_path)
        should_continue = str(input("Run again for a different directory? (Y/N) "))
        if should_continue == 'N' or should_continue == 'n':
            break

main()