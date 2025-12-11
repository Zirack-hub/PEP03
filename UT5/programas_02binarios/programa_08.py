from os import path

try:
    origen_nombre = input("Archivo de origen: ")
    destino_nombre = input("Archivo de destino: ")

    if not path.exists(origen_nombre):
        raise FileNotFoundError(f"El archivo '{origen_nombre}' no existe.")

    buffer_size = 64 * 1024  # 64 KB
    buffer = bytearray(buffer_size)
    total_bytes = 0
    progreso_umbral = 1 * 1024 * 1024  # 1 MB
    progreso_actual = 0

    with open(origen_nombre, "rb") as origen, open(destino_nombre, "wb") as destino:
        while True:
            bytes_leidos = origen.readinto(buffer)
            if not bytes_leidos:
                break
            destino.write(buffer[:bytes_leidos])
            total_bytes += bytes_leidos
            progreso_actual += bytes_leidos

            if progreso_actual >= progreso_umbral:
                print(f"Progreso: {total_bytes} bytes copiados...")
                progreso_actual = 0

    print(f"Copia finalizada. Total de bytes escritos: {total_bytes}")

except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(f"Se produjo un error inesperado: {e}")
