#Escribe un programa en Python que lea por teclado números y los guare en una lista, el
#proceso finaliza cuando se introduzca un número negativo. A continuación que muestre el
#máximo de los números guardado en la lista y los números pares de la lista.
numeros = []
booleano=True
while booleano:
    num = int(input("Introduce un número (negativo para terminar): "))
    if num < 0:
       booleano=False 
    else:
        numeros.append(num)

numax = max(numeros)
lista_pares = []
for numero in numeros:
    if numero % 2 == 0:
        lista_pares.append(numero)
print("El número máximo es:", numax)
print("Números pares en la lista:", lista_pares)


