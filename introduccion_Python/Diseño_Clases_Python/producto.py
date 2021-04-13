class Producto:
    contador_productos = 0

    def __init__(self, nombre, precio):
        Producto.contador_productos += 1 # Contador para cada vez que agregamos un objeto
        self.__id_producto = Producto.contador_productos # El ID, será el contador
        self.__nombre = nombre
        self.__precio = precio

    def __str__(self):
        return  "ID Producto: "+self.__id_producto+", Nombre: "+self.__nombre+", Precio: "+str(self.__precio)