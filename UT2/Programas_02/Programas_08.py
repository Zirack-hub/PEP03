#Escribe un programa para jugar a adivinar un número. En primer lugar la aplicación
#solicita genera un número aleatorio entre 1 y 20. A continuación va pidiendo números y va
#respondiendo si el número a adivinar es mayor o menor que el introducido. El programa
#termina cuando se acierta el número.
#Puedes generar el número usando la función random.randrange(1, 21) para
#obtener un número aleatorio entre 1 y 20 (para ello debes poner import random al inicio
#del programa).
#Mejora el programa de forma que el usuario tenga solo 3 intentos.
import random
num_aleatorio = random.randrange(1, 21)
intentos = 3
print("Tienes 3 intentos para adivinar el número entre 1 y20.")
while intentos > 0:
    num_usuario = int(input("Introduce tu número: "))
    if num_usuario < num_aleatorio:
        print("El número a adivinar es mayor.")
    elif num_usuario > num_aleatorio:
        print("El número a adivinar es menor.")
    else:
        print("¡Felicidades! Has adivinado el número.")
        break
    intentos -= 1
    if intentos == 0:
        print(f"Lo siento, has agotado tus intentos. El número era {num_aleatorio}.")
    else:
        print(f"Te quedan {intentos} intentos.")

