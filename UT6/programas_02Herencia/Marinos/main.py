from herencia_marinos import *


try:
    animal1 = Delfin("Flipper")
    animal2 = Tiburon("Yados", 5,6)
    animal3 = Delfin("LO PUTO CLE")
    animal4 = Tiburon("DRACUKASTI",5,6)

    animales=[animal1, animal2, animal3, animal4]
    for animal in animales:
        animal.saludar()
        animal.sonido()

    animal2.nadar()


except Exception as e:
    print(e)