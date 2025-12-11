alumnos = ["Ana", "Pedro", "Lucía", "Eva"]
try:
    with open("./ficheros/alumnos.txt", "w", encoding="utf-8") as fichero:
        for nombre in alumnos:
            fichero.writelines(nombre+"\n")

    with open("./ficheros/alumnos.txt", "r", encoding="utf-8") as fichero:
        for fila in fichero:
            print(fila.upper())

except FileNotFoundError:
    print("Error: El archivo 'datos.txt' no existe o no se encuentra en el directorio.")

except PermissionError:
    print("Error: No tienes permisos para leer el archivo.")

except ValueError:
    print("Error: El formato del archivo no es correcto.")
    
except Exception as e:
    print(f"Se ha producido un error inesperado: {e}")