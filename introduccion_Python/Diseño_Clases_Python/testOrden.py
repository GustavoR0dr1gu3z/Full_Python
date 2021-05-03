from producto import Producto
from orden import Orden

producto1 = Producto("Camisa", 100.00)
producto2 = Producto("Pantalon",200.00)
producto3 = Producto("Calcetines",50.00)
producto4 = Producto("Sueter",300.00)

productos = [producto1, producto2]

orden1 = Orden(productos)
print(orden1)

productos.append(producto3)
orden2 = Orden(productos)
print(orden2)

orden3 = Orden(productos)
orden3.agregar_producto(producto4)
print(orden3)

