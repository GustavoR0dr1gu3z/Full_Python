# Excepciones
resultado = None 

try:
    a = int(input("Primer numero: "))
    b = int(input("Segundo numero: "))
    resultado = a/b
    '''    
except ZeroDivisionError as e:
    print("Ocurrio un error: {}, {}".format(e, type(e)))
except TypeError as e:
    print("Ocurrio un error: {}, {}".format(e, type(e)))
except ValueError as e:
    print("Ocurrio un error: {}, {}".format(e, type(e)))
    '''
# Bloque de exception general
except  Exception as e:
    print("Ocurrio un error: {}, {}".format(e, type(e)))
else:
    print("NO SE ARROJÓ NINGUNA EXCEPTION")    

print("Resultado: {} ".format(resultado))
print('Continuamos...')