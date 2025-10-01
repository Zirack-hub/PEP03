# Programa 08
# Escribe un programa que simule un juego en el que dos jugadores tiran dos dados.
# El que saque mayor puntuación total, gana. Si la puntuación total coincide,
# gana quien haya sacado el dado con el valor más alto. Si el valor más alto también coincide, empatan.

import random

# Tiradas de los jugadores
dado1_j1 = random.randrange(1, 7)
dado2_j1 = random.randrange(1, 7)
dado1_j2 = random.randrange(1, 7)
dado2_j2 = random.randrange(1, 7)

total_j1 = dado1_j1 + dado2_j1
total_j2 = dado1_j2 + dado2_j2

print(f"Jugador 1: {dado1_j1}, {dado2_j1} (Total: {total_j1})")
print(f"Jugador 2: {dado1_j2}, {dado2_j2} (Total: {total_j2})")

if total_j1 > total_j2:
    print("Gana Jugador 1")
elif total_j2 > total_j1:
    print("Gana Jugador 2")
else:
    if max(dado1_j1, dado2_j1) > max(dado1_j2, dado2_j2):
        print("Gana Jugador 1 por dado más alto")
    elif max(dado1_j2, dado2_j2) > max(dado1_j1, dado2_j1):
        print("Gana Jugador 2 por dado más alto")
    else:
        print("Empate")
