#Crea una tupla de dos dimensiones que simule una tabla 3x3 de números.
#Recorre todos sus elementos con bucles anidados.
#Crea una tupla que contenga listas como elementos.
#Modifica una de las listas y comprueba si la tupla refleja el cambio
tupla_tabla = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
for fila in tupla_tabla:
    for elemento in fila:
        print(elemento, end=" ")
    print()

tupla_con_listas = ([10, 20, 30], [40, 50, 60], [70, 80, 90])
print("Antes de modificar la lista:", tupla_con_listas)
tupla_con_listas[2][1] = 99
print("Después de modificar la lista:", tupla_con_listas)