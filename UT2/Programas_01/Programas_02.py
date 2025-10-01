# Programa 02
# Escribe un programa que pida primero un número par (positivo o negativo) y si el valor no
# es correcto, muestre un aviso. Si el valor es correcto, pedirá un número impar y si el valor
# no es correcto, mostrará un aviso.

par = int(input("Introduce un número par: "))

if par % 2 == 0:
    impar = int(input("Introduce un número impar: "))
    if impar % 2 != 0:
        print("Correcto: par e impar introducidos.")
    else:
        print("Error: el segundo número debe ser impar.")
else:
    print("Error: el primer número debe ser par.")
