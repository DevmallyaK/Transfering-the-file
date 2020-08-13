# Import the required libraries
import os
import shutil

# Create and pint the path where you have the file stored to transfer
path = "D:/Python practice/Transfering file using python/Test_folder_1"
print(os.listdir(path))

# Put that file into the source variable
source = "D:/Python practice/Transfering file using python/Test_folder_1"

# Create a destination path where the file is suppose to move
destination = "D:/Python practice/Transfering file using python/Test_folder_2"

files = os.listdir(source)

# Move the content from Source to Destination
for f in source:
    shutil.move(source+f, destination)
