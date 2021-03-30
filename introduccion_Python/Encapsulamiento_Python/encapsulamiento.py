class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre  # __ es para variable privada

# METODOS GET Y SET
    def get_nombre(self):
        return self.__nombre
        
    def set_nombre(self, nombre):
        self.__nombre = nombre

p1 = Persona("Gus")
#print(p1.__nombre)  Marca error
print(p1.get_nombre())

p1.set_nombre("Gustavo")
print(p1.get_nombre())
