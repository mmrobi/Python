#Given a non-negative integer n, return the sum of its digits recursively (without loops).
#Hint (don't read this if you'd like to have a challenge)

#Mod (%) by 10 yields the rightmost digit (e.g. 126 % 10 is 6)
#C++, C#, Python

#Divide (/) by 10 removes the rightmost digit (e.g. 126 / 10 is 12).

def addToList(listcontainer):
	listcontainer += [10]

mylistContainer = [10, 20, 30, 40]
addToList(mylistContainer)
print(len(mylistContainer))
