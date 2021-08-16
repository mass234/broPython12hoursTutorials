import os

# path = "C:\\Users\\touch\\OneDrive\\바탕 화면\\test.txt"
path = "C:\\Users\\touch\\OneDrive\\바탕 화면\\Folder"


if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")

else:
    print("That location doesn't exist")