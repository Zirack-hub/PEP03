from tuplas import juegos

def encontrar_juego():  
    nombre_juego = input("Introduce el título de un juego: ").replace(" ", "").lower()
    encontrado = False
    i = 0
    while (not encontrado and i < len(juegos)):
        titulo, año, genero = juegos[i]
        if titulo.replace(" ", "").lower() == nombre_juego:
            print(f"Título: {titulo} | Género: {genero} | Año: {año}")
            encontrado = True
        i += 1

    if not encontrado:
            print("No se encontró el juego.")

if __name__ == "__main__":
    encontrar_juego()