from tkinter import *
import random
import itertools

root = Tk()

canvas = Canvas(root, width='400', height='400')
canvas.pack()

#canvas.create_rectangle(10,10,20,20,fill="purple")
def create_steps(x0,y0,x1,y1,c):
    canvas.create_rectangle(x0, y0, x1, y1, fill="purple")

for i in range(0,20):
    while i < 20:
        x0=10
        x0+=10
        y0=10
        y0+=10
        x1=20
        x1+=10
        y1=20
        y1+=10
        c=fill="purple"
        create_steps(x0, y0, x1, y1, c)






root.mainloop()