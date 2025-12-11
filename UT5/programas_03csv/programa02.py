import csv

try:
    with open("./ficheros/ciudades.csv", newline='', encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        if lector.fieldnames is None:
            archivo.seek(0)
            lector = csv.DictReader(archivo, fieldnames=["Ciudad", "País", "Población (millones)"])
            print("El archivo no tenía cabecera. Se han asignado manualmente:")
        else:
            print("Columnas encontradas en el archivo:")

        print(lector.fieldnames)
        print()

        for fila in lector:
            ciudad = fila.get("Ciudad")
            pais = fila.get("País")
            poblacion = fila.get("Población (millones)")
            print(f"{ciudad} ({pais}) tiene una población aproximada de {poblacion} millones.")

except FileNotFoundError:
    print("Error: El archivo 'ciudades.csv' no existe o no se encuentra en el directorio.")

except PermissionError:
    print("Error: No tienes permisos para leer el archivo.")

except Exception as e:
    print(f"Se ha producido un error inesperado: {e}")