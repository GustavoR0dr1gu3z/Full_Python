class Vehiculo:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def __str__(self):
        return "Vehiculo marca: "+self.marca+", modelo: "+str(self.modelo)+", color: "+self.color 

class Coche(Vehiculo):
    def __init__(self, marca, modelo, color, combustible):
        super().__init__(marca, modelo, color)
        self.combustible = combustible

    def __str__(self):
        return super().__str__()+", combustible: "+self.combustible

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, color, tamaño):
        super().__init__(marca, modelo, color)
        self.tamaño = tamaño
    
    def __str__(self):
        return super().__str__()+", tamaño: "+self.tamaño


coche = Coche("Nissan",2019,"Rojo","Gasolina")
print("Coche: \n")
print(coche)

bici = Bicicleta("Nosejaja", 2021, "Rojo", "Grandota")
print("\n\nBicicleta: \n")
print(bici)
