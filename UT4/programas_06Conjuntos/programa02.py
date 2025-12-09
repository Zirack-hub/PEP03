#Crea un conjunto con varias frutas.
#Añade nuevos elementos usando add().
#Elimina un elemento existente usando remove().
#Usa discard() para eliminar un elemento que no exista (sin error).
#Usa pop() para eliminar un elemento aleatorio..
conjunto_frutas = {"manzana", "banana", "cereza"}
conjunto_frutas.add("naranja")
conjunto_frutas.remove("banana")
conjunto_frutas.discard("banana")  # No da error si no existe
fruta_eliminada = conjunto_frutas.pop()  # Elimina un elemento aleatorio
print("Fruta eliminada con pop():", fruta_eliminada)
print("Conjunto de frutas actual:", conjunto_frutas)
