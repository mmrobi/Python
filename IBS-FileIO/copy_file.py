# Write a function that copies the contents of a file into another
# It should take the filenames as parameters
# It should return a boolean that shows if the copy was successful


def copy_file(path1, path2):
    fileread = open(path1, "r")
    copied = fileread.read()
    filewrite = open(path2, "w")
    copypaste = filewrite.write(copied)
    checkfile1 = open(path1, "r")
    checked1 = checkfile1.read()
    checkfile2 = open(path2, "r")
    checked2 = checkfile2.read()
    if checked1 == checked2:
        print(True)
    else:
        print(False)


copy_file("myfile2.txt", "copied.txt")
