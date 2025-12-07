# Funciones Auxiliares

#-------- CREAR VIDEOJUEGOS -------------------------------------------------
juego1 = ("Expedition 33", "2025", "JRPG")
juego2 = ("Silksong", "2025", "Metroidvania")
juego3 = ("Monster Hunter World", "2018", "RPG/Acción")
juego4 = ("Elden Ring", "2022", "RPG/Acción")
juego5 = ("World Of Warcraft", "2006", "MMO/RPG")

juegos = [juego1,juego2,juego3,juego4,juego5]


#-------- PINTAR VIDEOJUEGOS -------------------------------------------------
def imprimir_juegos(catalogo):
    for i in catalogo:
        print(" + "+str(catalogo[i]["titulo"])+"  "+str(" ".join(catalogo[i]["genero"]))+"  "+str(catalogo[i]["anio"]))

#-------- MUESTRA INFO COMPLETA DE UN VIDEOJUEGO -------------------------------------------------      
def ver_toda_info(jueguito):
    genero = ' '.join(jueguito["genero"])
    print("---------------------\nJuego encontrado:\n + Titulo: ", jueguito["titulo"],"\n + Año: ",jueguito["anio"],"\n + Géneros: ",genero)