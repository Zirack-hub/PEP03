import json

# Lista de capitales
capitales = [
    {"país": "Francia", "capital": "París"},
    {"país": "Australia", "capital": "Canberra"},
    {"país": "Kenia", "capital": "Nairobi"},
    {"país": "Brasil", "capital": "Brasilia"}
]

try:
    # Crear el archivo JSON con codificación UTF-8
    with open("./ficheros/capitales.json", "w", encoding="utf-8") as fichero:
        json.dump(capitales, fichero, ensure_ascii=False, indent=4)

    print("Archivo 'capitales.json' creado correctamente.")

except Exception as e:
    print(f"Error al crear el archivo: {e}")
