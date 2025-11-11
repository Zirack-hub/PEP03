import random
vidasJug=3
contador = 0
puntuacion =0
nivel =0
while vidasJug > 0:

    cartaJugador=0
    cartaOrdenador=0
    print("Total de vidas:", vidasJug)
    eleccion=0

    while (eleccion<1 or eleccion>=4):
        eleccion=int(input("Introduce 1 para fuerza 2 para precision y 3 para riesgo"))
        
    if(eleccion == 1):
        cartaJugador=random.randint(5, 10)
        print("Has elegido fuerza y has sacado un: ", cartaJugador)
        cartaOrdenador=random.randint(3,10)
    if(eleccion==2):
        cartaJugador=random.randint(3,8)
        print("Has elegido precision y has sacado un: ", cartaJugador)
        cartaOrdenador=random.randint(2,9)
    if(eleccion==3):
        cartaJugador=random.randint(1,10)
        print("Has elegido riesgo y has sacado un: ", cartaJugador)
        cartaOrdenador=random.randint(1,8)
        
    if(cartaJugador>cartaOrdenador):
        print(f"El jugador ha ganado con un {cartaJugador} contra un {cartaOrdenador}")
        puntuacion=puntuacion+1

    if(cartaJugador<cartaOrdenador):
        print(f"El jugador ha perdido con un {cartaJugador} contra un {cartaOrdenador}")
        vidasJug=vidasJug-1

    if(cartaJugador==cartaOrdenador):
        print(f"El jugador ha empatado con un {cartaJugador} contra un {cartaOrdenador}")

    if puntuacion==3:
        nivel=nivel+1
        puntuacion=0
        if vidasJug<3:
            vidasJug=vidasJug+1

print(f"El jugador ha terminado la partida con nivel {nivel} y un total de {puntuacion} puntos de experiencia para el siguiente nivel")                
            


    
    
    
    
