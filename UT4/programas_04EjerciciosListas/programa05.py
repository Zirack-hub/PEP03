#Escribe un programa en Python que escriba tu propia función myslplit(), que se
#comporte casi como el método original split(), por ejemplo:
#Debe aceptar únicamente un argumento: una cadena.
#Debe devolver una lista de palabras creadas a partir de la cadena, dividida en los
#lugares donde la cadena contiene espacios en blanco.
#Si la cadena está vacía, la función debería devolver una lista vacía.

cadena = "Alvaro no tienes ni idea de hacer asignaturas cortas"
palabra_actual =""
lista=[]

for caracter in cadena:
    if caracter != " ":
        palabra_actual += caracter
    else:
        if palabra_actual !="":
            lista.append(palabra_actual)
            palabra_actual = ""

if palabra_actual != "":
    lista.append(palabra_actual)

print(lista)