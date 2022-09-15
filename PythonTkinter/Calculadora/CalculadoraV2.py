#Better working calculator, implements adaptative screen resolution, also 1 character cut, and cool vew :D
#TODO maybe i'll try to get in the ^2,% andsquare root functions 

from tkinter import *
from tkinter import ttk

ventana = Tk()
ventana.title ("Calculadora_V2")
ventana.geometry ("+500+80")
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)
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
def elimina():
    E_Texto_state = E_Texto.get()
    if len (E_Texto_state):
        E_Texto_new_state = E_Texto_state[:-1]
        borrar()
        E_Texto.insert(0,E_Texto_new_state)
    else:   
        borrar()
        E_Texto.instert(0, "Error")
        
    
#ESTILO

estilo = ttk.Style()
estilo.theme_use('clam')
estilo.configure('mainframe.TFrame', background = "#002B5B")

mainframe = ttk.Frame(ventana,style = "mainframe.TFrame")
mainframe.grid(column=0, row=0, sticky=(W,N,E,S))
mainframe.columnconfigure(0,weight=1)
mainframe.columnconfigure(1,weight=1)
mainframe.columnconfigure(2,weight=1)
mainframe.columnconfigure(3,weight=1)

E_Texto =ttk.Entry(mainframe, font = "arial 15", width= 5)
E_Texto.grid(row=0,column=0, columnspan=4, sticky=(W,N,E,S))
mainframe.rowconfigure(0,weight=1)
mainframe.rowconfigure(1,weight=1)
mainframe.rowconfigure(2,weight=1)
mainframe.rowconfigure(3,weight=1)
mainframe.rowconfigure(4,weight=1)
mainframe.rowconfigure(5,weight=1)
mainframe.rowconfigure(6,weight=1)

estilo_boton_numeros  = ttk.Style()
estilo_boton_numeros.configure ('estilo_num.TButton', font = "arial 15", width= 5, background = "#FFFFFF", relief = "flat" )

estilo_borrar_numeros  = ttk.Style()
estilo_borrar_numeros.configure ('estilo_borrar.TButton', font = "arial 15", width= 5, background = "#2B4865", relief = "flat" )
estilo_borrar_numeros.map('estilo_borrar.TButton', foreground= [('active', '#FF0000')]) 
estilo_parentecis_numeros  = ttk.Style()
estilo_parentecis_numeros.configure ('estilo_parentecis.TButton', font = "arial 15", width= 5, background = "#2B4865", relief = "flat" )

estilo_operacion = ttk.Style()
estilo_operacion.configure('estilo_operacion.TButton', font = "arial 15", width= 5,background = "#256D85", relief = "flat")

estilo_igual = ttk.Style()
estilo_igual.configure ('estilo_igual.TButton', font = "arial 15", width= 5,background = "#8FE3CF", relief = "flat")

#BOTONES
button0 = ttk.Button(mainframe, text="0", style= "estilo_num.TButton", command= lambda: click_Boton(0))
button1 = ttk.Button(mainframe, text="1", style= "estilo_num.TButton", command= lambda: click_Boton(1))
button2 = ttk.Button(mainframe, text="2", style= "estilo_num.TButton", command= lambda: click_Boton(2))
button3 = ttk.Button(mainframe, text="3", style= "estilo_num.TButton", command= lambda: click_Boton(3))
button4 = ttk.Button(mainframe, text="4", style= "estilo_num.TButton", command= lambda: click_Boton(4))
button5 = ttk.Button(mainframe, text="5", style= "estilo_num.TButton", command= lambda: click_Boton(5))
button6 = ttk.Button(mainframe, text="6", style= "estilo_num.TButton", command= lambda: click_Boton(6))
button7 = ttk.Button(mainframe, text="7", style= "estilo_num.TButton", command= lambda: click_Boton(7))
button8 = ttk.Button(mainframe, text="8", style= "estilo_num.TButton", command= lambda: click_Boton(8))
button9 = ttk.Button(mainframe, text="9", style= "estilo_num.TButton", command= lambda: click_Boton(9))

button_sum = ttk.Button(mainframe, text="+", style= "estilo_operacion.TButton", command= lambda: click_Boton("+"))
button_rest = ttk.Button(mainframe, text="-", style= "estilo_operacion.TButton", command= lambda: click_Boton("-"))
button_mult = ttk.Button(mainframe, text="x", style= "estilo_operacion.TButton", command= lambda: click_Boton("*"))
button_div = ttk.Button(mainframe, text="/", style= "estilo_operacion.TButton", command= lambda: click_Boton("/"))

button_borr = ttk.Button(mainframe, text= chr (9003), style= "estilo_borrar.TButton", command= lambda: elimina())
button_ac = ttk.Button(mainframe, text=chr (9760), style= "estilo_borrar.TButton", command= lambda: borrar())
button_par1 = ttk.Button(mainframe, text="(", style= "estilo_parentecis.TButton", command= lambda: click_Boton("("))
button_par2 = ttk.Button(mainframe, text=")", style= "estilo_parentecis.TButton", command= lambda: click_Boton(")"))
button_punt = ttk.Button(mainframe, text=".", style= "estilo_parentecis.TButton", command= lambda: click_Boton("."))
button_igu = ttk.Button(mainframe, text="=", style= "estilo_igual.TButton", command= lambda: operacion())

#BOTON EN PANTALLA  
button0.grid(column= 0 , row= 5, columnspan = 2, sticky=(W,N,E,S))
button1.grid(column= 0 , row= 4, sticky=(W,N,E,S))
button2.grid(column= 1 , row= 4, sticky=(W,N,E,S))
button3.grid(column= 2 , row= 4, sticky=(W,N,E,S))
button4.grid(column= 0 , row= 3, sticky=(W,N,E,S))
button5.grid(column= 1 , row= 3, sticky=(W,N,E,S))
button6.grid(column= 2 , row= 3, sticky=(W,N,E,S))
button7.grid(column= 0 , row= 2, sticky=(W,N,E,S))
button8.grid(column= 1 , row= 2, sticky=(W,N,E,S))
button9.grid(column= 2 , row= 2, sticky=(W,N,E,S))

button_sum.grid(column= 3, row= 2, sticky=(W,N,E,S))
button_rest.grid(column= 3, row= 3, sticky=(W,N,E,S))
button_mult.grid(column= 3, row= 4, sticky=(W,N,E,S))
button_div.grid(column= 3, row= 5, sticky=(W,N,E,S))

button_borr.grid(column= 3, row= 1, sticky=(W,N,E,S))
button_ac.grid(column= 2, row= 1, sticky=(W,N,E,S))
button_par1.grid(column= 0, row= 1, sticky=(W,N,E,S))
button_par2.grid(column= 1, row= 1, sticky=(W,N,E,S))
button_punt.grid(column= 2, row= 5, sticky=(W,N,E,S))
button_igu.grid(column= 0, row= 6, columnspan = 4, sticky=(W,N,E,S))

#ESPACIO ENTRE BOTONES
for child in mainframe.winfo_children ():
    child.grid_configure(ipady=10,padx=1,pady=1)
    
ventana.mainloop()
