try:
    buffer_size = 64 * 1024  # 64 KB
    buffer = bytearray(buffer_size)
    total_bytes = 0

    with open("./ficheros/origen.bin", "rb") as origen, open("copia.bin", "wb") as destino:
        while True:
            bytes_leidos = origen.readinto(buffer)
            if not bytes_leidos:
                break
            destino.write(buffer[:bytes_leidos])
            total_bytes += bytes_leidos

    print(f"Se copiaron {total_bytes} bytes en total.")

except FileNotFoundError:
    print("Error: 'origen.bin' no existe.")
except Exception as e:
    print(f"Error inesperado: {e}")
