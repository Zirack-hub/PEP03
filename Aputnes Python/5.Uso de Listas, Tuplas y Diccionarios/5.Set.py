# Set es una lista que no guarda ningún orden y no permite almacenar elementos duplicados
planetas = {'Marte', 'Júpiter', 'Venus'}
print(planetas)

# Largo de los elementos
print(len(planetas))

# Revisar si un elemento está presente
print('Marte' in planetas)

# Agregar elementos
planetas.add('Tierra')
print(planetas)

# No se pueden duplicar elementos
planetas.add('Tierra')
print(planetas)

# Eliminar un elemento posiblemente saliendo un error
planetas.remove('Tierra')
print(planetas)

# Eliminar un elemento sin salir error
planetas.discard('Júpiters')
print(planetas)

# Limpiar Set
planetas.clear()
print(planetas)

# Eliminar Set
del planetas
print(planetas)