class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Modificar los valores
Persona.nombre = "Gustavo"
Persona.edad = 21

# Acceder a los valores
print(Persona.nombre, Persona.edad)

# Creacion de un objeto
persona = Persona("Guss", 22)
print(persona.nombre, persona.edad)

persona2 = Persona("Tavoo", 23)
print(persona2.nombre, persona2.edad)
