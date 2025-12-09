#Crea dos tuplas con valores distintos y únelas con +.
#Repite una tupla dos veces con *.
#Asigna la tupla a una nueva variable (copia = tupla) y muestra sus identificadores
#con id().
#Comprueba si ambas variables apuntan al mismo objeto.

tupla1=("yo", "hoy", "me","mato")
tupla2=("puto","alvaro","cabron")

tupla3 = tupla1+tupla2
print(tupla3)
print(tupla2*5)
copia = tupla2
print(id(tupla2))
print(id(copia))
