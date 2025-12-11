from os import strerror

try:
    nombre = input("Introduce el nombre del archivo binario de salida: ")
    datos = bytearray(range(256))  # Valores de 0 a 255

    with open("./ficheros/"+ nombre, "wb") as fichero:
        fichero.write(datos)

    print(f"Archivo '{nombre}' creado correctamente.")

except Exception as e:
    if hasattr(e, "errno"):
        print(f"Error: {strerror(e.errno)}")
    else:
        print(f"Se produjo un error inesperado: {e}")
