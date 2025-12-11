import csv
import os

try:
    with open("./ficheros/capitales.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)

        escritor.writerow(["Ciudad", "País", "Continente"])

        datos = [
            ["París", "Francia", "Europa"],
            ["Canberra", "Australia", "Oceanía"],
            ["Nairobi", "Kenia", "África"],
            ["Ottawa", "Canadá", "América"]
        ]

        escritor.writerows(datos)

    print("Archivo 'capitales.csv' creado correctamente.")

except OSError as e:
    print("Error al crear o escribir en el archivo:",
          os.strerror(e.errno))
    
except Exception as e:
    print("Se produjo un error inesperado:", e)