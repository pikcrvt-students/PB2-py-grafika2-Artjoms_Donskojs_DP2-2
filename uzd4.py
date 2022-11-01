from tkinter import *

window = Tk()
drawing = Canvas(window, height=500, width=500)
drawing.pack()
rect1 = drawing.create_rectangle(100, 100, 300, 200)
square1 = drawing.create_rectangle(30, 30, 80, 80)
oval1 = drawing.create_oval(100, 100, 300, 200)
circle1 = drawing.create_oval(30, 30, 80, 80)
