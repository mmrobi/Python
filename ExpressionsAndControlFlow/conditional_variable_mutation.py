a = 24
out = 0
out +=1
# if a is even increment out by one
if int(a):
    print(out)






b = 22
out2 = ""

if 10<b<20:
    out2="Sweet!"
elif b<10:
    out2="Less!"
elif b>20:
    out2="More!"
    
# if b is between 10 and 20 set out2 to "Sweet!"
# if less than 10 set out2 to "Less!",
# if more than 20 set out2 to "More!"

print(out2)




c = 123
credits = 100
is_bonus = True
# if credits are at least 50,
# and is_bonus is false decrement c by 2
# if credits are smaller than 50,
# and is_bonus is false decrement c by 1
# if is_bonus is true c should remain the same

if credits>=50:
    c-=2
    is_bonus= False
elif credits<50:
    c-=1
    is_bonus= False
elif is_bonus=True:
    c=c
    
print(c)




d = 8
time = 120
out3 = ""
# if d is dividable by 4
# and time is not more than 200
# set out3 to "check"
# if time is more than 200
# set out3 to "Time out"
# otherwise set out3 to "Run Forest Run!"


print(out3)
