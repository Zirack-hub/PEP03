# 3.1.5. Etapa 5: Diccionarios:
    #  Transforma tu colección en un diccionario donde:
    # ◦ La clave sea un identificador único ( título normalizado).
    # ◦ El valor sea otro diccionario con datos de la videojuego.
    # {
    #  "titulo": str,
    #  "anio": int,
    #  "genero": set
    # }
    #  Implementa operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre el catálogo
    # usando la clave.
    #  Implementa funciones de búsqueda:
    # ◦ Exacta por título.
    # ◦ Parcial (contenga un fragmento en el título).
    # ◦ Por género o rango de años.
    #  Calcula estadísticas:
    # ◦ Número total de videojuegos.
    # ◦ Conteo por género.
from tuplas import * # Lista de tuplas con los juegos

####################### FUNCIONES ############################
def crear_juego(catalogo):
    titulo = input("Título del nuevo juego: ")
    anio = int(input("Año: "))
    genero = input("Género(s) separados por '/': ")
    clave = titulo.lower().replace(" ", "_")
    if clave not in catalogo:
        catalogo[clave] = {
            "titulo": titulo,
            "anio": anio,
            "genero": set(genero.split("/"))
        }
        print("Juego añadido correctamente.")
    else:
        print("Ya existe un juego con ese nombre.")
#---------------------------------------------------------
def leer_juego(catalogo):
    nombre = input("Introduce el título exacto: ").lower().replace(" ", "_")
    if nombre in catalogo:
        print("Juego encontrado:", catalogo[nombre])
    else:
        print("No se encontró ese juego.")
#---------------------------------------------------------
def buscar_parcial(catalogo):
    fragmento = input("Escribe parte del nombre del juego: ").lower()
    encontrados = []
    for datos in catalogo.values():
        if fragmento in datos["titulo"].lower():
            encontrados.append(datos["titulo"])
    if encontrados:
        print("Coincidencias:", encontrados)
    else:
        print("No se encontraron juegos con ese fragmento.")
#---------------------------------------------------------
def buscar_por_genero(catalogo):
    buscar_genero = input("Género a buscar: ").lower()
    for datos in catalogo.values():
        for g in datos["genero"]:
            if buscar_genero == g.lower():
                print(datos["titulo"], "-", ", ".join(datos["genero"]))
#---------------------------------------------------------
def buscar_por_rango(catalogo):
    inicio = int(input("Año inicial: "))
    fin = int(input("Año final: "))
    for datos in catalogo.values():
        if inicio <= datos["anio"] <= fin:
            print(datos["titulo"], "-", datos["anio"])
#---------------------------------------------------------
def actualizar_juego(catalogo):
    clave = input("Título del juego a actualizar: ").lower().replace(" ", "_")
    if clave in catalogo:
        nuevo_anio = int(input("Actualizar Año: "))
        catalogo[clave]["anio"] = nuevo_anio
        nuevo_genero = input("Actualizar Genero: ")
        catalogo[clave]["genero"] = nuevo_genero
        print("Juego actualizado:", catalogo[clave])
    else:
        print("No se encontró ese juego.")
#---------------------------------------------------------
def eliminar_juego(catalogo):
    clave = input("Título del juego a eliminar: ").lower().replace(" ", "_")
    if clave in catalogo:
        del catalogo[clave]
        print("Juego eliminado.")
    else:
        print("No se encontró ese juego.")
#---------------------------------------------------------
def estadisticas(catalogo):
    print("\n=== Estadísticas ===")
    print("Número total de juegos:", len(catalogo))
    conteo_generos = {}
    for datos in catalogo.values():
        for g in datos["genero"]:
            if g not in conteo_generos:
                conteo_generos[g] = 1
            else:
                conteo_generos[g] += 1
    print("Conteo por género:")
    for g, cantidad in conteo_generos.items():
        print("-", g, ":", cantidad)
#  **************** FIN FUNCIONES ******************** 

####################### PROGRAMA PRINCIPA ############################
# --- Crear el Diccionario ---
catalogo = {}
for titulo, anio, genero in juegos:
    clave = titulo.lower().replace(" ", "_")
    catalogo[clave] = {
        "titulo": titulo,
        "anio": int (anio),
        "genero": set(genero.split("/"))
    }

def menu_principal():
    # --- Menú principal ---
    opcion = -7
    while opcion != 0 :
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Ver catálogo")
        print("2. Crear juego")
        print("3. Leer juego (búsqueda exacta)")
        print("4. Buscar parcial")
        print("5. Buscar por género")
        print("6. Buscar por rango de años")
        print("7. Actualizar juego")
        print("8. Eliminar juego")
        print("9. Ver estadísticas")
        print("0. Salir")
        opcion = input("Elige una opción: ")
        match opcion:
            case "1":
                for clave, datos in catalogo.items():
                    print(clave, ":", datos)
            case "2":
                crear_juego(catalogo)
            case "3":
                leer_juego(catalogo)
            case "4":
                buscar_parcial(catalogo)
            case "5":
                buscar_por_genero(catalogo)
            case "6":
                buscar_por_rango(catalogo)
            case "7":
                actualizar_juego(catalogo)
            case "8":
                eliminar_juego(catalogo)
            case "9":
                estadisticas(catalogo)
            case "0":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida.")

# ****** Programa Principal **********
if __name__ == "__main__":
    menu_principal()

