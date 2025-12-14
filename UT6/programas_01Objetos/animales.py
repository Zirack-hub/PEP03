class Animal:
    numero_animales = 0

    def __init__(self, nombre, especie, edad, id_chip, peso =60):
        self.nombre = nombre
        self.especie = especie
        self.__edad = edad
        self.__id_chip = id_chip
        self.__peso = peso
        Animal.numero_animales += 1

    @classmethod
    def contar_animales(cls):
        return cls.numero_animales


    def saludar(self):
        if hasattr(self, "_Animal__peso"):
            print(f"Hola soy {self.nombre} y soy un {self.especie}, tengo {self.edad} años chip: {self.chip} y mi peso es de {self.pesito}kg")
        else:
            print(f"Hola soy {self.nombre} y soy un {self.especie}, tengo {self.edad} años chip: {self.chip}")

    
    def cumplir_años(self):
        self.edad += 1


    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, nuevo_peso):
        if(isinstance(nuevo_peso,int)):
            self.__edad = nuevo_peso
            print("Se ha cambiado la edad")
        else:
            raise (TypeError("La edad debe ser un int"))
    
    @property
    def pesito(self):
        return self.__peso
    @pesito.setter
    def pesito(self, nuevo_peso):
        if(isinstance(nuevo_peso,int)):
            self.__peso = nuevo_peso
            print("Se ha cambiado el peso")
        else:
            raise (TypeError("El peso debe ser un int"))
        
    @pesito.deleter
    def pesito(self):
        del self.__peso
        print("El peso ha sido eliminado")
    
    @property
    def chip(self):
        return self.__id_chip
    
    @chip.setter
    def chip(self, nuevo_id_chip):
        if(isinstance(nuevo_id_chip,str)):
            self.__id_chip = nuevo_id_chip
            print("Se ha podido cambiar el chip")
        else:
            raise (TypeError("El id_chip debe ser un string"))
    
    @staticmethod
    def es_mayor_de_edad(edad):
        
        return (edad >= 9)
