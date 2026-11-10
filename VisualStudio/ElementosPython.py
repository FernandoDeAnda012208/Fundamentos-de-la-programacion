nombre = "Fernando"
edad = 18
estatura = 1.66
es_estudiante = True

print("Nombre:", nombre, type(nombre))
print("Edad:", edad, type(edad))
print("Estatura:", estatura, type(estatura))
print("Es estudiante:", es_estudiante, type(es_estudiante))

PROMEDIO_MINIMO = 6

materia = input("¿Qué materia cursas?")
calificacion = float(input("¿Qué calificación tienes?"))

suma = 8 + 2
resto = 10 % 3
potencia = 2 ** 3
mayor_de_edad = edad >= 18
aprobado = calificacion >= PROMEDIO_MINIMO and es_estudiante

print("Suma:", suma, "| Resto:", resto, "| Potencia:", potencia)
print("Mayor de edad:", mayor_de_edad)
print("Aprobado:", aprobado)