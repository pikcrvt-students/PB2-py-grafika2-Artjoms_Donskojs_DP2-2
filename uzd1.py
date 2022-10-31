from tkinter import *

def Adarbiba():
    print("paldies")
def Bdarbiba():
    print("Au! man sap!")
logs = Tk()
pogaA = Button(logs, text="Klikšķini te!", command=Adarbiba)
pogaB = Button(logs, text='Neklikšķini te!', command=Bdarbiba)

pogaA.pack()
pogaB.pack()
