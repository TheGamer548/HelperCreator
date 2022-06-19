import os

__version__ = "0.0.1"

def create_html_documentation_file(path_directory, file_name):
    # Creating a file at specified folder
    # join directory and file path
    with open(os.path.join(path_directory, file_name), 'w') as fp:
        # uncomment below line if you want to create an empty file
        fp.write('<!DOCTYPE html><html><head><title></title></head><body></body></html>')

def create_documentation_file(path_directory, file_name):
    # Creating a file at specified folder
    # join directory and file path
    with open(os.path.join(path_directory, file_name), 'w') as fp:
        # uncomment below line if you want to create an empty file
        fp.write('You can replace this text and write your documentation')

def help():
    Help = {"Read markdown file"}

def end():
    print("End of programm")