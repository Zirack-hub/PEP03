# 3.1.4. Etapa 4: Conjuntos:
    #  Crea un conjunto con todos los géneros de tus videojuegos.
    #  Añade nuevos géneros y elimina otros.
    #  Pregunta al usuario su género favorito y verifica si está en tu conjunto.
    #  Crea otro conjunto con los géneros de un amigo y encuentra:
    # ◦ Unión: todos los géneros entre ambos.
    # ◦ Intersección: géneros en común.
    # ◦ Diferencia : géneros que tú tienes y tu amigo no.

generos = {"Metroidvania","RPG/Acción","JRPG","Supervivencia","Supercell"}

generos.discard("Supervivencia")
generos.discard("Supercell")
generos.add("MMO/RPG")

if __name__ == "__main__":
    respuesta = input("Cual es tu género de juego favorito? ")

    if (respuesta in generos):
        print("SI tenemos tu genero favorito :D")
    else:
        print("NO tenemos tu genero favorito >:O")

generosAmigo = {"Metroidvania","JRPG","RPG","MMO/RPG","Anime"}

union = generos | generosAmigo
interseccion = generos & generosAmigo
diferencia = generos - generosAmigo
