import json

try:
    with open("./ficheros/paises.json", "r", encoding="utf-8") as fichero:
        paises = json.load(fichero)

    continente = input("Introduce un continente: ")

    filtrados = [p for p in paises if p["continente"].lower() == continente.lower()]

    if filtrados:
        print("\nPaíses encontrados:")
        for pais in filtrados:
            print(f"{pais['nombre']} está en {pais['continente']}.")
    else:
        print("\nNo se encontraron países en ese continente.")

    with open("paises_filtrados.json", "w", encoding="utf-8") as salida:
        json.dump(filtrados, salida, ensure_ascii=False, indent=4)

    print("\nArchivo 'paises_filtrados.json' creado correctamente.")

except FileNotFoundError:
    print("Error: No se encontró el archivo 'paises.json'.")
except json.JSONDecodeError:
    print("El archivo JSON está mal formado.")
except Exception as e:
    print(f"Error inesperado: {e}")
