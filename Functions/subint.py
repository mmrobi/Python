#  Create a function that takes a number and a list of numbers as a parameter
#  Returns the indeces of the numbers in the list where the first number is part of
#  Or returns an empty list if the number is not part of any of the numbers in the list

# Example

# should print: `[0, 1, 4]`

# should print: '[]'

def subint(number, lista):
    result=[]
    counter=0
    for x in lista:
        if  str(number) in str(x):
            result.append(counter)
        counter += 1
    return result



print(subint(9, [1, 11, 34, 52, 61]))
print(subint(1, [1, 11, 34, 52, 61]))
