# Definir una lista
nombres = ['Juan','Karla','Ricardo', 'María']

# Imprimir la lista nombres
print(nombres)

# Acceder a los elementos de una lista
print(nombres[0])

# Acceder a los elementos de manera inversa
print(nombres[-1])

# Imprimir un rango
print(nombres[0:2]) # Sin incluir el indice 2

# Ir del inicio de la lista al índice (sin incluirlo)
print(nombres[:3])

# Desde el índice indicado hasta el final
print(nombres[1:])

# Cambiar un valor de la lista
nombres[3] = 'Ivone'
print(nombres)

# Repetir una lista
for nombre in nombres:
    print(nombre)
else:
    print('No existen más nombres en la lista')

# Preguntar el largo de una lista
print(len(nombres))

# Agregar un elemento
nombres.append('Lorenzo')
print(nombres)

# Insertar un elemento en un índice en específico
nombres.insert(1, 'Octavio')
print(nombres)

# Borrar un elemento
nombres.remove('Octavio')
print(nombres)

# Borrar el ultimo valor agregado
nombres.pop()
print(nombres)

# Eliminar un indice
del nombres[0]
print(nombres)

# Limpiar la lista
nombres.clear()
print(nombres)

# Borrar la lista por completo
del nombres
print(nombres)