# Programa 09
# Escribe un programa que simule el juego de piedra, papel o tijera.
# El usuario elige una opción y el programa genera una jugada aleatoria.
# Se muestra el resultado (gana, pierde o empata).

import random

print("Juego: Piedra, Papel o Tijera")
print("1. Piedra")
print("2. Papel")
print("3. Tijera")

usuario = int(input("Seleccione una opción (1, 2 o 3): "))
pc = random.randint(1, 3)

opciones = {1: "Piedra", 2: "Papel", 3: "Tijera"}

print(f"Tú elegiste: {opciones[usuario]}")
print(f"La computadora eligió: {opciones[pc]}")

if usuario == pc:
    print("Empate")
elif (usuario == 1 and pc == 3) or (usuario == 2 and pc == 1) or (usuario == 3 and pc == 2):
    print("¡Ganaste!")
else:
    print("Perdiste")
