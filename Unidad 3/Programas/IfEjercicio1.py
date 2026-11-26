"""
-----Fundamentos de programación-----
-------Fernando de Anda Muñoz--------
-------------Modulo 3----------------

"""

calificacion = float(input("Escribe tu calificación: "))

if calificacion >= 11 or calificacion < 0:
    print("Calificación no valida")
else:
    if calificacion >= 9:
        print("Excelente")
    elif calificacion >= 8:
        print("Buen trabajo")
    elif calificacion >= 6:
        print("Aprobado")
    else:
        print("Reprobado")