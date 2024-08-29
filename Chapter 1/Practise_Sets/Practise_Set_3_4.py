import os

# Specify the directory path
path = '/'

# List all entries in the specified directory
entries = os.listdir(path)

# Print each entry
for entry in entries:
    print(entry)
