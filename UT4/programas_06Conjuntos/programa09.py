#Crea un conjunto normal y otro inmutable con frozenset().
#Muestra su tipo y contenido.
#Intenta añadir un nuevo elemento al frozenset y observa el resultado.
#Comprueba si el frozenset puede usarse como clave de un diccionario.
conjunto_normal = {"manzana", "banana", "cereza"}
conjunto_inmutable = frozenset(["rojo", "verde", "azul"])
print("Tipo de conjunto_normal:", type(conjunto_normal))
print("Contenido de conjunto_normal:", conjunto_normal)
print("Tipo de conjunto_inmutable:", type(conjunto_inmutable))
print("Contenido de conjunto_inmutable:", conjunto_inmutable)
try:
    conjunto_inmutable.add("amarillo")
    conjunto_inmutable[0] = "amarillo"
    print(conjunto_inmutable)
except AttributeError as e:
    print("Error al intentar añadir a frozenset:", e)
diccionario = {conjunto_inmutable: "colores primarios"}
print("Diccionario con frozenset como clave:", diccionario)
