# List all files in the data directory

import os

# List all files in the data directory
def list_files():
    files = os.listdir("data")
    return files


# Read first line of all files
def read_first_line(files):
    for file in files:
        with open("data/" + file) as f:
            line = f.readline()
            try:
                n, _, _ = map(int, line.split())
                if n >= 500:
                    print(file)
            except:
                pass

read_first_line(list_files())
