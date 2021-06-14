class Monitor():
    contador_monitor = 0

    def __init__(self, marca, tamaño):
        Monitor.contador_monitor += 1
        self._id_monitor = Monitor.contador_monitor
        self._marca = marca
        self._tamaño = tamaño 


    def __str__(self):
        return "ID Monitor: {}, Marca: {}, Tamaño: {}".format(self._id_monitor, self._marca, self._tamaño)


# Pruebas de la clase 
if __name__ == '__main__':
    mon1 = Monitor('HP','15')
    print(mon1)