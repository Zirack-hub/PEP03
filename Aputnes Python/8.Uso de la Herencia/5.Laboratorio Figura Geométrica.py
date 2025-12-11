from FiguraGeometrica import FiguraGeometrica
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

# No se puede instanciar una clase abstracta
# figura = FiguraGeometrica()

print('Creación Objeto Cuadrado'.center(50,'-'))
cuadrado1 = Cuadrado(lado=5, color='rojo')
cuadrado1.alto = -10
cuadrado1.ancho = -10
print(f'Cuadrado: {cuadrado1.calcular_area()}')

print('Creación Objeto Rectángulo'.center(50,'-'))
rectangulo1 = Rectangulo(alto=4, ancho=5, color='rojo')
rectangulo1.alto = 15
rectangulo1.ancho = 15
print(f'Rectángulo: {rectangulo1.calcular_area()}')

print(Cuadrado.mro())
print(Rectangulo.mro())