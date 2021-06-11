condicion = True

print("Condicion Verdadera ") if condicion else print("Condicion Falsa")

if condicion == True:
    print("La condicion es verdadera")  
else:
    print("La condicion es falsa")
    
    
numero = int(input("Digite un numero entre 1 y 3: "))
if numero == 1:
    numeroTexto = "Numero Uno"
elif numero == 2:
    numeroTexto = "Numero Dos"
elif numero == 3:
    numeroTexto = "Numero Tres"
else:
    numeroTexto = "Numero Fuera de Rango"
    
print("Numero proporcionado: {}".format(numeroTexto))

    
