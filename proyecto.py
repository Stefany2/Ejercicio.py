import tkinter

#------------------------ Window ------------------------

ventana = tkinter.Tk()
ventana.title("Ferreteria El Tornillo Feliz")
ventana.config(background="purple")
ventana. geometry("700x500")
ventana. resizable(0, 0)

#------------------------ Functions ------------------------

def calcular():
    subtotal1 = float(precio1Txt.get())*float(cantidad1Txt.get())
    importe1Txt.insert(0,str(subtotal1))

    subtotal2 = float(precio2Txt.get())*float(cantidad2Txt.get())
    importe2Txt.insert(0,str(subtotal2))

    subtotal3 = float(precio3Txt.get())*float(cantidad3Txt.get())
    importe3Txt.insert(0,str(subtotal3))

    subtotal4 = float(precio4Txt.get())*float(cantidad4Txt.get())
    importe4Txt.insert(0,str(subtotal4))

    totaltodos = float(importe1Txt.get()) + float(importe2Txt.get()) + float(importe3Txt.get()) + float(importe4Txt.get())
    totalTxt.insert(0, str(totaltodos)) 
    

def detallarPrecios1(nombre):
    precio1Txt.delete(0, tkinter.END)
    precio1Txt.insert(0, productos[nombre])

def detallarPrecios2(nombre):
    precio2Txt.delete(0, tkinter.END)
    precio2Txt.insert(0, productos[nombre])

def detallarPrecios3(nombre):
    precio3Txt.delete(0, tkinter.END)
    precio3Txt.insert(0, productos[nombre])

def detallarPrecios4(nombre):
    precio4Txt.delete(0, tkinter.END)
    precio4Txt.insert(0, productos[nombre])              
  
def eliminarTexto():
  apellidoTxt.delete(0, tkinter.END)
  dniTxt.delete(0, tkinter.END)
  nombreTxt.delete(0, tkinter.END)
  telefonoTxt.delete(0, tkinter.END)
  correoTxt.delete(0, tkinter.END)
  precio1Txt.delete(0, tkinter.END)
  precio2Txt.delete(0, tkinter.END)
  precio3Txt.delete(0, tkinter.END)
  precio4Txt.delete(0, tkinter.END)
  cantidad1Txt.delete(0, tkinter.END)
  cantidad2Txt.delete(0, tkinter.END)
  cantidad3Txt.delete(0, tkinter.END)
  cantidad4Txt.delete(0, tkinter.END)
  importe1Txt.delete(0, tkinter.END)
  importe2Txt.delete(0, tkinter.END)
  importe3Txt.delete(0, tkinter.END)
  importe4Txt.delete(0, tkinter.END)
  totalTxt.delete(0, tkinter.END)

#------------------------ Products ------------------------  

productos = {
    "Cemento"                : 15,
    "Clavos"                 : 5,
    "Martillo"               : 10,
    "Serrucho"               : 40,
    "Alicate"                : 8,
    "Carretillas"            : 45,
    "Escuadras"              : 8,
}

#------------------------ Labels, Text boxes and Buttons ------------------------

tiendaSticker = tkinter.Label(ventana, text = "Ferreteria El Tornillo Feliz", font= "Arial 14", bg="#808080", fg="White" )
nombresSticker = tkinter.Label(ventana, text = "Nombre(s):", font= "Arial 14", bg="#808080")
apellidosSticker = tkinter.Label(ventana, text = "Apellidos:", font= "Arial 14", bg="#808080")
dniSticker = tkinter.Label(ventana, text = "DNI:", font= "Arial 14", bg="#808080")
telefonoSticker = tkinter.Label(ventana, text = "Teléfono:", font= "Arial 14", bg= "#808080")
correoSticker = tkinter.Label(ventana, text = "Correo:", font= "Arial 14", bg= "#808080")
productoSticker = tkinter.Label(ventana, text = "Producto:", font= "Arial 14", bg= "#808080")
precioSticker = tkinter.Label(ventana, text = "Precio:", font= "Arial 14", bg= "#808080")
cantidadSticker = tkinter.Label(ventana, text = "Cantidad:", font= "Arial 14", bg= "#808080")
importeSticker = tkinter.Label(ventana, text = "Importe:", font= "Arial 14", bg= "#808080")
totalSticker = tkinter.Label(ventana, text = "Total:", font= "Arial 14", bg= "#808080")

tiendaSticker.place(x=220, y=20)
apellidosSticker.place(x= 50, y= 75)
dniSticker.place(x= 70, y= 120)
nombresSticker.place(x= 410, y= 70)
telefonoSticker.place(x= 410, y= 120)
correoSticker.place(x= 50 ,y= 180)
productoSticker.place(x= 100 ,y= 250)
precioSticker.place(x= 300 ,y= 250)
cantidadSticker.place(x= 440 ,y= 250)
importeSticker.place(x= 580 ,y= 250)
totalSticker.place(x= 480 ,y= 460)

apellidoTxt = tkinter.Entry(ventana, width=18 ,font = "Arial 12")
dniTxt = tkinter.Entry(ventana, width=18, font = "Arial 12")
nombreTxt = tkinter.Entry(ventana, width=18, font = "Arial 12")
telefonoTxt = tkinter.Entry(ventana, width=18, font = "Arial 12")
correoTxt = tkinter.Entry(ventana, width=55, font = "Arial 12")
precio1Txt = tkinter.Entry(ventana, width=10, font = "Arial 12")
precio2Txt = tkinter.Entry(ventana, width=10, font = "Arial 12")
precio3Txt = tkinter.Entry(ventana, width=10, font = "Arial 12")
precio4Txt = tkinter.Entry(ventana, width=10, font = "Arial 12")
cantidad1Txt = tkinter.Entry(ventana, width=10, font = "Arial 12")
cantidad2Txt = tkinter.Entry(ventana, width=10, font = "Arial 12")
cantidad3Txt = tkinter.Entry(ventana, width=10, font = "Arial 12")
cantidad4Txt = tkinter.Entry(ventana, width=10, font = "Arial 12")
importe1Txt = tkinter.Entry(ventana, width=10, font = "Arial 12")
importe2Txt = tkinter.Entry(ventana, width=10, font = "Arial 12")
importe3Txt = tkinter.Entry(ventana, width=10, font = "Arial 12")
importe4Txt = tkinter.Entry(ventana, width=10, font = "Arial 12")
totalTxt = tkinter.Entry(ventana, width=10, font = "Arial 12")

apellidoTxt.place(x= 175, y = 75)
dniTxt.place(x= 175, y = 120)
nombreTxt.place(x= 520, y = 74)
telefonoTxt.place(x= 520, y = 120)
correoTxt.place(x= 175, y = 180)
precio1Txt.place(x= 285, y = 300)
precio2Txt.place(x= 285, y = 340)
precio3Txt.place(x= 285, y = 380)
precio4Txt.place(x= 285, y = 420)
cantidad1Txt.place(x= 435, y = 300)
cantidad2Txt.place(x= 435, y = 340)
cantidad3Txt.place(x= 435, y = 380)
cantidad4Txt.place(x= 435, y = 420)
importe1Txt.place(x= 575, y = 300)
importe2Txt.place(x= 575, y = 340)
importe3Txt.place(x= 575, y = 380)
importe4Txt.place(x= 575, y = 420)
totalTxt.place(x= 575, y = 460)

boton1= tkinter.Button(ventana, text = "Calcular", font= "Arial 12", bg="white", fg="black", command= calcular)
boton2= tkinter.Button(ventana, text = "Reiniciar", font= "Arial 12", bg="white", fg="blue", command= eliminarTexto)

boton1.place(x= 55 , y = 460)
boton2.place(x= 150 , y = 460)

#------------------------ Products and prices modules ------------------------


tuplaProductos1 = ("Cemento", "Clavos", "Martillo", "Serrucho","Alicate", "Carretillas","Escuadras")

itemProductos1 = tkinter.StringVar(ventana, value = "Selecciona un producto")

listaProductos1 = tkinter.OptionMenu(ventana, itemProductos1, *tuplaProductos1, command= detallarPrecios1)

listaProductos1.place(x= 55 ,y= 300)

tuplaProductos2 = ("Cemento", "Clavos", "Martillo", "Serrucho","Alicate", "Carretillas","Escuadras" )

itemProductos2 = tkinter.StringVar(ventana, value = "Selecciona un producto")

listaProductos2 = tkinter.OptionMenu(ventana, itemProductos2, *tuplaProductos2, command= detallarPrecios2)

listaProductos2.place(x= 55 ,y= 340)

tuplaProductos3 = ("Cemento", "Clavos", "Martillo", "Serrucho","Alicate", "Carretillas","Escuadras" )

itemProductos3 = tkinter.StringVar(ventana, value = "Selecciona un producto")

listaProductos3 = tkinter.OptionMenu(ventana, itemProductos3, *tuplaProductos3, command= detallarPrecios3)

listaProductos3.place(x= 55 ,y= 380)

tuplaProductos4 = ("Cemento", "Clavos", "Martillo", "Serrucho","Alicate", "Carretillas","Escuadras" )

itemProductos4 = tkinter.StringVar(ventana, value = "Selecciona un producto")

listaProductos4 = tkinter.OptionMenu(ventana, itemProductos4, *tuplaProductos4, command= detallarPrecios4)

listaProductos4.place(x= 55 ,y= 420)

ventana.mainloop()
