from numerosIdenticosException import NumerosIdenticosException

# Excepciones
resultado = None 

try:
    a = int(input("Primer numero: "))
    b = int(input("Segundo numero: "))
    # resultado = a/b

    # Raise nos permite lanzar o arrojar una exception
    raise 


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
    print("NO SE ARROJÓ NINGUNA EXCEPCION")   
# SIEMPRE SE EJECUTA SE CUMPLA O NO LA EXCEPCION
finally:
    print("EJECUCION DEL BLOQUE FINALLY")

print("Resultado: {} ".format(resultado))
print('Continuamos...')