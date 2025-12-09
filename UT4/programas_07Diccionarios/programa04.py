#Comprueba si ciertas claves existen en el diccionario usando in y not in.
#Muestra el número total de elementos usando len().
#Muestra las claves (keys), los valores (values) y los pares (items)
diccionario_persona = {"nombre": "Rizwan",
                       "edad": 78,
                       "país": "Mexico"}
print("¿La clave 'edad' está en el diccionario?", "edad" in diccionario_persona)
print("¿La clave 'profesión' no está en el diccionario?", "profesión" not in diccionario_persona)
print("Número total de elementos en el diccionario:", len(diccionario_persona))
print("Claves:", diccionario_persona.keys())
print("Valores:", diccionario_persona.values())
print("Pares clave-valor:", diccionario_persona.items())