# - Create a function called `factorio`
#   that returns it's input's factorial
n= int(input("Write a number: "))

def factorio(n):
    fact= 0
    for x in range(n+1):
        fact += x
    return fact

print(factorio(n))
