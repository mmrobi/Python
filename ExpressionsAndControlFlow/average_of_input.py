# Write a program that asks for 5 integers in a row,
# then it should print the sum and the average of these numbers like:
#
# Sum: 22, Average: 4.4

x=int(input('Write a number from 1 to 25: '))
y=int(input('Write a number from 50 to 150: '))
z=int(input('Write a number from 600 to 1500: '))
w=int(input('Write a number from 2000 to 9999: '))
p=int(input('Write a number from 78 to 999: '))
S=x+y+z+w+p
A=S/5
print('Sum: ', S, 'Average: ', A)
      
