# Product database

#We are going to represent our products in a map where the keys are strings
#representing the product's name and the values are numbers representing the
#product's price.

#- Create a map with the following key-value pairs.

#  | Product name (key) | Price (value) |
#  | :----------------- | :------------ |
#  | Eggs               | 200           |
#  | Milk               | 200           |
#  | Fish               | 400           |
#  | Apples             | 150           |
#  | Bread              | 50            |
#  | Chicken            | 550           |

#- Create an application which solves the following problems.
#  - [How much is the fish?](https://www.youtube.com/watch?v=cbB3iGRHtqA)
#  - What is the most expensive product?
#  - What is the average price?
#  - How many products' price is below 300?
#  - Is there anything we can buy for exactly 125?
#  - What is the cheapest product?

products={"Eggs":200, "Milk":200, "Fish":400, "Apples":150, "Bread":50, "Chicken":550}

def check_stuff(products):
    print(products["Fish"])
    value=[]
    for x in products.values():
        value.append(x)
    print(sum(value)/len(value), "is the average")
    budget = []
    for y,z in products.items():
        if z < 300:
            budget.append(y)
    print("There are", len(budget), "products cheaper than 300: ", budget)
    for x,y in products.items():
        if y==125:
            print("We can buy : ", x, "for 125")
    expensive=0
    for k,v in products.items():
        if v >expensive:
            expensive=v
    print(expensive)
    


print(check_stuff(products))
