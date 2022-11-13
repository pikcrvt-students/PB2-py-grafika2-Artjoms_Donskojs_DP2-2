from tkinter import *
from random import randint #Šis importē funkciju 'randint' no random bibliotēkas.

def ripinat():
    #Šis kods nodzēš tekstu lauciņā un tajā parāda nejauši izvēlētu skaitli intervālā no 1 līdz 6.
    teksts.delete(0.0, END)
    teksts.insert(END, str(randint(1,6)))
logs = Tk()
teksts = Text(logs, width = 1, height=1)
pogaA = Button(logs, text="Klikšķini, lai ripininātu", command=ripinat)
teksts.pack()
pogaA.pack()
