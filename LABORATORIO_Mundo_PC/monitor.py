class Monitor():
    contador_monitor = 0

    def __init__(self, marca, tamaño):
        Monitor.contador_monitor += 1
        self._id_monitor = Monitor.contador_monitor
        self.marca = marca
        self.tamaño = tamaño 


    def __str__(self):
        return "ID Monitor: {}, Marca: {}, Tamaño: {}".format(self._id_monitor, self._marca, self.tamaño)