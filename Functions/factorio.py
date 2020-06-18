# - Create a function called `factorio`
#   that returns it's input's factorial
n= int(input("Write a number: "))

def factorio(n):
    factorial=1
    for x in range(1,n+1):
        factorial *= x
    return factorial

print(factorio(n))
