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

a.create_text(50, 30, text='LAIKS', fill='white')
a.create_text(150, 30, text='REZULTĀTS', fill='white')
laiks_teksts = a.create_text(50, 50, fill='white')
rezultats_teksts = a.create_text(150, 50, fill='white')
def paradit_rezultatu(rezultats):
    a.itemconfig(rezultats_teksts, text=str(rezultats))
def paradit_laiku(laiks_palicis):
    a.itemconfig(laiks_teksts, text=str(laiks_palicis))



burb_nejausi = 10
laika_ierobezojums = 30
papildlaika_rez = 1000
rezultats = 0
papildu = 0
beigas = time() + laika_ierobezojums



#Speles galvenais cikls

while time() < beigas:
    if randint(1, burb_nejausi) == 1:
        izveidot_burbuli()
        parvietot_burbulus()
        notirit_burbulus()
        rezultats += sadursme()
        if (int(rezultats / papildlaika_rez)) > papildu:
            papildu += 1
            beigas += laika_ierobezojums
        paradit_rezultatu(rezultats)
        paradit_laiku(int(beigas - time()))
        logs.update()
        sleep(0.01)

#SPĒLES BEIGAS

a.create_text(vid_x, vid_y, \
    text = 'SPĒLES BEIGAS', fill='white', font=('Helvetica',30))
a.create_text(vid_x, vid_y + 30, \
    text = 'Rezultāts: '+ str(rezultats), fill='white')
a.create_text(vid_x, vid_y + 45, \
    text = 'Papildu laiks: '+ str(papildu*laika_ierobezojums), fill='white')
