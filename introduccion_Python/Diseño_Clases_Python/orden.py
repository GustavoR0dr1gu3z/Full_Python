class Orden:
    contador_ordenes = 0


    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self.__id_orden = Orden.contador_ordenes
        self.__productos = productos

    