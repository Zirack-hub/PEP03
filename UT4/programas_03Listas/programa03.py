#Crea una nueva lista extrayendo un slice de los elementos desde el índice 2 hasta el índice 5 (recuerda que el índice final es excluido).
#Muestra una nueva lista que contenga solo los elementos de tu lista original que estén en posiciones pares, utilizando un incremento de 2 en el slicing.
#Reverso
#◦ Crear nueva lista en orden inverso utilizando la sintaxis de slicing [::-1].
#◦ Usa el método reverse() para invertir la lista y modificar su contenido.
mi_lista =[42, "Cadena insertada p2", "Hola", True, 3.14, "ERFINAH"]

lista_cortada=mi_lista[2:5]
lista_inversa=mi_lista[::-1]
mi_lista.reverse()
mi_lista[0]="ERPRINSIPIO"
print(mi_lista)