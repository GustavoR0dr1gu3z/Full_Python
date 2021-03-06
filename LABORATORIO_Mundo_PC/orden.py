class Orden:
    contador_orden = 0

    def __init__(self, computadoras):
        Orden.contador_orden += 1
        self._id_orden = Orden.contador_orden
        self._computadoras = computadoras

    def agregar(self, computadora):
        self._computadoras.append(computadora)

    def __str__(self):
        computadoras_str = ""
        for comp in self._computadoras:
            computadoras_str += comp.__str__() 
        return "Orden: {}\n\nComputadoras: {}\n\n".format(self._id_orden,computadoras_str)

