#Escribe un programa para jugar a una versión muy simplificada del black jack. En primer
#lugar el ordenador obtendrá un número aleatorio entre 17 y 21 (está será su jugada). A
#continuación el jugador ira sacando cartas (con valores entre 1 y 5), que se irán sumando
#para obtener su puntuación, hasta que el quiera. Si se pasa de 21 pierde, si obtiene una
#puntuación igual o menor que la banca pierde, y si obtiene una puntuación superior a la
#banca gana.
import random
num_banca = random.randrange(17, 22)
puntuacion_jugador = 0
print("La banca ya tiene su puntuación.")
while True:
    carta = int(input("¿Quieres sacar una carta (1-5)? Introduce 0 para plantarte: "))
    if carta == 0:
        break
    elif 1 <= carta <= 5:
        puntuacion_jugador += carta
        print(f"Tu puntuación actual es {puntuacion_jugador}.")
        if puntuacion_jugador > 21:
            print("¡Te has pasado de 21! Pierdes.")
            exit()
    else:
        print("Error: la carta debe estar entre 1 y 5.")
print(f"La banca tiene {num_banca} y tú tienes {puntuacion_jugador}.")
if puntuacion_jugador > num_banca:
    print("¡Felicidades! Has ganado.")
elif puntuacion_jugador == num_banca:
    print("Empate.")
else:
    print("La banca gana. Has perdido.")

