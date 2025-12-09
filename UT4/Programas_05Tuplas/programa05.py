#Crea una tupla con varios valores repetidos.
#Busca el índice de un elemento usando index().
#Muestra cuántas veces aparece un elemento usando count().
#Comprueba si un valor está en la tupla (in) o no está (not in)

tupla = ("ERFINAH","silksong","puto","alvaro","me","mato","silksong","ERFINAH")
print(tupla.index("ERFINAH"))
print(tupla.count("ERFINAH"))
scanner = input("Introduce la palabra a buscar: ")
if scanner in tupla:
    print(f"La palabra {scanner} se encuentra en la tupla")
if scanner not in tupla:
    print(f"la palabra {scanner} no esta en la tupla")