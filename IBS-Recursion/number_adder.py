#Write a recursive function that takes one parameter: n and adds numbers from 1 to n.

def num_adder(n):
    added= 1
    if n == 1:
        return 1
    else:
        return n + num_adder(n-1)


print(num_adder(5))
