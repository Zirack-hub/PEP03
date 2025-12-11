from DispositivoEntrada import Dispositivo_Entrada

class Raton(Dispositivo_Entrada):
    contador_ratones = 0

    def __init__(self, marca, tipo_entrada):
        Dispositivo_Entrada.__init__(self, marca, tipo_entrada)
        Raton.contador_ratones += 1
        self._id_raton = Raton.contador_ratones
    
    def __str__(self):
        return f'Raton: [ID Raton: {self._id_raton}] {Dispositivo_Entrada.__str__(self)}'

if __name__ == '__main__':
    raton1 = Raton('Logitech', 'Bluetooth')
    print(raton1.__str__())
    raton2 = Raton('Corsair', 'USB')
    print(raton2.__str__())