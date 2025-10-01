#Escribe un programa que pida números hasta que se introduzca un cero. Debe imprimir la
#suma y la media de todos los números introducidos. Realiza dos versiones: una que utiliza
#la instrucción break y otra no.

suma=0
cont=0
while True:
    num=int(input("Introduce un número (0 para terminar): "))
    if num==0:
        break
    suma+=num
    cont+=1
if cont>0:
    print("Suma:", suma)
    print("Media:", suma/cont)
else:
    print("No se han introducido números.")

suma=0
cont=0
num=-1
while num!=0:
    num=int(input("Introduce un número (0 para terminar): "))
    if num!=0:
        suma+=num
        cont+=1
if cont>0:
    print("Suma:", suma)
    print("Media:", suma/cont)
else:
    print("No se han introducido números.")

