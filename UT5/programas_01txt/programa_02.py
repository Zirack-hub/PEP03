try:
    with open("./ficheros/datos.txt", "r", encoding="utf-8") as fichero:
        numerado = int(0)
        for fila in fichero:
            numerado += 1
            print(numerado,fila)

except FileNotFoundError:
    print("Error: El archivo 'datos.txt' no existe o no se encuentra en el directorio.")

except PermissionError:
    print("Error: No tienes permisos para leer el archivo.")

except ValueError:
    print("Error: El formato del archivo no es correcto.")
    
except Exception as e:
    print(f"Se ha producido un error inesperado: {e}")