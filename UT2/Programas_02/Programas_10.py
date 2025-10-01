#Modifica el programa anterior par que pida en primer lugar el número de jugadores que
#van a jugar. Cada jugador irá jugando y el programa mostrará si ha ganado o no a la
#banca.
import random
num_banca = random.randrange(17, 22)
print("La banca ya tiene su puntuación.")
num_jugadores = int(input("¿Cuántos jugadores van a jugar? "))
for i in range(num_jugadores):
    print(f"Turno del jugador {i+1}:")
    puntuacion_jugador = 0
    while True:
        carta = int(input("¿Quieres sacar una carta (1-5)? Introduce 0 para plantarte: "))
        if carta == 0:
            break
        elif 1 <= carta <= 5:
            puntuacion_jugador += carta
            print(f"Tu puntuación actual es {puntuacion_jugador}.")
            if puntuacion_jugador > 21:
                print("¡Te has pasado de 21! Pierdes.")
                break
        else:
            print("Error: la carta debe estar entre 1 y 5.")
    if puntuacion_jugador <= 21:
        print(f"La banca tiene {num_banca} y tú tienes {puntuacion_jugador}.")
        if puntuacion_jugador > num_banca:
            print("¡Felicidades! Has ganado.")
        elif puntuacion_jugador == num_banca:
            print("Empate.")
        else:
            print("La banca gana. Has perdido.")
    print()  
print("Fin del juego.")
