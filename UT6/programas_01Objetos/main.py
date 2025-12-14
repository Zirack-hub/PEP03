from animales import *


try:
    animal1 = Animal("Kuma", "Tigre", 5, "A123", 300)
    animal2 = Animal("Carlos", "Venezolano", 19, "ES FACIL SOLO LEETE LOS APUNTES")
    animal1.saludar()
    animal1.cumplir_años()
    animal1.saludar()
    animal2.saludar()
    animal2.cumplir_años()
    animal1.chip = "Hola"
    animal2.pesito = 1
    del animal2.pesito
    animal2.saludar()

    print(Animal.contar_animales())
    
    if (Animal.es_mayor_de_edad(animal1.edad)):
        print ("Es mayor de edad")
    else:
        print ("Es menor de edad")

except Exception as e:
    print(e)