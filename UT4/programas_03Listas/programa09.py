#Crear una lista con dos elementos que a su vez sean una lista con los 100 primeros
#números pares y otra lista con los 100 primeros números impares.
#◦ Usa un for para crearla.
#◦ Usa compresión de listas para crearla.
#Recorre la lista y muestra por pantalla todos sus elementos: en una línea todos los
#números pares y en otra los impares.
lista_numeros =[[],[]]
for i in range (200):
    if i%2==0:
        lista_numeros[0].append(i)
    else:
        lista_numeros[1].append(i)
print("Números pares:", lista_numeros[0])
print("Números impares:", lista_numeros[1])