#Escribe un programa que muestre los números pares que hay entre 0 y 10. Resuelve el
#ejercicio de 4 formas diferentes. Usando los bucles for y while sin y con la sentencia
#continue.

cont=0
while cont<=10:
    if cont%2==0:
        print(cont)
    cont+=1
    
cont=-1
while cont<=10:
    cont+=1
    if cont%2!=0:
        continue
    print(cont)
    

for i in range(11):
    if i%2==0:
        print(i)

for i in range(-1, 11):
    if i % 2 != 0:   
        continue
    print(i)






