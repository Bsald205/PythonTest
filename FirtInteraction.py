#FIRST INTERACTION WITH PYTHON TKINTER LIBRERBY 
#FEW EXAMPLES LISTED BLOW 

import tkinter 

ventana =  tkinter.Tk ()
ventana.geometry ("300x300")

""" ETIQUETAS FUNCIONAMIENTO  
etiqueta = tkinter.Label(ventana, text= "Hola mundo", background= "blue")
etiqueta.pack(fill= tkinter.Y, expand= 1)  #se puede cambiar por X,Y y BOTH pero se necesita mantener el true o 1#  """

""" BOTONES FUNCIONAMIENTO
def saludoBoton(nombre):
    print ("Hola" + nombre)

boton1 = tkinter.Button (ventana, text = "Click", padx = 50, pady = 20, command= lambda: saludoBoton (" python")) #lamda se usa para funciones #
boton1.pack() """

""" ETIAQUETAS/ CAJA DE TEXTO FUNCIONAMIENTO
cajaTexto = tkinter.Entry (ventana, font = "Helvetica 20")
cajaTexto.pack()

etiqueta = tkinter.Label (ventana)
etiqueta.pack()

def textoDeCaja():
    texto = cajaTexto.get()
    etiqueta ["text"] = texto

boton2 =tkinter.Button (ventana, text="Click", command= textoDeCaja)
boton2.pack()"""

boton3 = tkinter.Button (ventana, text= "Boton 1", width= 10, height= 5)
boton4 = tkinter.Button (ventana, text= "Boton 2", width= 10, height= 5)
boton5 = tkinter.Button (ventana, text= "Boton 3", width= 10, height= 5)

boton3.grid(row=0,column=0)
boton4.grid(row=1,column=1)
boton5.grid(row=2,column=2)


ventana.mainloop()
