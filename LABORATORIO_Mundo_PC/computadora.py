from teclado import Teclado
from raton import Raton
from monitor import Monitor

class Computadora: 
    contador_computadora = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadora +=1
        self._id_Computadora =  Computadora.contador_computadora
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton 

    def __str__(self):
        return "{}: {}\nMonitor: {}\nTeclado: {}\nRaton: {}".format(self._nombre, self._id_Computadora, self._monitor, self._teclado, self._raton)


if __name__ == '__main__':

# OBJETO 1
    t1 = Teclado('HP', 'USB')        
    r1 = Raton('HP', 'USB')
    m1 = Monitor('HP',15)

    c1 = Computadora('HP',m1,t1,r1)
    print(c1)

# OBJETO 2
    t2 = Teclado('HP', 'USB')        
    r2 = Raton('HP', 'USB')
    m2 = Monitor('HP',15)

    c2 = Computadora('HP',m2,t2,r2)
    print(c2)