# Excepciones
resultado = None 
a = '10'
b = 0

# Division entre 0
try:
    resultado = a/b
except ZeroDivisionError as e:
    print("Ocurrio un error: {}".format(e))
except TypeError as e:
    print("Ocurrio un error: {}".format(e))


print("Resultado: {} ".format(resultado))