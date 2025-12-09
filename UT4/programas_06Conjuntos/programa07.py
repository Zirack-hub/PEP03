#Crea un conjunto con varios colores.
#Crea una copia con copy() y verifica que tienen distintos identificadores usando id().
#Usa update() para añadir todos los elementos de otro conjunto.
#Muestra ambos conjuntos antes y después de la actualización.

conjunto_colores = {"rojo", "verde", "azul"}
conjunto_copia = conjunto_colores.copy()
print("ID del conjunto original:", id(conjunto_colores))
print("ID del conjunto copia:", id(conjunto_copia))
conjunto_nuevos_colores = {"amarillo", "naranja"}
print("Conjunto original antes de update():", conjunto_colores)
conjunto_colores.update(conjunto_nuevos_colores)
print("Conjunto original después de update():", conjunto_colores)
