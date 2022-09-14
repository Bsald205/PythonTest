# CALCULADORA EN PYTHON USANDO TKINTER 

#TODO  IMPLEMENTAR MEJORA VISUAL 

from tkinter import *

ventana = Tk()
ventana.title ("Calculadora")
i = 0

#FUNCIONES 
def click_Boton(valor):
    global i
    E_Texto.insert (i, valor)
    i += 1
    
def borrar():
    E_Texto.delete (0,END)
    i = 0
def operacion():
    ecuacion = E_Texto.get()
    resultado = eval (ecuacion)
    E_Texto.delete(0,END)
    E_Texto.insert (0,resultado)
    i = 0 
    
#ENTRADAS 

E_Texto =Entry(ventana,font= ("Calibri 20"))
E_Texto.grid(row=0,column=0, columnspan=4, padx=10,pady=10)

#BOTONES

boton1 = Button (ventana, text="1", width=5, height=2, command= lambda: click_Boton(1))
boton2 = Button (ventana, text="2", width=5, height=2, command= lambda: click_Boton(2))
boton3 = Button (ventana, text="3", width=5, height=2, command= lambda: click_Boton(3))
boton4 = Button (ventana, text="4", width=5, height=2, command= lambda: click_Boton(4))
boton5 = Button (ventana, text="5", width=5, height=2, command= lambda: click_Boton(5))
boton6 = Button (ventana, text="6", width=5, height=2, command= lambda: click_Boton(6))
boton7 = Button (ventana, text="7", width=5, height=2, command= lambda: click_Boton(7))
boton8 = Button (ventana, text="8", width=5, height=2, command= lambda: click_Boton(8))
boton9 = Button (ventana, text="9", width=5, height=2, command= lambda: click_Boton(9))
boton0 = Button (ventana, text="0", width=16, height=2, command= lambda: click_Boton(0))

boton_sum = Button (ventana, text="+", width=5, height=2, command= lambda: click_Boton("+"))
boton_rest = Button (ventana, text="-", width=5, height=2, command= lambda: click_Boton("-"))
boton_div = Button (ventana, text="/", width=5, height=2, command= lambda: click_Boton("/"))
boton_mult = Button (ventana, text="x", width=5, height=2, command= lambda: click_Boton("*"))

boton_ac = Button (ventana, text="AC", width=5, height=2, command= lambda: borrar())
boton_par1 = Button (ventana, text="(", width=5, height=2, command= lambda: click_Boton("("))
boton_par2 = Button (ventana, text=")", width=5, height=2, command= lambda: click_Boton(")"))
boton_punt = Button (ventana, text=".", width=5, height=2, command= lambda: click_Boton("."))
boton_igu = Button (ventana, text="=", width=5, height=2, command= lambda: operacion())

#BOTON EN PANTALLA

boton_ac.grid(row =1, column=0 , padx=5, pady=5)
boton_par1.grid(row =1, column=1 , padx=5, pady=5)
boton_par2.grid(row =1, column=2 , padx=5, pady=5)
boton_punt.grid(row =5, column=2, padx=5, pady=5)

boton0.grid(row =5,  column=0 ,columnspan = 2, padx=5, pady=5)
boton1.grid(row =4, column=0 , padx=5, pady=5)
boton2.grid(row =4, column=1 , padx=5, pady=5)
boton3.grid(row =4, column=2 , padx=5, pady=5)
boton4.grid(row =3, column=0 , padx=5, pady=5)
boton5.grid(row =3, column=1 , padx=5, pady=5)
boton6.grid(row =3, column=2 , padx=5, pady=5)
boton7.grid(row =2, column=0 , padx=5, pady=5)
boton8.grid(row =2, column=1 , padx=5, pady=5)
boton9.grid(row =2, column=2 , padx=5, pady=5)

boton_sum.grid(row =4, column=3 , padx=5, pady=5)
boton_rest.grid(row =3, column=3 , padx=5, pady=5)
boton_div.grid(row =1, column=3 , padx=5, pady=5)
boton_mult.grid(row =2, column=3 , padx=5, pady=5)
boton_igu.grid(row =5, column=3 , padx=5, pady=5)


ventana.mainloop()

Calculadora python.png
