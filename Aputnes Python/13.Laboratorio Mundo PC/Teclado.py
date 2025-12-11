from DispositivoEntrada import Dispositivo_Entrada

class Teclado(Dispositivo_Entrada):
    contador_teclados = 0

    def __init__(self, marca, tipo_entrada):
        Dispositivo_Entrada.__init__(self, marca, tipo_entrada)
        Teclado.contador_teclados += 1
        self._id_teclado = Teclado.contador_teclados
    
    def __str__(self):
        return f'Teclado: [ID Teclado: {self._id_teclado}] {Dispositivo_Entrada.__str__(self)}'

if __name__ == '__main__':
    teclado1 = Teclado('Logitech', 'USB')
    print(teclado1.__str__())
    teclado2 = Teclado('Corsair', 'Bluetooth')
    print(teclado2.__str__())