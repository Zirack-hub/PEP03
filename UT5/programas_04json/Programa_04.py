import json

pais = {
    "nombre": "Islandia",
    "capital": "Reikiavik",
    "idiomas": ["Islandés", "Inglés"],
    "superficie_km2": 103000
}

# Convertir el diccionario en una cadena JSON
cadena_json = json.dumps(pais, indent=2, sort_keys=True, ensure_ascii=False)

with open("./ficheros/pais2.json", "w", encoding="utf-8") as fichero:
        json.dump(cadena_json, fichero, ensure_ascii=False, indent=4)

# Imprimir la cadena generada
print(cadena_json)
