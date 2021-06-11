class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return (self.base * self.altura)

base = int(input('Digite la base: '))
altura = int(input('Digite la altura: '))

rec = Rectangulo(base, altura)
print('EL area del rectangulo es: ',rec.calcularArea())
