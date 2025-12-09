#Define un diccionario con varias claves y valores.
#Accede a algunos valores usando corchetes [] y muestra los resultados.
#Accede a valores usando get() con y sin valor por defecto.
#Intenta acceder a una clave inexistente con get() y observa el resultado.
diccionario_ejemplo = {"clave1": "valor1",
                       "clave2": 42,
                       "clave3": [1, 2, 3]}
print("Acceso con corchetes clave1:", diccionario_ejemplo["clave1"])
print("Acceso con corchetes clave2:", diccionario_ejemplo["clave2"])
print("Acceso con get() clave3:", diccionario_ejemplo.get("clave3"))
print("Acceso con get() clave inexistente (sin valor por defecto):", diccionario_ejemplo.get("clave_inexistente"))
print("Acceso con get() clave inexistente (con valor por defecto):", diccionario_ejemplo.get("clave1", "hola perros"))
