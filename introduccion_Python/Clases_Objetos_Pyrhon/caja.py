class Caja():
    def __init__(self, alto, ancho, largo):
        self.alto = alto
        self.ancho = ancho
        self.largo = largo

    def calcularVolumen(self):
        return (self.alto * self.ancho * self.largo)

alto = int(input('Digite el alto: '))
ancho = int(input('Digite el ancho: '))
largo = int(input('Digite el largo: '))

caja = Caja(alto, ancho, largo)        
print('El volumen de la caja es: ',caja.calcularVolumen())