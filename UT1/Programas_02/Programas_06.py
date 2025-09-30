# Programa 06
# Escribe un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.

fahrenheit = float(input("Introduce los grados Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9

print(f"{fahrenheit}°F son {celsius:.2f}°C")
