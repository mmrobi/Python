#Create a function named **is anagram** following your current language's style
#guide. It should take two strings and return a boolean value depending on
#whether its an anagram or not.

### Examples

#| input 1 | input 2 | output |
#| :-----: | :-----: | :----: |
#|  "dog"  |  "god"  |  true  |
#| "green" |  "fox"  |  false |
first=str(input("Write a word: "))
second=str(input("Write another word or the anagram of your 1st: "))

def is_anagram(first,second):
    if (sorted(first) == sorted(second)):
        anagram = True
    else:
        anagram = False
    return anagram

print(is_anagram(first,second))

        
         
