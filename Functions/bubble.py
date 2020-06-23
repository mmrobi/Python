#  Create a function that takes a list of numbers as parameter
#  Returns a list where the elements are sorted in ascending numerical order
#  Make a second boolean parameter, if it's `True` sort that list descending


def bubble(arr):
    for x in range(len(arr)):
        for y in range(x+1, len(arr)):
            if arr[x]>arr[y]:
                arr[x],arr[y]=arr[y],arr[x]
    return arr



def advanced_bubble(arr, is_descending):
    if is_descending:
        for x in range(len(arr)):
            for y in range(x+1, len(arr)):
                if arr[x]<arr[y]:
                    arr[x],arr[y]=arr[y],arr[x]
    return arr
                    
    


#  Example:
print(bubble([43, 12, 24, 9, 5]))
#  should print [5, 9, 12, 24, 34]
print(advanced_bubble([43, 12, 24, 9, 5], True))
#  should print [34, 24, 9, 5]
