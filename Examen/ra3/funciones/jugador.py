import random


def ataque_jugador(conocimiento, energia):
    aleatorio = random.randint(1,3)
    ataque = conocimiento*energia*aleatorio
    return ataque

def mostrar_jugador(nombre, conocimiento, energia):
    print(f"Jugador:  {nombre}")
    print(f"  Conocimiento:  {conocimiento}")
    print(f"  Energia:       {energia}")