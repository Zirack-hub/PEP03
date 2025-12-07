import src.utils_texto as utils_texto
# Funciones de Búsqueda y Flitrado

#-------- BÚSQUEDA POR COINCIDENCIA DE CARACTERES -------------------------------------------------
def buscar_parcial(catalogo):
    fragmento = input("Escribe parte del nombre del juego: ").lower()
    encontrados = []
    for datos in catalogo.values():
        if fragmento in datos["titulo"].lower():
            encontrados.append("+ "+datos["titulo"])
    if encontrados:
        print("Coincidencias:\n", '\n '.join(encontrados))
    else:
        print("No se encontraron juegos con ese fragmento.")


#-------- FILTRA POR GÉNERO -------------------------------------------------
def filtrar_por_genero(catalogo):
    buscar_genero = input("Género a buscar: ").lower()
    if buscar_genero not in catalogo:
        for datos in catalogo.values():
            for g in datos["genero"]:
                if buscar_genero == g.lower():
                    print(" + "+datos["titulo"], "-", ", ".join(datos["genero"]))
    else:
        print("Género NO encontrado D:")


#--------- FILTRA POR RANGO DE AÑOS ------------------------------------------------
def filtrar_por_rango(catalogo):
    inicio = int(input("Año inicial: "))
    fin = int(input("Año final: "))
    for datos in catalogo.values():
        if inicio <= datos["anio"] <= fin:
            print(" + "+datos["titulo"], "-", datos["anio"])
    
