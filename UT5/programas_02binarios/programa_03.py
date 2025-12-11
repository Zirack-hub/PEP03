try:
    # Abrir archivo binario en modo lectura
    with open("./ficheros/datos.bin", "rb") as fichero:
        while True:
            fragmento = fichero.read(5)  # Leer hasta 5 bytes
            if not fragmento:  # Si no hay más datos, salir del bucle
                break
            # Mostrar bytes en hexadecimal
            print("Bytes leídos:", [hex(b) for b in fragmento])

except FileNotFoundError:
    print("Error: El archivo 'datos.bin' no existe.")

except Exception as e:
    print(f"Se produjo un error inesperado: {e}")
