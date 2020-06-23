## Exercise

#Create a function named **search palindrome** following your current language's
#style guide. It should take a string, search for palindromes that at least 3
#characters long and return a list with the found palindromes.

### Examples

#|               input              |                          output                         |
#| :------------------------------: | :-----------------------------------------------------: |
#| "dog goat dad duck doodle never" | \["og go", "g g", " dad ", "dad", "d d", "dood", "eve"] |
#|              "apple"             |                            []                           |
#|             "racecar"            |               \["racecar", "aceca", "cec"]              |
#|                ""                |                            []                           |


def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False


def search_palindrome(asd):
    sort = []
    for x in range(0, len(asd)):
        for y in range(0,len(asd)):
            if y-x >2:
                if is_palindrome(asd[x:y]):
                       sort.append(asd[x:y])
    return sort

print(search_palindrome("dog goat dad duck doodle never"))

    
