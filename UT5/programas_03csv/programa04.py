import csv

patrimonios = [
    {"Ciudad": "Roma", "País": "Italia", "Lugar emblemático": "Coliseo"},
    {"Ciudad": "El Cairo", "País": "Egipto", "Lugar emblemático": "Pirámides de Guiza"},
    {"Ciudad": "Kioto", "País": "Japón", "Lugar emblemático": "Templos históricos"}
]

try:
    with open("./ficheros/patrimonios.csv", "w", newline="", encoding="utf-8") as archivo:
        fieldnames = ["Ciudad", "País", "Lugar emblemático"]

        escritor = csv.DictWriter(archivo, fieldnames=fieldnames, delimiter=';')

        escritor.writeheader()

        escritor.writerows(patrimonios)

    print("Archivo 'patrimonios.csv' generado correctamente.")
    
except Exception as e:
    print("Se ha producido un error al generar el archivo:", e)