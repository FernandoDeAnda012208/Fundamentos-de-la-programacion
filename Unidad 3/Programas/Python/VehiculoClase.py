class Vehiculo:
    def __init__(self, marca, modelo, year, color): #definimos el constructor de la clase y sus datos
            self.marca = marca
            self.modelo = modelo 
            self.year = year
            self.color = color 

    def mostrar_caracteristicas(self):
          print("Marca:", self.marca)
          print("Modelo:", self.modelo)
          print("Año:", self.year)
          print("Color:", self.color)