class Orden:
    contador_orden = 0

    def __init__(self, computadoras):
        Orden.contador_orden += 1
        self._id_orden = Orden.contador_orden
        self.computadoras = computadoras

    def agregar(self, computadora):
        self._computadoras.append(computadora)