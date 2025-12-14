from herencia_animales import AnimalTerrestre
class ReservaNatural:
    def __init__(self, lista_animnales=None):
        self.__lista_animales = lista_animnales if lista_animnales is not None else []

    def añadir_animal(self, animal):
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
    