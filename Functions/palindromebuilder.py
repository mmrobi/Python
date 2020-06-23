### Exercise

#Create a function named **create palindrome** following your current language's
#style guide. It should take a string, create a palindrome from it and then
#return it.

### Examples

#|    input   |       output       |
#| :--------: | :----------------: |
#|     ""     |         ""         |
#| "greenfox" | "greenfoxxofneerg" |
#|    "123"   |      "123321"      |
word=str(input("Write a word: "))

def create_palindrome(word):
    palindrome=word + word[::-1]
    return palindrome


def create_palindrome2(kaka):
    asd= kaka
    for x in reverse(kaka):
        asd +=x
    return asd


def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str
        


print (create_palindrome2(word))

    
