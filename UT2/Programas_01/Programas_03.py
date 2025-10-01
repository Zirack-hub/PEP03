# Programa 03
# Escribe un programa que pida dos números y muestre su división.
# Se debe tener en cuenta que no se puede dividir por 0 mostrando en ese caso un aviso.

a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))

if b != 0:
    print("Resultado de la división:", a / b)
else:
    print("Error: no se puede dividir entre 0.")
