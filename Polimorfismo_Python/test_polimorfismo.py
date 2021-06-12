from empleado import Empleado 
from gerente import Gerente 

def imprimir_detalles(objeto):
    print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalles())
    # Si es objeto que estamos apuntando es de tipo Gerente, entonces imprime el departamento
    if isinstance(objeto, Gerente):
        print(objeto.departamento)


empleado = Empleado('Gustavo',5000)
imprimir_detalles(empleado)

gerente = Gerente('Karla',6000, 'Sistemas')
imprimir_detalles(gerente)