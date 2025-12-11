from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
    
    def calcular_area(self):
        return f'[Área: {self.alto * self.ancho}] {FiguraGeometrica.__str__(self)} {Color.__str__(self)}'