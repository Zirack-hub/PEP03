"""
Escribe un programa en Python que importe el módulo math completo y que le pregunte al
usuario qué operación matemática quiere hacer:
1. Seno de un ángulo
2. Coseno de un ángulo
3. Raíz cuadrada de un número
4. Potencia de dos números
Le pida los datos necesarios y muestre los resultados por pantalla.
"""

import math

print("Operaciones matemáticas")
print("1. Seno de un ángulo")
print("2. Coseno de un ángulo")
print("3. Raíz cuadrada de un número")
print("4. Potencia de dos números")

opcion = int(input("Elige una opción (1-4): "))

if opcion == 1:
    angulo = float(input("Introduce el ángulo en grados: "))
    resultado = math.sin(math.radians(angulo))
    print(f"El seno de {angulo}° es: {resultado:.4f}")

elif opcion == 2:
    angulo = float(input("Introduce el ángulo en grados: "))
    resultado = math.cos(math.radians(angulo))
    print(f"El coseno de {angulo}° es: {resultado:.4f}")

elif opcion == 3:
    numero = float(input("Introduce el número: "))
    if numero < 0:
        print("Error: No se puede calcular la raíz cuadrada de un número negativo.")
    else:
        resultado = math.sqrt(numero)
        print(f"La raíz cuadrada de {numero} es: {resultado:.4f}")

elif opcion == 4:
    base = float(input("Introduce la base: "))
    exponente = float(input("Introduce el exponente: "))
    resultado = math.pow(base, exponente)
    print(f"{base} elevado a la {exponente} es: {resultado:.4f}")

else:
    print("Opción no válida.")
