# Shopping list

#We are going to represent a shopping list in a list containing strings.

#- Create a list with the following items.
#  - Eggs, milk, fish, apples, bread and chicken
#- Create an application which solves the following problems.
#  - Do we have milk on the list?
#  - Do we have bananas on the list?

shop=["Eggs", "milk", "fish", "apples", "bread", "chicken"]

def check(shop):
    if "milk" in shop:
       print("Yes, we have milk")
    else:
        print("No, we do not have milk")
    if "bananas" in shop:
        print("Yup, we have bananas")
    else:
        print("Nop, we don't have bananas")
    
        

      

print(check(shop))
