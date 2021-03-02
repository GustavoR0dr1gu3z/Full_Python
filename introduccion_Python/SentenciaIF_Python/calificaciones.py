valor = float(input("Digite un valor entre 0 y 10: "))

nota = None
if valor >= 9 and valor <= 10:
    nota = "A"
elif valor >= 8 and valor < 9:
    nota = "B"
elif valor >= 7 and valor < 8:
    nota = "C"
elif valor >= 6 and valor < 7:
    nota = "D"
elif valor >= 0 and valor < 6:
    nota = "F"
else:
    nota = "Un Valor desconocido"

print("Su nota es: ",nota)
