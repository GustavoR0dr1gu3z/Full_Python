class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __add__(self, other):
        # Retorna el nombre del objeto y el nombre de other
        return self.nombre + other.nombre

# ob1 + ob2
# ob1.__add__(ob2)