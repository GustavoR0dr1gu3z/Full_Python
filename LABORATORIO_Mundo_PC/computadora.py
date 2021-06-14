class Computadora: 
    contador_computadora = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadora +=1
        self._id_Computadora =  Computadora.contador_computadora
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton 