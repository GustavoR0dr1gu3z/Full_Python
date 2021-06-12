class Empleado:

    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo


    def __str__(self):
        return 'Empleado: {}, Sueldo: {}'.format(self.nombre, self.sueldo)