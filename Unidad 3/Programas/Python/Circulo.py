import math #Esta linea importa la librería math para poder usar funciones matemáticas

radio = float(input("Radio del círculo: "))

area = math.pi * math.pow(radio, 2)
perimetro = 2 * math.pi * radio

print("Area:", round(area, 2))
print("Perímetro:", round(perimetro, 2))
print("Raiz cuadrada del radio:", round(math.sqrt(radio), 2))
print("Techo del área:", math.ceil(area))

#Tres ejemplos de funciones de la libreria math son pi, sqrt y pow

#Ejemplo de uso de la función pi

x = math.pi
print("Pi vale", x)

#Ejemplo de sqrt

y = 25
print("La raíz cuadrada de", y, "es:", math.sqrt(y))

#Ejemplo de pow

x2 = 3
y2 = 2
pow = math.pow(x2, y2)
print(x2, "elevado a", y2, "es:", pow)