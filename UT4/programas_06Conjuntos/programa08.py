#Usa comprensión de conjuntos para crear:
#◦ Un conjunto con los números del 1 al 10.
#◦ Un conjunto con los cuadrados de los números del 1 al 10.
#◦ Un conjunto con los números pares del 1 al 20
#Muestra los resultado

conjunto_numeros = {x for x in range(1, 11)}
conjunto_cuadrados = {x**2 for x in range(1, 11)}
conjunto_pares = {x for x in range(1, 21) if x % 2 == 0}
print("Conjunto de números del 1 al 10:", conjunto_numeros)
print("Conjunto de cuadrados del 1 al 10:", conjunto_cuadrados)
print("Conjunto de números pares del 1 al 20:", conjunto_pares)
