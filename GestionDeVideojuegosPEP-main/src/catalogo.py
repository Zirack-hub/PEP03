import src.utils_texto as utils_texto
# Funionaledades CRUD

#-------- CREAR JUEGO -------------------------------------------------
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


#--------- LEER INFO DE JUEGO ------------------------------------------------
def leer_juego(catalogo):
    nombre = input("Introduce el título exacto: ").lower().replace(" ", "_")
    if nombre in catalogo:
        utils_texto.ver_toda_info(catalogo[nombre])
    else:
        print("No se encontró ese juego.")


#--------- ACTUALIZAR JUEGO ------------------------------------------------
def actualizar_juego(catalogo):
    clave = input("Título del juego a actualizar: ").lower().replace(" ", "_")
    if clave in catalogo:
        nuevo_anio = int(input("Actualizar Año: "))
        catalogo[clave]["anio"] = nuevo_anio
        nuevo_genero = input("Actualizar Genero: ")
        catalogo[clave]["genero"] = nuevo_genero
        utils_texto.ver_toda_info(catalogo[clave])
    else:
        print("No se encontró ese juego.")


#----------- ELIMINAR JUEGO ----------------------------------------------
def eliminar_juego(catalogo):
    clave = input("Título del juego a eliminar: ").lower().replace(" ", "_")
    if clave in catalogo:
        del catalogo[clave]
        print("Juego eliminado.")
    else:
        print("No se encontró ese juego.")
