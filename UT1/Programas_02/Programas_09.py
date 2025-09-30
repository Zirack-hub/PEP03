# Programa 09
# Escribe un programa que calcule la calificación de estudiante en un módulo.
# La calificación se obtiene de la calificación parcial en cada RA (RA1 20%, RA2 60% y RA3 20%).

ra1 = float(input("Introduce calificación RA1 (20%): "))
ra2 = float(input("Introduce calificación RA2 (60%): "))
ra3 = float(input("Introduce calificación RA3 (20%): "))

calificacion = ra1 * 0.2 + ra2 * 0.6 + ra3 * 0.2

print(f"La calificación final del módulo es: {calificacion:.2f}")
