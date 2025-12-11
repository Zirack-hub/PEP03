# Una tupla es una lista que no se puede modificar

# Definir una tupla
frutas = ('Naranja', 'Platano', 'Guayaba')
print(frutas)

# Saber el largo de una tupla
print(len(frutas))

# Acceder a un elemento
print(frutas[0])

# Navegación inversa
print(frutas[-1])

# Acceder a un rango
print(frutas[0:1]) # sin incuir el último índice

# Recorrer elementos de una tupla
for fruta in frutas:
    print(fruta, end=' ')

# Cambiar valor de una tupla
# frutas[0] = 'Pera' # En este caso como es una tupla te salta error y te dice que no se puede modificar

# El comando "list" nos permite cambiar una tupla a una lista
frutasLista = list(frutas)
frutasLista[0] = 'Pera'
# El comando "tuple" nos permite cambiar una lista a una tupla
frutas = tuple(frutasLista)
print('\n', frutas)

# Eliminar la tupla
del frutas
print(frutas)