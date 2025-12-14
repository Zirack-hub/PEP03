from herencia_marinos import *


try:
    animal1 = Delfin("Flipper")
    animal2 = Tiburon("Yados")
    animal3 = Delfin("LO PUTO CLE")
    animal4 = Tiburon("DRACUKASTI")

    animales=[animal1, animal2, animal3, animal4]
    for animal in animales:
        animal.saludar()
        animal.sonido()



except Exception as e:
    print(e)