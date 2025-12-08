#Crea una lista solo de números (ejemplo: temperaturas =).
#Calcula la suma de todos los elementos utilizando la función sum() y la media
#(promedio) combinando sum() y len().
#Muestra los valores máximo y mínimo de la lista.
temperaturas = [23.5, 25.0, 19.8, 22.1, 24.3, 20.0]
suma_temperaturas = sum(temperaturas)
media_temperaturas = suma_temperaturas / len(temperaturas)
max_temperatura = max(temperaturas)
min_temperatura = min(temperaturas)
print("Suma de temperaturas:", suma_temperaturas)
print("Media de temperaturas:", media_temperaturas)
print("Temperatura máxima:", max_temperatura)
print("Temperatura mínima:", min_temperatura)
