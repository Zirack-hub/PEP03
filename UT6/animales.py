class Animal:
    __numero_animales = 0

    def __init__(self, nombre, especie, edad, id_chip, peso = 60):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.__id_chip = id_chip
        self.__peso = peso
        Animal.__numero_animales = Animal.__numero_animales +1

    @classmethod
    def contar_animales(cls):
        return cls.__numero_animales
    
    @staticmethod
    def es_mayor_de_edad(edad):
        return (edad  >=2 )

    @property
    def chip(self):
        return self.__id_chip
    
    @chip.setter
    def chip(self, nuevo_id_chip):
        if (isinstance(nuevo_id_chip,str)):
            self.__id_chip = nuevo_id_chip
            print ("Se ha cambiado el chip")
        else:    
            raise (TypeError("El id_chip debe ser un string"))
        
    @property
    def peso(self):
        return self.__peso
    
    @peso.setter
    def peso(self,nuevo_peso):
        if (nuevo_peso < 0):
            raise ValueError("El peso debe ser positivo")
        else:
            self.__peso=nuevo_peso
        
    def saludar(self):
        print(f"Soy un {self.especie} llamado {self.nombre} y tengo {self.edad} años ")

    def cumplir_anios(self):
        self.edad = self.edad +1

try:
    print(Animal.contar_animales())
    animal1 = Animal("Kuma", "tigre", 10, "a123", 100)
    print(Animal.contar_animales())
    animal2 = Animal("Miu", "gato", 5, "a234", 25)
    print(Animal.contar_animales())

    
    print(animal1.chip)
    animal1.chip = "a5222"
    print(animal1.chip)
    animal1.peso = 99
    print(animal1.peso)

    animal1.edad = 30
    animal1.cumplir_anios()
    if (Animal.es_mayor_de_edad(animal1.edad)):
        print ("Es mayor de edad")
    else:
        print ("Es menor de edad")



except Exception as e:
    print(e)
    


        
