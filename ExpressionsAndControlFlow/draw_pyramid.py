# Write a program that reads a number from the standard input, then draws a
# pyramid like this:
#
#
#    *
#   ***
#  *****
# *******
#
# The pyramid should have as many lines as the number was

x=int(input("Write a number: "))

for s in range(0,x):
    for d in range(0,x-s-1):
        print(end=" ")
    for d in range(0,2*s+1):
        print("*",end="")
    print()



