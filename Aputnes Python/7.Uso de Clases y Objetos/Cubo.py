class Cubo:
    def __init__(self, ancho, largo, alto):
        self.ancho = ancho
        self.largo = largo
        self.alto = alto
    
    def calcular_volumen(self):
        return self.ancho * self.largo * self.alto

ancho = int(input('Proporciona el ancho: '))
largo = int(input('Proporciona el largo: '))
alto = int(input('Proporciona el alto: '))

cubo1 = Cubo(ancho, largo, alto)
print(f'El volúmen del cubo es: {cubo1.calcular_volumen()}')