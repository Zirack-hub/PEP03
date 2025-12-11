# Definir nuestra función para multiplicar valores
def multiplicar_valores(*numeros):
    resultado = 1
    # Repetimos cada elemento
    for numero in numeros:
        resultado *= numero
    return resultado

# Llamada de la función
print(f'Resultado de la multiplicación: {multiplicar_valores(3, 5, 15)}')