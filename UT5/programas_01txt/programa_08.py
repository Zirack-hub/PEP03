from os import strerror
try:
    with open("./ficheros/inexistente.txt", "r", encoding="utf-8") as fichero:
        
        for fila in fichero:
            
            print(fila)

except FileNotFoundError as e:
    print(f"Error: {strerror(e.errno)}")

except PermissionError:
    print("Error: No tienes permisos para leer el archivo.")

except ValueError:
    print("Error: El formato del archivo no es correcto.")
    
except Exception as e:
    print(f"Se ha producido un error inesperado: {e}")