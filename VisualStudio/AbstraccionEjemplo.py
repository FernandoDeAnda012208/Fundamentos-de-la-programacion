#clase 
class Persona:
    def __init__(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion
#funciones
    def calificar(self):
        if self.calificacion >= 6:
            print("Estimado", self.nombre, "aprobaste con un promedio de", self.calificacion)
        else:
            print("Estimado", self.nombre, "reprobaste con un promedio de", self.calificacion)

        if self.calificacion <= 5.9:
            print("Oh no viejo")
        else:
            print("Im the goat")
#objetos

p1 = Persona("AuronPlay", 5.9)
p2 = Persona("Rubius", 7)
p3 = Persona("Willyrex", 9.5)
p4 = Persona("Vegetta777", 7.7)

p2.calificar()

