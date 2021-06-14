class Monitor():
    contador_monitor = 0

    def __init__(self, marca, tamaño):
        Monitor.contador_monitor += 1
        self._id_monitor = Monitor.contador_monitor
        self.marca = marca
        self.tamaño = tamaño 
        