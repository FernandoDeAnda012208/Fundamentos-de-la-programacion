nombre = "Fernando" #variable de tipo string
edad = 18 #variable tipo int
estatura = 1.66 #variable tipo float
es_estudiante = True #variable tipo boolean

# Imrpime la variable y su tipo de dato
print("Nombre:", nombre, type(nombre))
print("Edad:", edad, type(edad))
print("Estatura:", estatura, type(estatura))
print("Es estudiante:", es_estudiante, type(es_estudiante))
# Definimos una constante 
PROMEDIO_MINIMO = 6

# Recibimos datos y se los asignamos a las variables booleanas
materia = input("¿Qué materia cursas?")
calificacion = float(input("¿Qué calificación tienes?"))

# Operaciones basicas 
suma = 8 + 2
resto = 10 % 3
potencia = 2 ** 3

#Comparaciones
mayor_de_edad = edad >= 18
aprobado = calificacion >= PROMEDIO_MINIMO and es_estudiante


print("Suma:", suma, "| Resto:", resto, "| Potencia:", potencia)
print("Mayor de edad:", mayor_de_edad)
print("Aprobado:", aprobado)

# Comentarios para varias lineas 
'''
Le digo hola ella me dice goodbye

le digo nena como tu ya no hay
'''

#Comentarios solo de una línea