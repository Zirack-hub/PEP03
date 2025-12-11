from NumerosIdenticosException import NumerosIdenticosException

resultado = None

# Se puede capturar un error o excepción con el siguiente comando:
try:
    a = int(input('Primer número: '))
    b = int(input('Segundo número: '))
    if a == b:
        raise NumerosIdenticosException('Números Idénticos')
    resultado = a / b
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrió un error: {e}')
except TypeError as e:
    print(f'TypeError - Ocurrió un error: {e}')
except Exception as e:
    print(f'Exception - Ocurrió un error: {e}')
else:
    print('No se ha mostrado ningúna excepción')
finally:
    print('Ejecución del bloque finally')

print(f'Resultado: {resultado}')
print('Continuamos...')