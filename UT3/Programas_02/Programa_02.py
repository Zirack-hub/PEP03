"""
Modifica el programa anterior para que solo se importen las funciones del módulo math
que se usan en el programa.
"""

from math import sin, cos, sqrt, pow, radians

print("Operaciones matemáticas")
print("1. Seno de un ángulo")
print("2. Coseno de un ángulo")
print("3. Raíz cuadrada de un número")
print("4. Potencia de dos números")

opcion = int(input("Elige una opción (1-4): "))

if opcion == 1:
    angulo = float(input("Introduce el ángulo en grados: "))
    resultado = sin(radians(angulo))
    print(f"El seno de {angulo}° es: {resultado:.4f}")

elif opcion == 2:
    angulo = float(input("Introduce el ángulo en grados: "))
    resultado = cos(radians(angulo))
    print(f"El coseno de {angulo}° es: {resultado:.4f}")

elif opcion == 3:
    numero = float(input("Introduce el número: "))
    if numero < 0:
        print("Error: No se puede calcular la raíz cuadrada de un número negativo.")
    else:
        resultado = sqrt(numero)
        print(f"La raíz cuadrada de {numero} es: {resultado:.4f}")

elif opcion == 4:
    base = float(input("Introduce la base: "))
    exponente = float(input("Introduce el exponente: "))
    resultado = pow(base, exponente)
    print(f"{base} elevado a la {exponente} es: {resultado:.4f}")

else:
    print("Opción no válida.")
