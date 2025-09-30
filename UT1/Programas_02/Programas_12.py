# Programa 12
# Sabiendo que 1 milla equivale a 1,61 Km escribe un programa que pida un número
# de millas y un número de Km, muestre respectivamente el número de millas y kilómetros.
# Los resultados deben estar redondeados a 2 decimales.

millas = float(input("Introduce número de millas: "))
km = float(input("Introduce número de km: "))

km_convertidos = millas * 1.61
millas_convertidas = km / 1.61

print(f"{millas} millas son {km_convertidos:.2f} km")
print(f"{km} km son {millas_convertidas:.2f} millas")
