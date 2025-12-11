from Ordenador import Ordenador
from Monitor import Monitor
from Teclado import Teclado
from Raton import Raton

class Orden(Ordenador):
    contador_ordenes = 0

    def __init__(self, ordenadores):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._ordenadores = ordenadores
    
    def agregar_ordenador(self, ordenador):
        self._ordenadores.append(ordenador)

    def __str__(self):
        ordenadores_str = ''
        for ordenador in self._ordenadores:
            ordenadores_str += ordenador.__str__()
        return f'''
        [Orden: {self._id_orden}]

        Ordenadores: {ordenadores_str}
        '''

if __name__ == '__main__':

    monitor1 = Monitor('Asus', 24)
    teclado1 = Teclado('Logitech', 'USB')
    raton1 = Raton('Logitech', 'Bluetooth')
    ordenador1 = Ordenador('PC_1', monitor1, teclado1, raton1)

    monitor2 = Monitor('Samsung', 27)
    teclado2 = Teclado('Corsair', 'Bluetooth')
    raton2 = Raton('Corsair', 'USB')
    ordenador2 = Ordenador('PC_2', monitor2, teclado2, raton2)

    ordenadores1 = [ordenador1, ordenador2]
    orden1 = Orden(ordenadores1)
    print(orden1.__str__())