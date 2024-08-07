import os

def get_extension_type(fileTypes, fileNames, i):
    split = os.path.splitext(fileNames[i])  # split file extension
    path = os.getcwd() + "/" + fileNames[i]
    ext = split[1]

    if os.path.isdir(path):
        fileTypes[i] = "Directory"
    else:
        if ext == "":
            fileTypes[i] = "Unknown file"
        else:
            fileTypes[i] = ext.upper()[1:] + " file"
