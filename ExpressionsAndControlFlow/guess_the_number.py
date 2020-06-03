# Write a program that stores a number, and the user has to figure it out.
# The user can input guesses, after each guess the program would tell one
# of the following:
#
# The stored number is higher
# The stried number is lower
# You found the number: 8
import random
Num=random.randrange(1,100,1)

x=int(input("Guess the number: "))

while x>Num:
    print("The stored number is lower  \n")
    x=int(input("Guess the number: "))
    while x<Num:
        print("The stored number is higher \n")
        x=int(input("Guess the number: "))
if x==Num:
    print("You found the number: " , Num)

