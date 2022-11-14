from tkinter import *
from random import randint
from time import sleep, time

garums = 500
platums = 800

logs=Tk()
logs.title("Burbuļu spridzinātājs")

a = Canvas(logs, width=platums, height=garums, bg='darkblue')
a.pack()

kuga_id = a.create_polygon(5, 5, 5, 25, 30, 15, fill="red")
kuga_id2 = a.create_polygon(0, 0, 30, 30, outline="red")

kuga_r = 15
vid_x = platums / 2
vid_y = garums / 2

a.move(kuga_id, vid_x, vid_y)
a.move(kuga_id2, vid_x, vid_y)

kuga_atr = 10

def parvietot_kugi(notikums):
    if notikums.keysym == 'Up':
        a.move(kuga_id, 0, -kuga_atr)
        a.move(kuga_id2, 0, -kuga_atr)
    elif notikums.keysym == 'Down':
        a.move(kuga_id, 0, kuga_atr)
        a.move(kuga_id2, 0, kuga_atr)
    elif notikums.keysym == 'Left':
        a.move(kuga_id, -kuga_atr ,0)
        a.move(kuga_id2, -kuga_atr, 0)
    elif notikums.keysym == 'Right':
        a.move(kuga_id, kuga_atr ,0)
        a.move(kuga_id2, kuga_atr, 0)
a.bind_all('<Key>', parvietot_kugi)

burb_id = list()
burb_r = list()
burb_atrums = list()

min_burb_r = 10
max_burb_r = 30
max_burb_atr = 10

atstarpe = 100

def izveidot_burbuli():
    x = platums + atstarpe
    y = randint(0, garums)
    r = randint(min_burb_r, max_burb_r)

    id1 = a.create_oval(x - r, y -r, x + r, y + r, outline = 'white')

    burb_id.append(id1)
    burb_r.append(r)
    burb_atrums.append(randint(1, max_burb_atr))

def parvietot_burbulus():
    for i in range(len(burb_id)):
        a.move(burb_id[i], 0)

def iegut_koord(id_skaitlis):
    poz = a.coords(id_skaitlis)
    x = (poz[0] + poz[2]) / 2
    y = (poz[1] + poz[3]) / 2
    return x,y


def dzest_burbuli(i):
    del burb_r[i]
    del burb_atrums[i]
    a.delete(burb_id[i])
    del burb_id[i]

def notirit_burbulus():
    for i in range(len(burb_id)-1, -1, -1):
        x,y = iegut_koord(burb_id[i])
        if x < -atstarpe:
            dzest_burbuli(i)

from math import sqrt

def attalums(id1, id2):
    x1, y1 = iegut_koord(id1)
    x2, y2 = iegut_koord(id2)
    return sqrt((x2-x1)**2 + (y2-y1)**2)

def sadursme():
    punkti=0
    for burb in range(len(burb_id)-1, -1, -1):
        if attalums(kuga_id2, burb_id[burb]) < (kuga_r + burb_r[burb]):
            punkti += (burb_r[burb] + burb_atrums[burb])
            dzest_burbuli(burb)
    return punkti

burb_nejausi = 10

#Speles galvenais cikls

while True:
    if randint(1, burb_nejausi) == 1:
        izveidot_burbuli()
        parvietot_burbulus()
        notirit_burbulus()
        logs.update()
        sleep(0.01)
