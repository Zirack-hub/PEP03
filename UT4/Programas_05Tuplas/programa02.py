#Crea una lista de f juegos y conviértela a tupla usando tuple().
#Convierte nuevamente la tupla a lista.
#Muestra los tipos antes y después de cada conversión.

# Lista original
juegos = ["Silksong", "Expedition33", "LOL"]
print("Tipo de 'juegos' inicialmente:", type(juegos))

# Convertir lista a tupla
juegos_tupla = tuple(juegos)
print("Tipo después de convertir a tupla:", type(juegos_tupla))

# Convertir nuevamente a lista
juegos_lista = list(juegos_tupla)
print("Tipo después de convertir otra vez a lista:", type(juegos_lista))


