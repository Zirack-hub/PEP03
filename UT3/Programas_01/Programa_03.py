#Escribe un programa en Python que muestre un menú que permita al usuario seleccionar
#qué operación desea realizar. Las operaciones que puede realizar serán calcular el área
#de un círculo, un triángulo o un rectángulo. El menú que se le muestra al usuario será
#similar al siguiente:
#   1. Calcular el área de un círculo
#   2. Calcular el área de un triángulo
#   3. Calcular el área de un rectángulo
#   4. Salir
#   Introduce una opción (1-4):

import math

# Funciones para calcular áreas
def area_circulo(radio):
    return math.pi * radio**2

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_rectangulo(base, altura):
    return base * altura

while True:
    print("\n--- Menú de cálculo de áreas ---")
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un triángulo")
    print("3. Calcular el área de un rectángulo")
    print("4. Salir")
    
    opcion = input("Introduce una opción (1-4): ")
    
    if opcion == "1":
        radio = float(input("Introduce el radio del círculo: "))
        print(f"El área del círculo es: {area_circulo(radio):.2f}")
    elif opcion == "2":
        base = float(input("Introduce la base del triángulo: "))
        altura = float(input("Introduce la altura del triángulo: "))
        print(f"El área del triángulo es: {area_triangulo(base, altura):.2f}")
    elif opcion == "3":
        base = float(input("Introduce la base del rectángulo: "))
        altura = float(input("Introduce la altura del rectángulo: "))
        print(f"El área del rectángulo es: {area_rectangulo(base, altura):.2f}")
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida, por favor elige entre 1 y 4.")
