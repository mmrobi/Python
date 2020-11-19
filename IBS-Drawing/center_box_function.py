from tkinter import *
import random
root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def draw_square(a):
    canvas.create_rectangle(150-(a/2),150-(a/2),150+(a/2),150+(a/2))

for i in range(0,3):
    draw_square(random.randint(0,295))

# Create a function that draws one square and takes 1 parameters:
# The square size
# and draws a square of that size to the center of the canvas.
# Draw 3 squares with that function.
# Avoid code duplication.

root.mainloop()