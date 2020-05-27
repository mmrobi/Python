# Write a program that asks for two numbers
# The first number represents the number of girls that comes to a party, the
# second the boys
# It should print: The party is exellent!
# If the the number of girls and boys are equal and there are more people coming than 20
#
# It should print: Quite cool party!
# It there are more than 20 people coming but the girl - boy ratio is not 1-1
#
# It should print: Average party...
# If there are less people coming than 20
#
# It should print: Sausage party
# If no girls are coming, regardless the count of the people

x=int(input('How many girls are coming? '))
y=int(input('How many boys are coming? '))
Equal=x==y
NotEQ=x>y or y>x

if Equal and x+y>20:
    print('The party is exellent!')
elif x+y>20 and NotEQ and x>0:
    print('Quite cool party!')
elif x+y<20 and x>0:
    print('Average party...')
elif x==0 and y>1:
    print('Sausage party ')
    
