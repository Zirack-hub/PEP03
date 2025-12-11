from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado


class Ordenador(Monitor, Raton, Teclado):
    contador_ordenadores = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Ordenador.contador_ordenadores += 1
        self._id_ordenador = Ordenador.contador_ordenadores
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton
    
    def __str__(self):
        return f'''
        {self._nombre} [ID Ordenador: {self._id_ordenador}] 
        {self._monitor}
        {self._teclado}
        {self._raton}
        '''

if __name__ == '__main__':
    monitor1 = Monitor('Asus', 24)
    teclado1 = Teclado('Logitech', 'USB')
    raton1 = Raton('Logitech', 'Bluetooth')
    ordenador1 = Ordenador('PC_1', monitor1, teclado1, raton1)
    print(ordenador1.__str__())

    monitor2 = Monitor('Samsung', 27)
    teclado2 = Teclado('Corsair', 'Bluetooth')
    raton2 = Raton('Corsair', 'USB')
    ordenador2 = Ordenador('PC_2', monitor2, teclado2, raton2)
    print(ordenador2.__str__())