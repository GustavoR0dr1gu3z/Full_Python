# Excepciones
resultado = None 
a = 10
b = 0

# Division entre 0
try:
    resultado = a/b
except ZeroDivisionError as e:
    print("Ocurrio un error: {}, {}".format(e, type(e)))
except TypeError as e:
    print("Ocurrio un error: {}, {}".format(e, type(e)))
except  Exception as e:
    print("Ocurrio un error: {}, {}".format(e, type(e)))

print("Resultado: {} ".format(resultado))
print('Continuamos...')