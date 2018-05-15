from tkinter import *

raiz=Tk()

raiz.title("Pokedex")

raiz.iconbitmap("lol.ico")

raiz.geometry("620x430")

raiz.resizable(0,0)

raiz.config(bg="blue")


#####################################

frame1=Frame()

frame1.pack(fill=BOTH, expand=YES)


#########################################

texto = Label(text= "Nombre: ").place(x= 310,y=70)
entrada= StringVar()
CuadroTexto= Entry(raiz,textvariable=entrada).place(x=380,y=70)



#########################################

"""
PARA IMAGENES SOLO SE PUEDE PNG Y GIF
"""

Fondo2= PhotoImage(file="plantilla.png")


IblFondo= Label(frame1, image=Fondo2).place(x=0,y=0)







raiz.mainloop()
