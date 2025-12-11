# El polimorfismo sirve para que objetos de diferentes clases puedan responder al mismo mensaje
from Gerente import Gerente
from Empleado import Empleado


def imprimir_detalles(objeto):
    print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalles())
    # El comando "isinstance" sirve para verificar si un objeto es una instancia de una clase o una tupla de clases
    if isinstance(objeto, Gerente):
        print(objeto.departamento)

empleado = Empleado('Juan', 5000)
imprimir_detalles(empleado)

gerente = Gerente('Karla', 6000, 'Sistemas')
imprimir_detalles(gerente)