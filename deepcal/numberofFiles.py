import os

folder_path = r'C:\Users\Mark\Desktop\CAL\deepcal\ImageSeq\ImageSeq'  # Replace with the actual folder path

# List all files in the folder
files = os.listdir(folder_path)

# Count the number of files
num_files = len(files)

print("Number of files:", num_files)
