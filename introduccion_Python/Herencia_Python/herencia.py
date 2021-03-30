class Persona:
    def __init__(self, nombre, edad): # Nombre, Edad
        self.nombre = nombre
        self.edad = edad

    def __str__(self): # Sobtr Escribir
        return "Nombre:" + self.nombre + " , edad: "+ str(self.edad)

class Empleado(Persona): # Empleado HEREDA de Persona
    def __init__(self, nombre, edad, sueldo): # Nombre, Edad, Sueldo
        super().__init__(nombre, edad)
        self.sueldo = sueldo


persona = Persona("Gustavo", 21)
print(persona)

empleado = Empleado("Gustavo",21,500)