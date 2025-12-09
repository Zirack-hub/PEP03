#Escribe un programa en Python que lea una cadena y devuelva un diccionario con la
#cantidad de apariciones de cada palabra en la cadena. Por ejemplo, si recibe "Qué lindo
#día que hace hoy" debe devolver: 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1
cadena = "Que lindo dia hace qué hoy".lower()
lista = cadena.split(" ")
print(lista)
diccionario = {palabra: (lista.count(palabra)) for palabra in lista}
print(diccionario)