try:
    palabras = 0
    lineas = 0
    caracteres = 0

    with open("./ficheros/origen.txt", "r", encoding="utf-8") as origen, \
         open("./ficheros/copia.txt", "w", encoding="utf-8") as copia:

        for fila in origen:
            lineas += 1
            palabras += len(fila.split())
            caracteres += len(fila)

            print(fila.strip())
            copia.write(fila)

    print(f"Número de líneas copiadas: {lineas}, "
          f"Número de palabras copiadas: {palabras}, "
          f"Número de caracteres copiados: {caracteres}")

except FileNotFoundError:
    print("Error: El archivo 'origen.txt' no existe o no se encuentra en el directorio.")

except PermissionError:
    print("Error: No tienes permisos para leer el archivo.")

except ValueError:
    print("Error: El formato del archivo no es correcto.")

except Exception as e:
    print(f"Se ha producido un error inesperado: {e}")
