# El signo "*args" sirve para decir que se pueden meter todos los valores que quieras
def listar_nombres(*nombres):
    for nombre in nombres:
        print(nombre)

listar_nombres('Juan', 'Karla', 'María', 'Ernesto')
listar_nombres('Laura', 'Carlos')