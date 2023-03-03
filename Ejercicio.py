#Desarrolle un algoritmo para hallar el area de un circulo,el usuario debe ingresar el Radio.
#Utilizar la fórmula: A=PI*r^2
import math
print("Ingrese el radio del circulo")
r = float(input()) # capturando el radio
a = math.pi* r*r
print ("El area de circulo con radio:",r,"Es: ",round(a,2))