a = 3
a += 10
# make the "a" variable's value bigger by 10

print(a)

b = 100
b -= 7
# make b smaller by 7

print(b)

c = 44
c *= 2
# please double c's value

print(c)

d = 125
d /= 5
# please divide by 5 d's value

print(d)

e = 8
e **= 3
# please cube of e's value

print(e)

f1 = 123
f2 = 345
if f1 < f2:
    print('Is 123>345?  :' ,False)
# tell if f1 is bigger than f2 (pras a boolean)

g1 = 350
g2 = 200
if 2*g2 > g1:
    print('Yes, the double of 200 is bigger,than 350')
# tell if the double of g2 is bigger than g1 (pras a boolean)

h = 1357988018575474
h %= 11
if h is 0:
     print('Yes, 11 is a divisor of h')
    
# tell if 11 is a divisor of h (pras a boolean)

i1 = 10
i2 = 3
# tell if i1 is higher than i2 squared and smaller than i2 cubed (pras a boolean)
if 10 > i2*2 and 10< i2**3:
    print('Yes , 9<10<27')
divs = [3, 5]
j = 1521
j %= 3
if j is 0:
    print('yes, it is divisible by 3')

j1 = 1521
j1 %= 5
if j1 is 0:
    print('yes it is divisible by 5')
else:
    print(' no it is not divisible by 5')



# tell if j is divisible by 3 or 5 (pras a boolean)
