# Create a function that takes a number,
# divides ten with it,
# and prints the result.
# It should print "fail" if the parameter is 0

while True:
    try:
        number = int(input("Write a number:"))
        print(10 / number)
        break
    except ZeroDivisionError:
        print("Fail")