try:
    contador =1
    
    with open("./ficheros/datos.txt", "r", encoding="utf-8") as fichero:
        
        for fila in fichero:
            if contador == 2:
                fichero.seek(0)
            contador += 1
            print(fila)
        
        
        
except FileNotFoundError:
    print("Error: El archivo 'datos.txt' no existe o no se encuentra en el directorio.")

except PermissionError:
    print("Error: No tienes permisos para leer el archivo.")

except ValueError:
    print("Error: El formato del archivo no es correcto.")
    
except Exception as e:
    print(f"Se ha producido un error inesperado: {e}")