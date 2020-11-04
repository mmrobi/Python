from tkinter import *
import random

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def draw_lines(x,y):
    canvas.create_line(x,y,150,150)

for i in range(0,15):
    draw_lines(random.randint(0,300),random.randint(0,300))

# Create a function that draws a single line and takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# Draw at least 3 lines with that function using a loop.

root.mainloop()