

ISBN_map={"978-1-60309-452-8":"A Letter to Jo","978-1-60309-459-7":"Lupus","978-1-60309-444-3":"Red Panda and Moon Bear", "978-1-60309-461-0":"The Lab"}

for k,v in ISBN_map.items():
    print(v + '(ISBN: '+ k +")" )

#- Remove the key-value pair with key 978-1-60309-444-3
#- Remove the key-value pair with value The Lab
#- Add the following key-value pairs to the map

#  | Key               | Value                 |
#  | :---------------- | :-------------------- |
#  | 978-1-60309-450-4 | They Called Us Enemy  |
#  | 978-1-60309-453-5 | Why Did We Trust Him? |

#- Print whether there is an associated value with key 478-0-61159-424-8 or not
#- Print the value associated with key 978-1-60309-453-5


del ISBN_map['978-1-60309-444-3']
print (ISBN_map)
del ISBN_map["978-1-60309-461-0"]
print(ISBN_map)

ISBN_map["978-1-60309-450-4"]="They Called Us Enemy"
ISBN_map["978-1-60309-453-5"]="Why Did We Trust Him"
print(ISBN_map)

for k,v in ISBN_map.items():
    if k =='478-0-61159-424-8':
        print('Yes')
    else:
        print(" There's no such ISBN, fuck off")
        break
    
print(ISBN_map['978-1-60309-453-5'])
