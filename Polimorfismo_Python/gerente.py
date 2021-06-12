from empleado import Empleado 

class Gerente(Empleado):

    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.departamento = departamento

    def __str__(self):
        return 'Gerente {}, Departamento: {}'.format(super().__str__(), self.departamento)


    def mostrar_detalles(self):
        return self.__str__()