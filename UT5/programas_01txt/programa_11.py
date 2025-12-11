try:
    diccionario = {}
    numereos = int(0)
    nombre = str(input("Introduce el nombre del fichero: "))
    with open("./ficheros/"+ nombre +".txt", "r", encoding="utf-8") as fichero:
        
        for linea in fichero:
            for caracter in linea:
                if caracter.isalpha():
                    letra = caracter.lower()
                    if letra in diccionario:
                        diccionario[letra] += 1
                    else:
                        diccionario[letra] = 1
        
        diccionario_ordenado = sorted(diccionario.items(), key=lambda x: x[1], reverse=True)
        print("NUMERO DE LETRAS, NO HISTOGRAMA NUMERO DE MALDITAS LETRAS EN EL TEXTO")
        for letra, numero in diccionario_ordenado:
            print(f"{letra}: {numero}")
        
        guardado = nombre + ".hist"

        with open("./ficheros/"+guardado, "w", encoding="utf-8") as salida:
            for letra, frecuencia in diccionario_ordenado:
                salida.write(f"{letra}: {frecuencia}\n")

        print(f"\nHistograma guardado en el archivo '{guardado}'")

except FileNotFoundError:
    print("Error: El archivo 'datos.txt' no existe o no se encuentra en el directorio.")

except PermissionError:
    print("Error: No tienes permisos para leer el archivo.")

except ValueError:
    print("Error: El formato del archivo no es correcto.")
    
except Exception as e:
    print(f"Se ha producido un error inesperado: {e}")