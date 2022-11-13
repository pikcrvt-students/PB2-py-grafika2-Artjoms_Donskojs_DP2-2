from tkinter import *

def Adarbiba():
    print("paldies") #Šis ziņojums parādās, kad tiek piespiesta A poga.
def Bdarbiba():
    print("Au! man sap!") #Šis ziņojums parādās, kad tiek piespiesta B poga.
logs = Tk()
pogaA = Button(logs, text="Klikšķini te!", command=Adarbiba) #Šāds teksts būs redzams uz A pogas
pogaB = Button(logs, text='Neklikšķini te!', command=Bdarbiba)#Šāds teksts būs redzams uz B pogas

#Šis kods liek datoram ievietot pogas logā.
pogaA.pack()
pogaB.pack()
