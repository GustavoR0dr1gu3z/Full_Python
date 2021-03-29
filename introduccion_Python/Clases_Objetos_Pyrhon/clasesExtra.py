class Persona:
    def __init__(self, nombre, edad, *varios, **diccionario):
        self.nombre = nombre
        self.edad = edad
        self.varios = varios
        self.diccionario = diccionario

    def desplegar(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)
        print("Valores: ",self.varios)
        print("Diccionario: ",self.diccionario)    

p1 = Persona('Gustavo', 21) 
p2 = Persona('Rodriguez',21, 1,2,3)
p3 = Persona('Calzada', 21, 1,2,3, m="Manzana", p="Pera", j="Jicama") 

p1.desplegar()
p2.desplegar()
p3.desplegar()