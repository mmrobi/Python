from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw a box that has different colored lines on each edge.
box = canvas.create_rectangle(50, 50, 200, 150, fill="grey")
topline = canvas.create_line(50, 50, 200, 50, fill="red")
leftline = canvas.create_line(50, 50, 50, 150, fill="green")
rightline = canvas.create_line(200, 50, 200, 150, fill="blue")
bottomline = canvas.create_line(50, 150, 200, 150, fill="orange")
root.mainloop()
