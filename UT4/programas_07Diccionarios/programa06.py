#Crea un diccionario con varias claves.
#Elimina una clave con del.
#Elimina otra con pop() y muestra el valor eliminado.
#Usa clear() para vaciar el diccionario.
#Reasigna el diccionario a {} y muestra el resultado
diccionario_ejemplo = {"clave1": "valor1",
                       "clave2": 42,
                       "clave3": [1, 2, 3]}
print("Diccionario original:", diccionario_ejemplo)
del diccionario_ejemplo["clave1"]
print("Diccionario después de eliminar clave1:", diccionario_ejemplo)
valor_eliminado = diccionario_ejemplo.pop("clave2")
print("Valor eliminado con pop():", valor_eliminado)
diccionario_ejemplo.clear()
print("Diccionario después de clear():", diccionario_ejemplo)
diccionario_ejemplo = {}
print("Diccionario reasignado a {}:", diccionario_ejemplo)
