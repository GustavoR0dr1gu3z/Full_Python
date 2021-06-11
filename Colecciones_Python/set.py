# Set es una colección sin orden, y sin indices, ni 
# elementos repetidos, y estos tampoco se modifican
# pero si agregar nuevos o eliminar

planetas = {"Marte", "Jupiter", "Venus"}
print(planetas)

# Largo
print(len(planetas))

# Revisar si un elemento está presente
print("Marte" in planetas)
print("Tierra" in planetas)

# Agregar elementos
planetas.add("Tierra")
print(planetas)

# Eliminar elementos SI arroja excepcion
planetas.remove("Tierra")
print(planetas)

# Eliminar con discard NO arroja excepcion
planetas.discard("Jupiter")
print(planetas)

# Limpiar el set 
planetas.clear()
print(planetas)