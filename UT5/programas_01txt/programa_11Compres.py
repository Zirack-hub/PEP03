try:
    nombre = str(input("Introduce el nombre del fichero: "))
    with open("./ficheros/"+ nombre + ".txt", "r", encoding="utf-8") as fichero:
        texto = fichero.read().lower()
        caracteres = {caracter: texto.count(caracter) for caracter in texto if caracter.isalpha()}
        caracteres_ordenados = sorted(caracteres.items(), key=lambda x: x[1], reverse=True)
        
    print("Histograma de las narices")
    for letra, frecuencia in caracteres_ordenados:
         print(f"{letra}: {frecuencia}")


    guardado = nombre + ".hist"

    with open("./ficheros/"+guardado, "w", encoding="utf-8") as fichero:
            for clave, valor in caracteres_ordenados:
                fichero.writelines(f"{clave}: {valor}\n")

except FileNotFoundError:
    print("Error, El archivo 'datos' no existe o no se encuentra en el directorio.")
except PermissionError:
    print("Error, No tienes permisos para leer el archivo.")
except ValueError:
    print("Error, El formato del archivo no es correcto.")
except Exception as e:
    print(f"Se ha producido un error inseperado: {e}")