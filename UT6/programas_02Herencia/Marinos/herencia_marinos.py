from abc import ABC, abstractmethod
class AnimalMarino:

    def __init__(self, nombre):
        self.__nombre = nombre
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre_nuevo):
        if (isinstance(nombre_nuevo,str)):
            self.__nombre = nombre_nuevo
        else:    
            raise (TypeError("El nombre debe ser un string"))
    
    @abstractmethod
    def saluda(self):
        raise NotImplementedError
    
    @abstractmethod
    def sonido(self):
        raise NotImplementedError

class Delfin(AnimalMarino):

    def __init__(self, nombre):
        super().__init__(nombre)

    def saludar(self):
        print(f"Soy un delfin llamado {self.nombre}")
    
    def sonido(self):
        print("Click y silbidos, de vez en cuando se cagan en python y mysql")
    
class Tiburon(AnimalMarino):
    def __init__(self, nombre, tamañocora, tamañopulm):
        super().__init__(nombre)
        self.corazon = corazon(tamañocora)
        self.pulmon = pulmon(tamañopulm)

    def saludar(self):
        print(f"Soy un Tiburon llamado {self.nombre}")
    
    def sonido(self):
        print("No tiene un sonido audible característico ademas de LEVANTA FUKING PANZA")
    
    def nadar(self):
        self.corazon.latir()
        self.pulmon.respitar()

    
class corazon:
    def __init__(self, tamaño):
        self.tamaño = tamaño
    
    def latir (self):
        print("Estoy latiendo")

class pulmon:
    def __init__(self, tamaño):
        self.tamaño = tamaño
    
    def respitar (self):
        print("Estoy respitando")

