from cuadrado import Cuadrado

cuadrado = Cuadrado(5,"Rojo")

print("El area del cuadrado es: ",cuadrado.area())
print("El color del cuadrado es: "+cuadrado.color)

# Method Resolution Order, orden en que se ejecutan las clases
print(Cuadrado.mro())
