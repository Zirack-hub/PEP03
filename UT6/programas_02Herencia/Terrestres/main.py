from herencia_animales import *
from veterinario import *
from reservanatural import *

try:
    animal1 = AnimalTerrestre("Kuma", 5, 300)
    animal2 = AnimalTerrestre("Carlos", 19)
    animal3 = Mamifero("Jefesito", 19, 60, 90)
    animal4 = Ave("Alvaro", 4, 3, False)
    animal4 = Ave("Alvaro", 4, 3, False)
    animal6 = AnimalTerrestre("Titan", 2, 150)
    veterinario1 = veterinario("Clefo")
    veterinario1.revisar_animal(animal1)


    lista = [animal3, animal4]
    for animal in lista:
        animal.saluda()
    
    print(animal1<animal2)
    animal5 = animal1+animal2
    animal5.saluda()
    manada = Manada([animal1, animal2, animal3, animal4])
    manada.agregar_animal(animal6)

    for animal in manada:
        print(animal)

    print("LISTA DE ANIMALES EN LA RESERVA NATURAL:")
    reserva = ReservaNatural([animal1, animal2, animal3, animal4])
    
    for animal in reserva:
        print(animal)
    
except Exception as e:
    print(e)