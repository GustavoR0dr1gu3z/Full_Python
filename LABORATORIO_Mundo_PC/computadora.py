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
        return "NombreComputadora: {}, ID_Computadora: {}\nMonitor: {}\nTeclado: {}\nRaton: {}".format(self._nombre, self._id_Computadora, self._monitor, self._teclado, self._raton)