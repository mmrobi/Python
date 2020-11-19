from tkinter import *
import random
root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def draw_square(x,y):
    canvas.create_rectangle(x,y,x+50,y+50)

for i in range(0,3):
    draw_square(random.randint(0,250),random.randint(0,250))
# Create a function that draws one square and takes 2 parameters:
# The x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# Draw 3 squares with that function.
# Avoid code duplication.

root.mainloop()