import random


def generar_enemigo():
    nombres =["Hydra", "Kraken", "Minotauro", "Gorgona", "Titan"]
    nomEnem = random.choice(nombres)
    conEnem= random.randint(1, 10)
    magEnem= random.randint(1, 5)
    return nomEnem, conEnem, magEnem


def ataque_enemigo(conEnem, magEnem):
    aleatorio=random.randint(1,3)
    ataque=conEnem*magEnem*aleatorio
    return ataque
def mostrar_enemigo(nomEnem, conEnem, magEnem):
    print(f"Enemigo:  {nomEnem}")
    print(f"  Conocimiento:  {conEnem}")
    print(f"  Energia:       {magEnem}")