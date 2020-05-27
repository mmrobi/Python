current_hours = 14;
current_minutes = 34;
current_seconds = 42;

# Write a program that prints the remaining seconds (as an integer) from a
# day if the current time is represented by the variables

sec=1
minute=60
hour=3600
Day=24*3600

tRemaining=Day-(current_hours*hour+current_minutes*minute+current_seconds*sec)

print(tRemaining)
