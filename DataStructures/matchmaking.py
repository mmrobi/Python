# Write function that joins the two lists by matching one girl with one boy in a new list
# If someone has no pair, he/she should be the element of the list too
# Exepected output: ["Eve", "Joe", "Ashley", "Fred"...]

girls = ["Eve", "Ashley", "Claire", "Kat", "Jane"]
boys = ["Joe", "Fred", "Tom", "Todd", "Neef", "Jeff"]

def making_matches(girls, boys):
    match=[]
    for x in boys:
        for y in girls:
            if boys.index(x) == girls.index(y):
                match.append(x)
                match.append(y)
    if len(boys) > len(girls):
        diff= len(boys)-len(girls)
        match.extend(boys[-diff:])
       
    return match

print(making_matches(girls, boys))
