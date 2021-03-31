from figura_g import FiguraGeometrica
from color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lados, color):
        FiguraGeometrica.__init__(self, lados, lados)
        Color.__init__(self, color)

    def area(self):
        return self.alto * self.ancho