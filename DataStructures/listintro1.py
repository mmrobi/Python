#We are going to play with lists. Feel free to use the built-in methods where
#possible.

#- Create an empty list which will contain names (strings)
#- Print out the number of elements in the list
#- Add William to the list
#- Print out whether the list is empty or not
#- Add John to the list
#- Add Amanda to the list
#- Print out the number of elements in the list
#- Print out the 3rd element
#- Iterate through the list and print out each name
# ```text
#William
#John
#Amanda
#  ```
#- Iterate through the list and print
#  ```text
#  1. William
#  2. John
#  3. Amanda
#  ```
#- Remove the 2nd element
#- Iterate through the list in a reversed order and print out each name
#  ```text
#  Amanda
#  William
#  ```
#- Remove all elements

listintro=[]
print(len(listintro))
listintro.append("William")
print(listintro)

if len(listintro) == 0:
    print("empty")
else:
    print("not empty")
    
listintro.append("John")
listintro.append("Amanda")
print(len(listintro))
print(listintro[2])
for x in listintro:
    print(x)
listintro[1:2]=[]
for y in  reversed(listintro):
    print(y)

listintro[:]=[]
