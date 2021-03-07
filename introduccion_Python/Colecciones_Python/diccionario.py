# Un diccionario está compuesto con valores de llave, valor
diccionario = {
    "IDE": "Integrated development Environment",
    "OOP": "Object Oriented Programming",
    "DBMS": "Database Management System"
}
# Imprimir diccionario
print(diccionario)

# Largo 
print(len(diccionario))

# Acceder a un elemento
print(diccionario["IDE"])

# Otra forma, mismo resultado
print(diccionario.get("IDE"))

# Modificando valores
diccionario["IDE"] = "integrated development environment"
print(diccionario)

# Iterando
for termino in diccionario:
    print(termino)

for termino in diccionario:
    print(diccionario[termino])    

for valor in diccionario.values():
    print(valor)

# Comprobar existencia de un elemento
    print("IDE" in diccionario)    
    print("Tierra" in diccionario)    

# Agregar nuevos elementos
diccionario["PK"] = "Primary Key"

print(diccionario)

# Remover elementos
diccionario.pop("DBMS")

# limpiar 
diccionario.clear()
print(diccionario)