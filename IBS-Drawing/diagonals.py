from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

diagonal1= canvas.create_line(0,0,300,300, fill= "green")

diagonal2=canvas.create_line(300,0,0,300,fill="red")
# If it starts from the upper-left corner it should be green, otherwise it should be red.

root.mainloop()