from tkinter import *
import random
import itertools

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
size=[]
for x in range(300,0,-25):
    size.append(x)
print(size)
def draw_rainboxsquare(a, c):
    canvas.create_rectangle(150 - (a / 2), 150 - (a / 2), 150 + (a / 2), 150 + (a / 2), fill=c)



for i in range(0, 11):
    c= colors[i]
    a = size[i]
    draw_rainboxsquare(a, c)
# Create a square drawing function that takes 2 parameters:
# The square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# Create a loop that fills the canvas with rainbow colored squares (red, orange, yellow, green, blue, indigo, violet).

root.mainloop()