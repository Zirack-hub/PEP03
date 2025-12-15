import json

try:
    # Abrir y cargar el archivo JSON
    with open("./ficheros/juegos.json", "r", encoding="utf-8") as fichero:
        juegos = json.load(fichero)

    # Mostrar cada país con el formato requerido
    for pais in juegos:
        print(f"{pais['nombre']} está en {pais['plataforma']} y es del año {pais['año']}.")

except FileNotFoundError:
    print("Error: El archivo 'juegos.json' no existe o no se encontró.")

except json.JSONDecodeError:
    print("Error: El archivo no tiene un formato JSON válido.")

except Exception as e:
    print(f"Ha ocurrido un error inesperado: {e}")