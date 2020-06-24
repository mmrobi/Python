# List introduction 2

#- Create a list ('`List A`') which contains the following values
#  ```text
#  Apple, Avocado, Blueberries, Durian, Lychee
#  ```
#- Create a new list ('`List B`') with the values of `List A`
#- Print out whether `List A` contains Durian or not
#- Remove Durian from `List B`
#- Add Kiwifruit to `List A` after the 4th element
#- Compare the size of `List A` and `List B`
#- Get the index of Avocado from `List A`
#- Get the index of Durian from `List B`
#- Add Passion Fruit and Pomelo to `List B` in a single statement
#- Print out the 3rd element from `List A`

list_a=['Apple', 'Avocado', 'Blueberries', 'Durian', 'Lychee']
list_b=['Apple', 'Avocado', 'Blueberries', 'Durian', 'Lychee']
print(list_b)

for x in list_a:
    if x== 'Durian':
        print(' yes, there is a "Durian"')

list_b[3:4]=[]
list_a.append('Kiwifruit')
print(list_a)

if len(list_a) > len(list_b):
    print("a=", len(list_a), ">", "b=", len(list_b))
elif len(list_a) < len(list_b):
    print("a=" ,len(list_a), "<","b=", len(list_b))
print(list_a.index('Avocado'))
for x in list_b:
    if x =='Durian':
        print(list_b.index('Durian'))
    else:
        print("Durian has been removed from this list")
        break
list_b[4:6]=['Passion Fruit', 'Pomelo']
print(list_b)

print(list_a[2])
