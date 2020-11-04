#Create an application which solves the following problems.
#  - How much does Bob pay?
#  - How much does Alice pay?
#  - Who buys more Rice?
#  - Who buys more Potato?
#  - Who buys more different products?
#  - Who buys more products? (piece)



shopping={ "price": {"Milk" : 1.07, "Rice" : 1.59, "Eggs" : 3.14, "Cheese": 12.60, "Chicken" : 9.40, "Apples":2.31, "Tomato": 2.58, "Potato":1.75, "Onion":1.10},
           "bob" : {"Milk" : 3, "Rice" : 2, "Eggs" : 2, "Cheese": 1, "Chicken" : 4, "Apples":1, "Tomato": 2, "Potato":1},
           "alice" : {"Rice" : 1, "Eggs" : 5, "Chicken" : 2, "Apples":1, "Tomato": 10}}



def shop(shopping):
    bob_pay=[]
    for k,v in shopping["price"].items():
        for l,b in shopping["bob"].items():
            if k==l:
                bob_pay.append(v*b)
    print(sum(bob_pay))
    alice_pay=[]
    for d,f in shopping["price"].items():
        for x,y in shopping["alice"].items():
            if d==x:
                alice_pay.append(f*y)
    print(sum(alice_pay))
    

print(shop(shopping))


