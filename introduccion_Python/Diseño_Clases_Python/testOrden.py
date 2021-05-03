from producto import Producto
from orden import Orden

# CREACION DE OBJETOS (PRODUCTOS)
producto1 = Producto("Camisa", 100.00)
producto2 = Producto("Pantalon",200.00)
producto3 = Producto("Calcetines",50.00)
producto4 = Producto("Sueter",300.00)

# SE AÑADEN A UNA LISTA ALGUNOS PRODUCTOS
productos = [producto1, producto2]

# SE CREA LA ORDEN UNO CON 2 PRODUCTOS
orden1 = Orden(productos)
# SE IMPRIME LA ORDEN
print(orden1)

# SE AÑADE OTRO PRODUCTO
productos.append(producto3)
# SE CREA LA ORDEN DOS CON OTRO PRODUCTO MAS
orden2 = Orden(productos)
# SE IMPRIMEN
print(orden2)

# SE CREA LA ORDEN 3
orden3 = Orden(productos)
# SE AGREGA EL PRODUCTO 4
orden3.agregar_producto(producto4)
# SE IMPRIME
print(orden3)




