from tkinter import *
from random import *

izmers = 500

logs = Tk()

audeklis = Canvas(logs, width=izmers, height=izmers)
audeklis.pack()

while True:
    krasa = choice(['pink', 'orange', 'purple', 'yellow'])
    x0=randint(0, izmers)
    y0=randint(0, izmers)
    d = randint(0, izmers/5)
    audeklis.create_oval(x0, y0, x0 + d, y0 + d, fill=krasa)
    logs.update()
