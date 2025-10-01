# Programa 05
# Escribe un programa que pida dos números y que indique cuál es el menor,
# cuál el mayor o que indique que son iguales.

a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))

if a > b:
    print(f"El mayor es {a} y el menor es {b}")
elif b > a:
    print(f"El mayor es {b} y el menor es {a}")
else:
    print("Ambos números son iguales.")
