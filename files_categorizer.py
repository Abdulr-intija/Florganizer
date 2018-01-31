import os
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('--dir_path', type=str, help='Path to the directory whose files should be categorized')
args = arg_parser.parse_args()

# some check ups before using specified path
assert (args.dir_path is not None), "You have to input a valid path to a directory first by setting --dir_path"
assert (len(os.listdir(args.dir_path)) != 0), "No files to categorize here. Must be a dir with FiLEs"

print("\nCategorizing... chill for some millisecs\n")

# get the extension of a file
def getExtension(file_name):
    dot_split = file_name.split('.')
    return dot_split[len(dot_split) - 1]

# move to specified directory
os.chdir(args.dir_path)

# check if a file has extension
def hasExtension(file_name):
    return len(file_name.split('.')) > 1


for current_file in os.listdir(args.dir_path):
    if hasExtension(current_file):
        new_dir = getExtension(current_file) + " files/"

        if not os.path.exists(new_dir):
            os.mkdir(new_dir)
        os.rename(current_file, new_dir + current_file)

print("Files categorized!")