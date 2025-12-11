try:
    # Crear un bytearray con los números del 1 al 10
    datos = bytearray(range(1, 11))  # range(1, 11) genera 1,2,...,10

    # Abrir archivo en modo escritura binaria
    with open("./ficheros/datos.bin", "wb") as fichero:
        bytes_escritos = fichero.write(datos)  # Escribir bytearray en el archivo

    print(f"Se escribieron {bytes_escritos} bytes en 'datos.bin'.")

except Exception as e:
    print(f"Se produjo un error: {e}")
