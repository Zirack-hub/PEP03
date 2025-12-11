from Cuadrado import Cuadrado

cuadrado1 = Cuadrado(5, 'rojo')
print(f'Cáculo área cuadrado: {cuadrado1.calcular_area()}')

# "MRO - Method Resolution Order" sirve para saber el orden de resolución del metodo
print(Cuadrado.mro())