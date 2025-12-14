class AnimalTerrestre:

    def __init__(self, nombre, edad, peso =60):
        self.__nombre = nombre
        self.__edad = edad
        self.__peso = peso
    
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if(isinstance(nuevo_nombre,str)):
            self.__id_chip = nuevo_nombre
            print("Se ha podido cambiar el nombre")
        else:
            raise (TypeError("El nombre debe ser un string"))
        
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, nueva_edad):
        if (nueva_edad > 0):
            self.__edad = nueva_edad
        else:
            raise(TypeError("La edad debe ser mayor que 0"))
    
    @property
    def peso(self):
        return self.__peso
    @edad.setter
    def edad(self, nuevo_peso):
        if (nuevo_peso > 0):
            self.__edad = nuevo_peso
        else:
            raise(TypeError("El peso debe ser mayor que 0"))
        
    def saluda(self):
        print(f"Hola soy {self.nombre} tengo {self.edad} años y peso {self.peso}Kgs")
    
    def __str__(self):
        return f"AnimalTerrestre(nombre={self.nombre}, edad={self.edad}, peso={self.peso})"
    
    def __lt__(self, otro):
        return self.edad > otro.edad
    
    def __add__(self, otro):
        return AnimalTerrestre(self.nombre + "-" + otro.nombre,self.edad + otro.edad, self.peso + otro.peso)    
    


class Mamifero(AnimalTerrestre):
    
    def __init__(self, nombre, edad, peso, gestacion_dias):
        super().__init__(nombre, edad, peso)
        self.__gestacion_dias = gestacion_dias
    
    @property
    def gestacion_dias(self):
        return self.__gestacion_dias
    @gestacion_dias.setter
    def gestacion_dias(self,nueva_gest_dias):
        if(nueva_gest_dias < 0):
            raise ValueError("Los dias deben ser mayores a 0")
        else:
            self.__gestacion_dias = nueva_gest_dias
    
    def saluda(self):
        print(f"Soy un mamimefero llamado {self.nombre}, tengo {self.edad} años  y mi gestación es de {self.__gestacion_dias}")

    def __str__(self):
         return f"Mamifero(nombre={self.nombre}, edad={self.edad}, peso={self.peso}, gestacion_dias={self.__gestacion_dias})"

class Ave(AnimalTerrestre):
    def __init__(self, nombre, edad, peso, puede_volar = True):
        super().__init__(nombre, edad, peso)
        self.__puede_volar = puede_volar
    
    @property
    def puede_volar(self):
        return self.__puede_volar
    
    @puede_volar.setter
    def puede_volar(self,nueva_puede_volar):
            self.__puede_volar=nueva_puede_volar

    def saluda(self):
        if (self.__puede_volar):
            print(f"Soy un ave llamado {self.nombre}, tengo {self.edad} años, que puede volar.")
        else:
            print(f"Soy un ave llamado {self.nombre}, tengo {self.edad} años, que no puede volar.")
    
    def __str__(self):
         return f"Ave(nombre={self.nombre}, edad={self.edad}, peso={self.peso}, puede_volar={self.__puede_volar})"

class Manada:
    def __init__(self, lista_animnales=None):
        self.__lista_animales = lista_animnales if lista_animnales is not None else []
    
    def agregar_animal(self, animal):
        if isinstance(animal, AnimalTerrestre):
            self.__lista_animales.append(animal)
        else:
            raise TypeError("Solo se pueden agregar animales")

    def __iter__(self):
        self._index =0
        return self
    
    def __next__(self):
        if self._index < len(self.__lista_animales):
            animal = self.__lista_animales[self._index]
            self._index += 1
            return animal
        else:
            raise StopIteration
    
