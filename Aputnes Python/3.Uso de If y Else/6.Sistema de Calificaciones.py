nota = int(input('Proporciona tu nota: '))
calificacion = None

if (nota >= 0) and (nota < 6):
    calificacion = 'F'
elif (nota >= 6) and (nota < 7):
    calificacion = 'D'
elif (nota >= 7) and (nota < 8):
    calificacion = 'C'
elif (nota >= 8) and (nota < 9):
    calificacion = 'B'
elif (nota >= 9) and (nota <= 10):
    calificacion = 'A'
elif (nota == 11):
    calificacion = 'S'
else:
    calificacion = 'Valor incorrecto'

print(f'Tu nota es: {nota}, Tu calificación es: {calificacion}')