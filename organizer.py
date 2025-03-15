import shutil
import os

directory = os.path.join(os.path.expanduser('~'), 'Documents') # change this to the directory you want to organize

extensions ={
    ".pdf": "PDF",
    ".doc": "Documents",
    ".docx": "Documents",
    ".ppt": "Presentations",
    ".pptx": "Presentations",
    ".xls": "Spreadsheets",
    ".xlsx": "Spreadsheets",
    ".zip": "Compressed",
    ".rar": "Compressed",
    ".tar": "Compressed",
    ".gz": "Compressed",
    ".txt": "Text",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".mp4": "Videos",
    ".mov": "Videos",
    ".mkv": "Videos",
    ".mp3": "Music",
    ".wav": "Music",
    ".flac": "Music",
    ".wma": "Music"
}

for filename in os.listdir(directory): # Loop through all the files in the directory
    file_path = os.path.join(directory, filename)

    if os.path.isfile(file_path): # Check if the file is a file
        extension = os.path.splitext(filename)[1].lower() 

        if extension in extensions: # Check if the file extension is in the extensions dictionary
            folder_name = extensions[extension] 

            folder_path = os.path.join(directory, folder_name) # Create the folder path
            os.makedirs(folder_path, exist_ok=True)

            destination = os.path.join(folder_path, filename) # Create the destination path
            shutil.move(file_path, destination)
            print(f"Moved {filename} to {folder_name}") 
        else:
            print(f"Unknown file type: Skipping {filename} ...")
    else:
        print(f"Skipping {filename} as it is a directory ...")

print("Organizing files completed!")
