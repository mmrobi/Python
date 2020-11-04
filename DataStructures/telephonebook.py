# Telephone book

#We are going to represent our contacts in a map where the keys are going to be
#strings and the values are going to be strings as well.

#- Create a map with the following key-value pairs.

#  | Name (key)          | Phone number (value) |
#  | :------------------ | :------------------- |
#  | William A. Lathan   | 405-709-1865         |
#  | John K. Miller      | 402-247-8568         |
#  | Hortensia E. Foster | 606-481-6467         |
#  | Amanda D. Newland   | 319-243-5613         |
#  | Brooke P. Askew     | 307-687-2982         |

#- Create an application which solves the following problems.
#  - What is John K. Miller's phone number?
#  - Whose phone number is 307-687-2982?
#  - Do we know Chris E. Myers' phone number?

phonebook= {"{William A. Lathan":"405-709-1865", "John K. Miller":"402-247-8568", "Hortensia E. Foster":"606-481-6467","Amanda D. Newland":"319-243-5613", "Brooke P. Askew":"307-687-2982"}


def application(phonebook):
    print("The number of J.K.M. :" , phonebook["John K. Miller"])
    for k,v in phonebook.items():
        if v=="307-687-2982":
            print(k)
    for c,b in phonebook.items():
        if c=="Chris E. Myers":
            print("Yes ,we know the number, here it is: ", b)
        else:
            print("Unfortunatelly we don't know shit")
            break
            



print(application(phonebook))
