# Write a function that checks if the list contains "7" if it contains return "Hoorray" otherwise return "Noooooo"

numbers = [1, 2, 3, 4, 5,7, 6, 8];
def contains_seven(numbers):
    solution="Noooo"
    for x in numbers:
        if x == 7:
            solution="Hoorray"
        
    return solution
    
    
            
print(contains_seven(numbers))
# The output should be: "Noooooo"
# Do this again with a different solution using different list functions!

