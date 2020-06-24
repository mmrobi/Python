#- Create an empty map where the keys are integers and the values are characters
#- Print out whether the map is empty or not
#- Add the following key-value pairs to the map

#  | Key | Value |
#  | :-- | :---- |
#  | 97  | a     |
#  | 98  | b     |
#  | 99  | c     |
#  | 65  | A     |
#  | 66  | B     |
#  | 67  | C     |

#- Print all the keys
#- Print all the values
#- Add value D with the key 68
#- Print how many key-value pairs are in the map
#- Print the value that is associated with key 99
#- Remove the key-value pair where with key 97
#- Print whether there is an associated value with key 100 or not
#- Remove all the key-value pairs

mapecske= {97:'a', 98:'b', 99:'c', 65:'A', 66:'B', 67:'C'}

if len(mapecske)  ==0:
    print("empty")
else:
    print("not empty")

for k,v in mapecske.items():
    print(k)
    print(v)

mapecske[68]= 'D'

print(len(mapecske))

print(mapecske[99])

del mapecske[97]

print(mapecske)


if k==100 is True in mapecske.items():
    print(mapecske[100])
else:
    print("There is no key = 100")

mapecske{:}={}
print(mapecske)

mapecske.clear()

        
