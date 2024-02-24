import math 

def calcular_area (radio):
    radio = float(input("ingrese el valor: "))
    resultado = math.pi*(radio**2)
    return resultado

x = calcular_area(1.72)
print(x)