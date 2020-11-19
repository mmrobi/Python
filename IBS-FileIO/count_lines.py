import sys
try:
    my_file= open("my_file.txt","r")
    count_lines= my_file.readlines()
    number_lines=len(count_lines)
    print(number_lines)
except NameError:
    print("0")


