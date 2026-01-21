import json
planetas = [
   
    {"nombre": "Marte", "Tipo": "Rocoso", "Lunas": 2},
    {"nombre": "Jupiter", "Tipo": "Gaseoso", "Lunas": 79},
    {"nombre": "Marte", "Tipo": "Rocoso", "Lunas": 0},
]

try:
    # Crear el archivo JSON con codificación UTF-8
    with open("./ficheros/planetas.json", "w", encoding="utf-8") as fichero:
        json.dump(planetas, fichero, ensure_ascii=False, indent=4)

    print("Archivo 'planetas.json' creado correctamente.")
    try:
        # Abrir y cargar el archivo JSON
        with open("./ficheros/planetas.json", "r", encoding="utf-8") as fichero:
            planetitas = json.load(fichero)

        # Mostrar cada país con el formato requerido
        for planets in planetitas:
            print(f"{planets['nombre']} es de tipo {planets['Tipo']} y tiene {planets['Lunas']}.")

    except FileNotFoundError:
        print("Error: El archivo 'planetas.json' no existe o no se encontró.")

    except json.JSONDecodeError:
        print("Error: El archivo no tiene un formato JSON válido.")

    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")
except Exception as e:
    print(f"Error al crear el archivo: {e}")