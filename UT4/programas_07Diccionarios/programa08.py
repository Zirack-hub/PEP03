#Crea una cadena o lista y genera un diccionario que cuente la frecuencia de cada elemento usando compresión.
#Crea otro diccionario que asigne números del 1 al 5 con sus cuadrados.
#Muestra ambos resultados.
cadena = "abracadabra"
frecuencia = {Letra: cadena.count(Letra) for Letra in set(cadena)}
print("Frecuencia de letras:", frecuencia)
cuadrados = {num: num**2 for num in range(1, 6)}
print("Números y sus cuadrados:", cuadrados)
