class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __add__(self, other):
        # Retorna el nombre del objeto y el nombre de other
        return self.nombre + other.nombre


    def __sub__(self, other):
        return self.edad - other.edad

p1 = Persona('Gus',22)
p2 = Persona('Tavo',12)

print('Nombre concatenado: ',p1+p2)
print('Resta de edades: ',p1-p2)
# ob1 + ob2
# ob1.__add__(ob2)