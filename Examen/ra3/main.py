from funciones import *

nombre=str(input("Introduce tu nombre:  "))
conocimiento=int(input("introduce tu conocimiento(1-5):   "))
energia=int(input("Introduce tu energia(1-10):   "))
nomEnem=str("")
conEnem=int(0)
magEnem=int(0)
nomEnem,conEnem,magEnem=generar_enemigo()
ataque= 0
ataEnem=0

print("         -------BATALLA MAGICA-------")
mostrar_jugador(nombre, conocimiento, energia)
print("")
print("")
mostrar_enemigo(nomEnem, conEnem, magEnem)
for i in range(3):
    ataque=ataque_jugador(conocimiento, energia)
    print(ataque)
    ataEnem=ataque_enemigo(conEnem, magEnem)
    print(ataEnem)
    if (ataque>ataEnem):
        print("Ha ganado el jugador")
        magEnem= magEnem-1
    if (ataque<ataEnem):
        print("Ha ganado el enemigo")
        energia= energia-1
    if(ataque==ataEnem):
        print("Han empatado")

if (energia>magEnem):
    print(f"{nombre} ha conseguido derrotar a la bestia {nomEnem}")
if(energia<magEnem):
    print(f"La bestia {nomEnem} ha conseguido derrotar al valiente {nombre}")
if(energia==magEnem):
    print(f"Despues de una ardua batalla ambos conendientes jugador{nombre} enemigo{nomEnem} terminan en tablas")

