from abc import ABC, abstractmethod
class Producto(ABC):

    def __init__(self, nombre, lista_precios):
        self.nombre = nombre
        self.lista_precios = lista_precios
    
    @property
    def nombre(self):
        return self.nombre
    @nombre.setter
    def nombre(self):
        return self.nombre
    
    @property
    def lista_precios(self):
        return self.lista_precios()
    
    def añadir_precio(self, precio):
        if precio>0:
            self.precios.append(precio)
        else:
            print("El precio no debe ser negativo")

class disco_duro(Producto):

    def __init__(self, nombre, lista_precios, tipo):
        super().__init__(nombre, lista_precios = [])
        self.tipo = tipo


class memoria(Producto):
    def __init__(self, nombre, lista_precios, capacidad):
        super().__init__(nombre, lista_precios = [])
        self.capacidad = capacidad
