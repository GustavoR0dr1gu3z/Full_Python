class Orden:
    contador_ordenes = 0


    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self.__id_orden = Orden.contador_ordenes
        self.__productos = productos

    def agregar_producto(self, producto):
        pass

    def calcular_total(self):
        pass

    def __str__(self):
        # Listado de productos de productos
        productos_str = ""
        for producto in self.__productos:
            productos_str += producto.__str__()+" | " # Concatenamos con la clase str de producto.py
        return "Orden: "+str(self.__id_orden)+", Productos: "+productos_str

