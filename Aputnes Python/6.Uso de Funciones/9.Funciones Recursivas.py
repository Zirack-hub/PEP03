# La función recursiva es una función que se manda llamar a si misma para completar una tarea
def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)

numero = int(input('Proporciona el número: '))
resultado = factorial(numero)
print(f'El factorial de {numero} es: {resultado}')