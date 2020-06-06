# - Create a variable named `orders`
#   with the following content: `["first", "second", "third"]`
# - Swap the first and the third element of `orders`

orders=["first", "second", "third"]
a,b=orders.index("first"), orders.index("third")
orders[b],orders[a]=orders[a],orders[b]


print(orders)
