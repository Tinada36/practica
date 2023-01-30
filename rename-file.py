import os

def rename_files(directory, pattern, kolvo):
    for i in range(kolvo):
        file_path = os.path.join(directory, os.listdir(directory)[i])
        print(file_path)
        if os.path.isfile(file_path):
            new_filename = pattern.format(os.listdir(directory)[i])
            new_file_path = os.path.join(directory, new_filename)
            os.rename(file_path, new_file_path)


kolvo = int(input("How many files do you want to rename?: "))
directory = input("Enter the directory path: ")
pattern = input("Enter the file renaming pattern (e.g. '{}_new'): ")
rename_files(directory, pattern, kolvo)