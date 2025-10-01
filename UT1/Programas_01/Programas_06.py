"""Escribe un programa que use varias veces la función printf() para

Mostrar las operaciones del los operadores aritméticos de Python entre dos
números.

Mostrar las operaciones de los operadores lógicos de Python con valores
booleanos.

Mostrar las operaciones de los operadores de comparación de Python con valores
booleanos y/o números."""


# Programa demostrativo de operadores en Python

a = 10
b = 3

print("=== Operadores Aritméticos ===")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")     
print(f"{a} // {b} = {a // b}")  
print(f"{a} % {b} = {a % b}")    
print(f"{a} ** {b} = {a ** b}")  

x = True
y = False

print("\n=== Operadores Lógicos ===")
print(f"{x} and {y} = {x and y}")
print(f"{x} or {y}  = {x or y}")
print(f"not {x}     = {not x}")

print("\n=== Operadores de Comparación ===")
print(f"{a} == {b} → {a == b}")
print(f"{a} != {b} → {a != b}")
print(f"{a} > {b}  → {a > b}")
print(f"{a} < {b}  → {a < b}")
print(f"{a} >= {b} → {a >= b}")
print(f"{a} <= {b} → {a <= b}")

# Comparaciones con booleanos
print(f"{x} == {y} → {x == y}")
print(f"{x} != {y} → {x != y}")
