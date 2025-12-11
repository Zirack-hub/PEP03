import json

try:
    # Abrir y cargar el archivo JSON
    with open("./ficheros/paises.json", "r", encoding="utf-8") as fichero:
        paises = json.load(fichero)

    # Mostrar cada país con el formato requerido
    for pais in paises:
        print(f"{pais['nombre']} está en {pais['continente']} y tiene {pais['poblacion']} millones de habitantes.")

except FileNotFoundError:
    print("Error: El archivo 'paises.json' no existe o no se encontró.")

except json.JSONDecodeError:
    print("Error: El archivo no tiene un formato JSON válido.")

except Exception as e:
    print(f"Ha ocurrido un error inesperado: {e}")
