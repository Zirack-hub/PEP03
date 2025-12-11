try:
    with open("./ficheros/datos.bin", "rb") as fichero:
        datos = fichero.read()  # Leer todo el contenido
        datos_bytearray = bytearray(datos)  # Convertir a bytearray

    print("Contenido de 'datos.bin' en hexadecimal:")
    for byte in datos_bytearray:
        print(hex(byte), end=' ')
    print() 

except FileNotFoundError:
    print("Error: El archivo 'datos.bin' no existe.")

except Exception as e:
    print(f"Se produjo un error inesperado: {e}")
