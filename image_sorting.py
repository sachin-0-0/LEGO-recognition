import os
import re
import shutil

# specify your folder path here
folder_path = "/path/to/your/folder"

# specify your new folder path here
new_folder_path = "/path/to/new/folder"

# list all files in the directory
all_files = os.listdir(folder_path)

# create a regex pattern to match files that contain only digits before the dot and have .stl extension
pattern = r"^\d+\.stl$"

# filter out the files which satisfy the regex pattern
filtered_files = [f for f in all_files if re.match(pattern, f)]

# create new folder if it doesn't exist
if not os.path.exists(new_folder_path):
    os.makedirs(new_folder_path)

# move the filtered files to the new folder
for file in filtered_files:
    # create source file path
    source = os.path.join(folder_path, file)
    
    # create destination file path
    destination = os.path.join(new_folder_path, file)
    
    # move the file
    shutil.move(source, destination)

print("Moved all filtered .stl files to the new folder.")
