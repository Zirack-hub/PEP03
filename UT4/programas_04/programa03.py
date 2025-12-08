#Escribe un programa en Python que permita crear una lista de palabras y que, a
#continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista
lista = []
for i in range (5):
    scanner = str(input("introduce una palabra: "))
    lista.append(scanner)

scanner = str(input("introduce una palabra: "))

if scanner in lista:
    print(f"La palabra introducida {scanner} se ha repetido: {lista.count(scanner)} veces")

