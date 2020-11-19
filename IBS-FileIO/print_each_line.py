# Write a program that opens a file called "my-file.txt", then prints
# each line from the file.
# If the program is unable to read the file (for example it does not exist),
# then it should print the following error message: "Unable to read file: my-file.txt"

try:
    my_file= open("my_file.txt","r")
    print(my_file.readlines())
    my_file.close()
except NameError:
    print("Unable to read file: my_file.txt")