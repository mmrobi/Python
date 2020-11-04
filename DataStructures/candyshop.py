shop_items = ["Cupcake", 2, "Brownie", False]

# Accidentally we added "2" and "false" to the list.
# Your task is to change from "2" to "Croissant" and change from "false" to "Ice cream"
# No, don't just remove the items :)
# Create a function called sweets() which takes the list as a parameter.
# Expected output: "Cupcake", "Croissant", "Brownie", "Ice cream"

def sweets(shop_items):
    shop_items[1]= "Croissant"
    shop_items[3]= "Ice cream"
    print(shop_items)

print(sweets(shop_items))
    
