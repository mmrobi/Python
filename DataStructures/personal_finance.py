# Personal finance

#We are going to represent our expenses in a list containing integers.

#- Create a list with the following items.
#  - 500, 1000, 1250, 175, 800 and 120
#- Create an application which solves the following problems.
#  - How much did we spend?
#  - Which was our greatest expense?
#  - Which was our cheapest spending?
#- What was the average amount of our spendings?

expenses=[500, 1000, 1250, 175, 800, 120]

def application(expenses):
    print(" We spent: ", sum(expenses))
    print("Our greatest expense was: ", max(expenses))
    print("Our cheapest expense was: ", min(expenses))
    avg= sum(expenses)/len(expenses)
    print("The average amount was: ", avg)

print(application(expenses))
    
        
    
    
