# Programa 01
# Escribe un programa que pida primero un número par y luego un número impar (positivos
# o negativos). En caso de que uno o los dos valores no sea correcto, se mostrará un aviso.

par = int(input("Introduce un número par: "))
impar = int(input("Introduce un número impar: "))

if par % 2 == 0 and impar % 2 != 0:
    print("Correcto: se han introducido un número par y un número impar.")
else:
    print("Error: el primero debe ser par y el segundo impar.")
