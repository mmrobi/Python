# Write a function called `sum` that returns the sum of numbers from zero to the given parameter
x=int(input("Write a number: "))

def Sum(x):
    sum_ = 0
    for y in range(x):
        sum_ += y
    return sum_

print(Sum(x))


