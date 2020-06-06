# - Create a variable named `animals`
#   with the following content: `["koal", "pand", "zebr"]`
# - Add all elements an `"a"` at the end

animals=["koal", "pand", "zebr"]

animals=[x+"a" for x in animals]

print(animals)
