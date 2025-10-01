# Programa 06
# Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.

dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
anio = int(input("Introduce el año: "))

valida = True

# Días máximos por mes
if mes < 1 or mes > 12:
    valida = False
elif mes in [1, 3, 5, 7, 8, 10, 12]:
    if not (1 <= dia <= 31):
        valida = False
elif mes in [4, 6, 9, 11]:
    if not (1 <= dia <= 30):
        valida = False
elif mes == 2:
    # Año bisiesto
    bisiesto = (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)
    if bisiesto:
        if not (1 <= dia <= 29):
            valida = False
    else:
        if not (1 <= dia <= 28):
            valida = False

if valida:
    print("La fecha es correcta.")
else:
    print("La fecha no es válida.")
