juego1 = ("Expedition 33", "2025", "JRPG")
juego2 = ("Silksong", "2025", "Metroidvania")
juego3 = ("Monster Hunter World", "2018", "RPG/Acción")
juego4 = ("Elden Ring", "2022", "RPG/Acción")
juego5 = ("World Of Warcraft", "2006", "MMO/RPG")

juegos = [juego1,juego2,juego3,juego4,juego5]

def imprimir_juegos():
    for i in range(len(juegos)):
        for j in range(len(juegos[i])):
            print(juegos[i][j], end=" ")
        print("\n")

if __name__ == "__main__":
    imprimir_juegos()