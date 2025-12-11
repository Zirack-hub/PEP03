# Una función sirve para acortar un trozo de codigo que hace algo a una palabra
# Se le pueden poner argumentos para que si pones algo se haga la función teniendo en cuenta esos argumentos y si no pones nada al llamar a la función de error
def mi_funcion(nombre, apellido):
    print('Saludos desde mi función')
    print(f'Nombre: {nombre}, Apellido: {apellido}')

def mi_funcion2():
    # La palabra "pass" sirve para indicar que se cree la función pero que no va a tener ningún contenido
    pass

mi_funcion('Juan', 'Perez')
mi_funcion('Karla', 'Lara')