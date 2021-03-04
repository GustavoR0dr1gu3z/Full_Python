#Creando la lista
nombreLista = ["Gus","Mich","Mari","Renata"]
# Imprimir la lista
print(nombreLista)
# Para saber el largo de la lista
print(len(nombreLista))
# Acceder a un elemento
print(nombreLista[0])
# Navegacion inversa
print(nombreLista[-1])

# Imprimir rango
print(nombreLista[0:2]) # Sin incluir el 2
# Imprimir los elementos de inicio hasta i
print(nombreLista[:3]) #Sin incluir el 3
# Imprimir los elementos hasta el final
print(nombreLista[1:])
# Cambiar los elementos de una lista
nombreLista[3]="Reni"
print(nombreLista)
# Iterar la lista
for i in nombreLista:
    print(i)
# Revisar si existe un elemento dentro de la lista
if "Renid" in nombreLista:
    print("Reni si existe en la lista")
else:
    print("El elemento buscado no existe en la lista"        )

