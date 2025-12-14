class veterinario:
    def __init__ (self, nombre):
        self.__nombre = nombre
    
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    def revisar_animal(self, animal):
        print(f"Hola, soy el veterinarion {self.nombre} y estoy revisando el animal {animal.nombre}")
    
