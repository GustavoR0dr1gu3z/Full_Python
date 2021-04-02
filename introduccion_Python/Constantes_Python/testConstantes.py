# Para usar las constantes debemos crearla en archivos diferentes
# from constantes import *
from constantes import MI_CONSTANTE, Matematicas as mate


print(MI_CONSTANTE)
print(mate.PI)

MI_CONSTANTE = "Nuevo Valor"
print(MI_CONSTANTE)

mate.PI = 3.14
print(mate.PI)