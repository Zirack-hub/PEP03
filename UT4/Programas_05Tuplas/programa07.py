#Crea una tupla con tres valores y asígnalos a tres variables mediante
#desempaquetado.
#Usa el operador * para desempaquetado extendido.
#Define una función media(*args) que calcule la media de varios números y
#pruébala con diferentes argumentos.
tupla1=["puto","alvaro","cabron"]
a,b,c = tupla1

tupla2 = (1, 2, 3, 4, 5)

x, *resto, z = tupla2

print("x:", x)
print("resto:", resto)
print("z:", z)



def media(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)

print(media(*tupla2))
print(media(30,20,10))
