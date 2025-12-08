#Crea una cadena "Python".
#Extrae la subcadena "Pyt" con slicing.
#Extrae los caracteres en posiciones pares con slicing ::2.
#Invierte la cadena con slicing [::-1].
#Recorre la cadena carácter por carácter e imprímelos
cadena = "Python"
subcadena = cadena[0:3]
print("Subcadena 'Pyt':", subcadena)
caracteres_pares = cadena[::2]
print("Caracteres en posiciones pares:", caracteres_pares)
cadena_invertida = cadena[::-1]
print("Cadena invertida:", cadena_invertida)
print("Recorriendo la cadena carácter por carácter:")
for char in cadena:
    print(char)