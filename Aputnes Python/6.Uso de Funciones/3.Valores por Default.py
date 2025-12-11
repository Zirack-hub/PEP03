# Si usamos valores predeterminados en la función tenemos que definir los valores al mostrar la función
def sumar(a = 0, b = 0):
    return a + b

resultado = sumar()
print(f'Resultado de la suma: {resultado}')

print(f'Resultado de la suma: {sumar(2, 8)}')