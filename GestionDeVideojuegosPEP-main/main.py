# 3.1.6. Etapa 6 : Proyecto final:
    # Crea un menú interactivo que permita:
    #  Listar, buscar, filtrar, añadir, actualizar y eliminar videojuegos.
    #  Mostrar estadísticas generales.
    # Usa funciones para organizar el código.
    # Muestra siempre la información en un formato claro y atractivo.
    # El proyecto final debe tener la siguiente estructura.
    #  Los ficheros dentro de `etapas/` son el resultado de las etapas intermedias.
    #  Los módulos fuera de `etapas/` son los que se usan en main.py para construir el
    # programa final.
    #  El README debe indicar:
    # ◦ El reparto de roles y tareas.
    # ◦ Cómo ejecutar el programa.
from src.estadisticas import *
from src.busquedas import *
from src.catalogo import *
from src.utils_texto import *

def menu_principal():
    # --- Menú principal ---
    opcion = -7 # (entrar en el bucle)
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
                print("\n==== Catálogo ===")
                imprimir_juegos(catalogo)
            case "2":
                crear_juego(catalogo)
            case "3":
                leer_juego(catalogo)
            case "4":
                buscar_parcial(catalogo)
            case "5":
                filtrar_por_genero(catalogo)
            case "6":
                filtrar_por_rango(catalogo)
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
# --- Crear el Catálogo de Videojuegos ---
    catalogo = {}
    for titulo, anio, genero in juegos:
        clave = titulo.lower().replace(" ", "_")
        catalogo[clave] = {
            "titulo": titulo,
            "anio": int (anio),
            "genero": set(genero.split("/"))
        }

# ---- Mostrar Menú ----
    menu_principal()

