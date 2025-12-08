#Ordenación Modificable vs. no modificable:
#◦ Crea una lista de cadenas no ordenadas. Utiliza el método sort() para
#ordenar la lista y comprueba que la lista original ha sido modificada.
#◦ Utiliza la función sorted() y comprueba que la lista original no se modifica.
#Concatenación
#◦ Crea dos listas y crea una nueva lista que se la concatenación de las anteriores.
#◦ Crea dos listas y amplia la primera añadiendo los elementos de las segunda
#Diferencia de copia:
#◦ Asigna tu lista original a una nueva variable utilizando una asignación directa
#(copia = lista). Muestra los identificadores de memoria de ambas variables
#usando id() para verificar que apuntan al mismo objeto.

mi_lista_cadenas =["ERPRINSIPIO","naranja", "manzana", "plátano", "kiwi","ERFINAH"]
mi_lista_cadenas.sort()
print("Lista ordenada con sort():", mi_lista_cadenas)
mi_lista_cadenas =["ERPRINSIPIO","naranja", "manzana", "plátano", "kiwi","ERFINAH"]
lista_ordenada = sorted(mi_lista_cadenas)
print("Lista ordenada con sorted():", lista_ordenada)
print("Lista original después de sorted():", mi_lista_cadenas)
lista1 = [1, 2, 3]
lista2 = ["a", "b", "c"]
lista_concatenada = lista1 + lista2
print("Lista concatenada:", lista_concatenada)
lista1 = [1, 2, 3]
lista2 = ["a", "b", "c"]
lista1.extend(lista2)
print("Lista1 después de extender con lista2:", lista1)
nueva_lista = mi_lista_cadenas
print("ID de mi_lista_cadenas:", id(mi_lista_cadenas))
print("ID de nueva_lista:", id(nueva_lista))
lista3 = mi_lista_cadenas.copy()
nueva_lista.append("uva")
print("mi_lista_cadenas después de modificar nueva_lista:", mi_lista_cadenas)
print("nueva_lista:", nueva_lista)
print("lista3 (copia de mi_lista_cadenas):", lista3)


