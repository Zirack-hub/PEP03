# Definir nuestra función para sumar valores
def sumar_valores(*args):
    resultado = 0
    # Repetimos cada elemento
    for valor in args:
        resultado += valor
    return resultado

# Llamada de la función
print(f'Resultado de la suma: {sumar_valores(3, 5, 9, 4, 6)}')