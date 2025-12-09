#Crea un diccionario vacío y muestra su tipo.
#Crea un diccionario con al menos tres pares clave-valor (por ejemplo, nombre,
#edad, país).
#Crea un diccionario usando el constructor dict().
#Muestra el contenido y el tipo de cada uno.
diccionario_vacio = {}
print("tipo del diccionario_vacio:", type(diccionario_vacio))
diccionario_persona = {"nombre": "Ana", 
                       "edad": 28, 
                       "país": "España"
                       }
print("diccionario_persona:", diccionario_persona)
print("nombre:", diccionario_persona["nombre"])
print("tipo del diccionario_persona:", type(diccionario_persona))
diccionario_construct = dict(ciudad="Madrid", 
                            población=3200000, 
                            continente="Europa"
                            )
print("diccionario_construct:", diccionario_construct)
print("tipo del diccionario_construct:", type(diccionario_construct))