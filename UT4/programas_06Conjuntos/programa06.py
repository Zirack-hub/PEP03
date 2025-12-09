#Crea tres conjuntos diferentes.
#Usa los métodos issubset(), issuperset() e isdisjoint() para verificar
#relaciones entre ellos.
#Muestra los resultados de cada comprobación
conjunto_X = {1, 2, 3}
conjunto_Y = {1, 2, 3, 4, 5}
conjunto_Z = {6, 7, 8}
print("¿X es subconjunto de Y?", conjunto_X.issubset(conjunto_Y))
print("¿Y es superconjunto de X?", conjunto_Y.issuperset(conjunto_X))
print("¿X y Z son disjuntos?", conjunto_X.isdisjoint(conjunto_Z))