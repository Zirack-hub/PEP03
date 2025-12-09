#Crea una cadena de texto con palabras separadas por espacios.
#Divide la cadena en una lista con split() y conviértela a tupla
#Usa join() para convertir una tupla de palabras en una sola cadena separada por
#guiones.
#Usa partition() para dividir una expresión y mostrar el resultado como tupla.

cadena = "Esta es una cadena de texto"
tupla_cadena = tuple(cadena.split())
print("Tupla creada a partir de la cadena:", tupla_cadena)
tupla_palabras = ("Python", "es", "genial")
cadena_con_guiones = "-".join(tupla_palabras)
print("Cadena con guiones:", cadena_con_guiones)
expresion = "3 + 5 = 8"
resultado_partition = expresion.partition("=")
print("Resultado de partition():", resultado_partition)
 