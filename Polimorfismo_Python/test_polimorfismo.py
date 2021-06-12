from empleado import Empleado 
from gerente import Gerente 

def imprimir_detalles(objeto):
    print(objeto)
    print(type(objeto))


empleado = Empleado('Gustavo',5000)
imprimir_detalles(empleado)