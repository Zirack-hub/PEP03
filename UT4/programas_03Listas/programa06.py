#Crea un cadena de caracteres con varias palabras y a partir de ella crear una lista
#que contenga como elementos las palabras de la cadena.
#◦ Usa la método split().
#◦ Usa método partition()
# Crea lista que contenga como elementos varias palabras y partir de ella crear una
#cadena de caracteres que contenga las palabras separadas por guiones.
cadena = "Esta es una cadena de caracteres con varias palabras"
lista_split = cadena.split()
print("Lista usando split():", lista_split)
lista_partition = list(cadena.partition("de"))
print("Lista usando partition():", lista_partition)
lista_palabras = ["Esta", "es", "una", "lista", "de", "palabras"]
cadena_guiones = "-".join(lista_palabras)
print("Cadena unida con guiones:", cadena_guiones)
