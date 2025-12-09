#Crea dos diccionarios con algunas claves comunes.
#Combínalos en un nuevo diccionario usando el operador |.
#Actualiza uno de ellos con update().
#Crea una copia con copy() y muestra los identificadores (id()) para comprobar
#que son distintos.
diccionario1 = {"clave1": "valor1", "clave2": 42, "clave3": [1, 2, 3]}
diccionario2 = {"clave2": "nuevo_valor", "clave4": 3.14, "clave5": True}

diccionario_combinado = diccionario1 | diccionario2
print("Diccionario combinado:", diccionario_combinado)
diccionario1.update(diccionario2)
print("Diccionario1 después de update():", diccionario1)
diccionario_copia = diccionario1.copy()
print("ID del diccionario1:", id(diccionario1))
print("ID del diccionario copia:", id(diccionario_copia))