import tkinter
from tkinter import *
#from time import sleep
#from pyfirmata import Arduino




#arduino = Arduino("COM4")
#sleep(5)



def camara():
    import camara


def modelo():
    import detectando

def prueba():
    import prueba

root = Tk()
root.title("menu de opciones")
root.minsize(300,150)

bon = Button(root, text="tomar fotos", command=camara)
bon.grid(column=1, row=4)

boff = Button(root, text="crear modelo", command=modelo)
boff.grid(column=2, row=4)

boff = Button(root, text="reconocimiento facial", command=prueba)
boff.grid(column=3, row=4)

root.mainloop()