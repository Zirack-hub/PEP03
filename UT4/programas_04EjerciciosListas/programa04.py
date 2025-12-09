#Escribe un programa en Python que permita crear dos listas de palabras y que, a
#continuación, escriba las siguientes listas (en las que no debe haber repeticiones):
#• Lista de palabras que aparecen en las dos listas.
#• Lista de palabras que aparecen en la primera lista, pero no en la segunda.
#• Lista de palabras que aparecen en la segunda lista, pero no en la primera.
#• Lista de palabras que aparecen en ambas listas
lista1 = []
lista2 = []

# Rellenar lista 1
for i in range(3):
    palabra = input("Introduce una palabra para lista 1: ")
    if palabra in lista1:
        print("Las palabras no deben estar repetidas")
    else:
        lista1.append(palabra)

# Rellenar lista 2
for i in range(3):
    palabra = input("Introduce una palabra para lista 2: ")
    if palabra in lista2:
        print("Las palabras no deben estar repetidas")
    else:
        lista2.append(palabra)

# Palabras que aparecen en las dos listas
print("Lista de palabras en las dos listas:")
for palabra in lista1:
    if palabra in lista2:
        print(palabra)

# Palabras solo en lista 1
print("Lista de palabras que solo están en lista 1:")
for palabra in lista1:
    if palabra not in lista2:
        print(palabra)

# Palabras solo en lista 2
print("Lista de palabras que solo están en lista 2:")
for palabra in lista2:
    if palabra not in lista1:
        print(palabra)

# Lista de palabras que aparecen en ambas listas (sin repeticiones)
print("Lista de palabras que aparecen en ambas listas (sin repeticiones):")
comunes = list(set(lista1) & set(lista2))
for palabra in comunes:
    print(palabra)
