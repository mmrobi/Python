from tkinter import *
import random
root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# Create a function that draws a single line and takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# Draw at least 3 lines with that function using a loop.
def draw_horizontal(x,y):
    canvas.create_line(x,y,x+50,y,fill="red")

for i in range(0,5):
    draw_horizontal(random.randint(0,250),random.randint(0,300))


root.mainloop()