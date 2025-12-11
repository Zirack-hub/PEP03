try:
    buffer = bytearray(10)

    with open("./ficheros/datos.bin", "rb") as fichero:
        bytes_leidos = fichero.readinto(buffer)

    print(f"Bytes leídos: {list(buffer)}")
    print(f"Número total de bytes cargados: {bytes_leidos}")

    # Modificar el bytearray (ejemplo: sumar 1 a cada byte)
    for i in range(bytes_leidos):
        buffer[i] = (buffer[i] + 1) % 256

    # Guardar en nuevo archivo
    with open("./ficheros/datos_modificados.bin", "wb") as salida:
        salida.write(buffer[:bytes_leidos])

    print("Bytearray modificado y guardado en 'datos_modificados.bin'.")

except FileNotFoundError:
    print("Error: 'datos.bin' no existe.")
except Exception as e:
    print(f"Error inesperado: {e}")
