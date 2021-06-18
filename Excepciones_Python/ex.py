# Excepciones
resultado = None 
a = 10
b = 0

# Division entre 0
try:
    resultado = a/b
except Exception as e:
    print("Dividion entre cero, no se puede: {}".format(e))

print("Resultado: {} ".format(resultado))