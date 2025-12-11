from Orden import Orden
from Ordenador import Ordenador
from Monitor import Monitor
from Teclado import Teclado
from Raton import Raton

monitor1 = Monitor('Asus', 24)
teclado1 = Teclado('Logitech', 'USB')
raton1 = Raton('Logitech', 'Bluetooth')
ordenador1 = Ordenador('PC_1', monitor1, teclado1, raton1)

monitor2 = Monitor('Samsung', 27)
teclado2 = Teclado('Corsair', 'Bluetooth')
raton2 = Raton('Corsair', 'USB')
ordenador2 = Ordenador('PC_2', monitor2, teclado2, raton2)

monitor3 = Monitor('MSI', 27)
teclado3 = Teclado('Logitech', 'Bluetooth')
raton3 = Raton('Razor', 'USB')
ordenador3 = Ordenador('PC_3', monitor3, teclado3, raton3)

ordenadores1 = [ordenador1, ordenador2]
orden1 = Orden(ordenadores1)
orden1.agregar_ordenador(ordenador3)
print(orden1.__str__())