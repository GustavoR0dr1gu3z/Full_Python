print("Digite los siguientes datos del libro")
nombre = input("Nombre del Libro: ")
id=int(input("Id del Libro: "))
precio = float(input("Precio del Libro: "))
envio = input("Es gratuito o no (True/False): ")


if(envio == 'True' or envio == 'true'):
    envio = True
elif (envio == 'False' or envio =='false'): 
    envio = False    
else:
    envio = "Valor incorrecto, únicamente True/False"
    
    
print("El Nombre es: {}, con un ID: {}, un Precio: {}".format(nombre, id, precio))    
print("¿Con envio Gratuito?: ",envio)
