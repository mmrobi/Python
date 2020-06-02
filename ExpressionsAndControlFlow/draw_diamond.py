# Write a program that reads a number from the standard input, then draws a
# diamond like this:
#
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#
# The diamond should have as many lines as the number was

num=int(input("Write a number: "))

for x in range(0,num//2+1):
    for y in range(0, (num//2+1)-x-1):
        print(end=" ")
    for y in range (0, x*2+1):
        print("*",end= "")
    print()
for x in range(0, num-(num//2+1)):
    for z in range(0,num-x-1):
        print(end=" ")
    for z in range(0,num):
        print("*", end="")
    print()
    
