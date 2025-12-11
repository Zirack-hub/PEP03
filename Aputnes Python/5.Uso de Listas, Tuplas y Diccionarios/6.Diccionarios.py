# Un diccionario está compuesto de dos elementos una llave (key) y un valor (value)
diccionario = {
    'IDE':'Integrated Development Environment',
    'OOP':'Object Oriented Programming',
    'DBMS':'Database Management System'
}
print(diccionario)

# Largo del diccionario
print(len(diccionario))

# Acceder a un elemento (key)
print(diccionario['IDE'])

# Otra forma de acceder a un elemento
print(diccionario.get('OOP'))

# Modificar elementos
diccionario['IDE'] = 'integrated development environment'
print(diccionario)

# Recorrer los elementos
for termino, valor in diccionario.items():
    print(termino, valor)

# Recorrer solo las llaves
for termino in diccionario.keys():
    print(termino)

# Recorrer solo los valores
for valor in diccionario.values():
    print(valor)

# Comprobar la existencia de algún elemento
print('IDE' in diccionario)

# Agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

# Borrar un elemento
diccionario.pop('DBMS')
print(diccionario)

# Limpiar el diccionario
diccionario.clear()
print(diccionario)

# Eliminar el diccionario
del diccionario
print(diccionario)