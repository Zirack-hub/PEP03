# Programa 04
# Escribe un programa que pregunte la base y altura de un rectángulo y calcule su área y perímetro.

base = float(input("Introduce la base del rectángulo: "))
altura = float(input("Introduce la altura del rectángulo: "))

area = base * altura
perimetro = 2 * (base + altura)

print("Área:", area)
print("Perímetro:", perimetro)
