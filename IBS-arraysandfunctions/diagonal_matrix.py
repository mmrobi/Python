# - Create (dynamically) a two dimensional list
#   with the following matrix. Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1
#
# - Print this two dimensional list to the output

list1=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
for x in list1:
    for y in x:
        print(y, end=" ")
    print()
