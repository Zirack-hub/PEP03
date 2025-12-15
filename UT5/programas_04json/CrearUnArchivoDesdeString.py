import json

# Lista de capitales
cadena_json ='''
[
{"nombre": "Chile", "moneda": "Peso chileno"},
{"nombre": "Egipto", "moneda": "Libra egipcia"}
]
'''


try:
    monedas=json.loads(cadena_json)
    print("Tipo de dato:", type(monedas))
   
    for pais in monedas:
        print(f"{pais['nombre']} utiliza la moneda: {pais['moneda']}.")

    # Guardar también en un archivo JSON
    with open("./ficheros/monedas.json", "w", encoding="utf-8") as fichero:
        json.dump(monedas, fichero, ensure_ascii=False, indent=4)

    print("Archivo 'paises_monedas.json' creado correctamente.")

except Exception as e:
    print(f"Error al crear el archivo: {e}")