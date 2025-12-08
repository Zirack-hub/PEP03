#Elimina el cuarto elemento de la lista utilizando la instrucción del.
#Elimina un elemento de la lista utilizando el método remove().
#Verifica si un un elemento pertenece a la lista.
#Muestra por pantalla el índice de un elemento de la lista.
#Muestra por pantalla el número de ocurrencias de un elemento en la lista
mi_lista =[42, "Cadena insertada p2", "Hola", True, 3.14, "ERFINAH"]
del mi_lista[3]
mi_lista.remove("Hola")
print("Cadena insertada p2" in mi_lista)
print("Índice de 3.14:", mi_lista.index(3.14))
print("Número de ocurrencias de 'ERFINAH':", mi_lista.count("ERFINAH"))
