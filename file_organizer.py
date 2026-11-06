import os

audio = [".mp3"]
video = [".mp4",".m4a"]
image = [".pdf",".jpg","jpeg"]
docs = [".pdf",".doc",".xlsx"]
zips = [".zip"]

path = "C:\\Users\\kaiqu\\OneDrive\\Documents"
path2 = "C:\\Users\\kaiqu\\OneDrive\\Documents\\documents_fixed"

###getting file neme (test only)
# for file in files:
#     print(f"{file}\n")

#making folders

file_types = {
    "audio": [".mp3"],
    "video": [".mp4", ".m4a"],
    "image": [".pdf", ".jpg", "jpeg"],
    "docs": [".pdf", ".doc", ".xlsx"],
    "zips": [".zip"],
    "extras": []
}

for folder in file_types:
    full_path = os.path.join(path2, folder)
    
    try:
        os.mkdir(full_path)
        print(f"Folder '{folder}' Created!")
    except FileExistsError:
        print(f"Folder '{folder}' Already Exists!")

###getting file extention (test only)

# files = os.listdir(path)

# for file in files:
#     extention = os.path.splitext(file)[1]
#     print(extention)

import shutil as shtl

# Function to move files

def move_file(file, current_path):

    extension = os.path.splitext(file)[1].lower()

    category = "extras"

    for folder, extensions in file_types.items():
        if extension in extensions:
            category = folder
            break

    relative_path = os.path.relpath(current_path, path)

    destination = os.path.join(path2, category, relative_path)

    os.makedirs(destination, exist_ok=True)

    shtl.move(
        os.path.join(current_path, file),
        os.path.join(destination, file)
    )


# Function to find files

def find_files(path):

    files = os.listdir(path)

    for file in files:

        deep_file = os.path.join(path, file)

        if os.path.isdir(deep_file):
            find_files(deep_file)

        else:
            move_file(file, path)

#deleting empty folders

def delete_empty_folders(path):

    for folder in os.listdir(path):

        full_path = os.path.join(path, folder)

        if os.path.isdir(full_path):

            delete_empty_folders(full_path)

            if not os.listdir(full_path):
                os.rmdir(full_path)
                print(f"Deleted empty folder: {folder}")

#calling functions

find_files(path)
delete_empty_folders(path)

#user UI

from time import sleep

print("\nMoving Files...")
sleep(2)
print("\nFiles Organized!")

f_count = 0

print("\nCurrent number of files in each folder:")

for folder in file_types:

    f_count = 0

    for file in os.listdir(os.path.join(path2, folder)):
        f_count += 1

    print(f"{folder}: {f_count} files")
