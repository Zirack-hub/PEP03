# Programa 10
# Escribe un programa que dado un número de dos cifras, diseñe un algoritmo que permita
# obtener el número invertido.

numero = input("Introduce un número de dos cifras: ")

if len(numero) == 2 and numero.isdigit():
    numero_invertido = numero[::-1]
    print("Número invertido:", numero_invertido)
else:
    print("Debe introducir un número de dos cifras.")
