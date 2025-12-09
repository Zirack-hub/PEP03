#Partiendo de mi_listaXX del ejercicio anterior modifica el valor del tercer elemento aun nuevo valor de tu elección.
#Añade un nuevo elemento al final de la lista utilizando el método append().
#Inserta una nueva cadena de caracteres en la segunda posición de la lista (índice1) utilizando el método insert().
#Recorre la lista y muestra sus elementos por pantalla.
mi_lista03 = [42, "Hola", True, 3.14]
mi_lista03[2]= "Nuevo Valor"
mi_lista03.append("ERFINAH")
mi_lista03.insert(1,"Cadena Insertada p2")
for elemento in mi_lista03:
    print(elemento)