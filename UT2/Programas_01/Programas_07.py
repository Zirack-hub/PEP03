# Programa 07
# Escriba un programa que pida un año y que escriba si es bisiesto o no.
# Un año es bisiesto si es múltiplo de 4 pero no múltiplo de 100,
# aunque sí es bisiesto si es múltiplo de 400.

anio = int(input("Introduce un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print(f"El año {anio} es bisiesto.")
else:
    print(f"El año {anio} no es bisiesto.")
