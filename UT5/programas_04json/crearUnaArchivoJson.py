import json

# Lista de capitales
juegos = [
   
    {"nombre": "The Legend of Zelda: Breath of the Wild", "plataforma": "Nintendo Switch", "año": 2017},
    {"nombre": "God of War", "plataforma": "PlayStation 4", "año": 2018},
    {"nombre": "Minecraft", "plataforma": "Multiplataforma", "año": 2011},
    {"nombre": "Expedition 33", "plataforma": "Multiplataforma", "año": 2025}
]

try:
    # Crear el archivo JSON con codificación UTF-8
    with open("./ficheros/juegosCopia.json", "w", encoding="utf-8") as fichero:
        json.dump(juegos, fichero, ensure_ascii=False, indent=4)

    print("Archivo 'juegosCopia.json' creado correctamente.")

except Exception as e:
    print(f"Error al crear el archivo: {e}")