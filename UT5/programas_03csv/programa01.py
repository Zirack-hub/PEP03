import csv

try:
    with open("./ficheros/ciudades.csv", newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)

        next(lector)

        for fila in lector:
            ciudad, pais, poblacion = fila
            print(f"La ciudad de {ciudad} está en {pais} y tiene {poblacion} millones de habitantes.")

except FileNotFoundError:
    print("Error: El archivo 'ciudades.csv' no existe o no se encuentra en el directorio.")

except PermissionError:
    print("Error: No tienes permisos para leer el archivo.")

except ValueError:
    print("Error: El formato del archivo no es correcto.")
    
except Exception as e:
    print(f"Se ha producido un error inesperado: {e}")