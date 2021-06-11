class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # __ es para variable privada
        self.__edad = edad

# METODOS GET Y SET -------NOMBRE--------
    def get_nombre(self):
        return self.__nombre
        
    def set_nombre(self, nombre):
        self.__nombre = nombre
# METODOS GET Y SET ---------EDAD----------
    def get_edad(self):
        return self.__edad

    def set_edad(self,edad):
        self.__edad = edad 

p1 = Persona("Gus", 21)
#print(p1.__nombre)  Marca error
print(p1.get_nombre())
print(p1.get_edad())
