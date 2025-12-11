try:
    numereos = int(0)

    with open("./ficheros/saludo.txt", "r", encoding="utf-8") as fichero:
        
        caracter = fichero.read(1)
        while caracter != "":
            if caracter != " ":
                numereos += 1
            caracter = fichero.read(1)
        
        print(f"El numero de caracteres es {numereos}")
        
except FileNotFoundError:
    print("Error: El archivo 'datos.txt' no existe o no se encuentra en el directorio.")

except PermissionError:
    print("Error: No tienes permisos para leer el archivo.")

except ValueError:
    print("Error: El formato del archivo no es correcto.")
    
except Exception as e:
    print(f"Se ha producido un error inesperado: {e}")