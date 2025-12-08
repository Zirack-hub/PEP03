#Declara dos cadenas y únelas con concatenación (+).
#Repite una cadena tres veces con *.
#Compara dos cadenas lexicográficamente e indica cuál es mayor.
#Comprueba si una subcadena pertenece a otra con in.
cadena1 = "Hola"
cadena2 = "Mundo"
cadena_concatenada = cadena1 + " " + cadena2
print("Cadena concatenada:", cadena_concatenada)
cadena_repetida = cadena1 * 3
print("Cadena repetida:", cadena_repetida)

if cadena1 > cadena2:
    print(f'"{cadena1}" es mayor que "{cadena2}"')
elif cadena1 < cadena2:
    print(f'"{cadena2}" es mayor que "{cadena1}"')
else:
    print(f'"{cadena1}" es igual a "{cadena2}"')
