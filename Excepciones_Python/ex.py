# Excepciones


# Division entre 0
try:
    10/0
except Exception as e:
    print("Dividion entre cero, no se puede: {}".format(e))