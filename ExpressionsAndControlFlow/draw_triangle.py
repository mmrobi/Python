# Write a program that reads a number from the standard input, then draws a
# triangle like this:
#
# *
# **
# ***
# ****
#
# The triangle should have as many lines as the number was


x=int(input("Write a number: "))

for x in range(1, (x+1), 1):
    for y in range(1, (x+1), 1):
        print("*", end="")
    print()
