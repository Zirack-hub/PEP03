class Monitor:
    contador_monitores = 0

    def __init__(self, marca, tamaño):
        Monitor.contador_monitores += 1
        self._id_monitor = Monitor.contador_monitores
        self._marca = marca
        self._tamaño = tamaño
    
    def __str__(self):
        return f'Monitor: [ID Monitor: {self._id_monitor}] [Marca: {self._marca}, Tamaño: {self._tamaño} pulgadas]'

if __name__ == '__main__':
    monitor1 = Monitor('Asus', 24)
    print(monitor1.__str__())
    monitor2 = Monitor('Samsung', 27)
    print(monitor2.__str__())