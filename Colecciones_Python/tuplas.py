# Tupla mantiene el orden, pero no se modifica
frutas = ("Naranja", "Platano", "Guayaba")
print(frutas)

# Largo de la tupla
print(len(frutas))

# Accediendo a un elemento
print(frutas[0])

# Navegacion inversa
print(frutas[-1])

# Rangos
print(frutas[0:2]) # Excluyendo el 2

# Modificar un valor
frutasLista = list(frutas) # Convirtiendo a lista
frutasLista[1] = "Platanoo" # Lo modificamos
frutas = tuple(frutasLista) # Convertimos a tupla
print(frutas)

# Iterar una tupla
for frut in frutas:
    print(frut, end=', ')