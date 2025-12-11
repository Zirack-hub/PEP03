#Profundizando en el tipo float
tipo_float = 3.0
print(f'tipo_float: {tipo_float:.2f}')

# Constructor float puede recibir int  y str
tipo_float_int = float(10)
print(f'tipo_float_int: {tipo_float_int:.2f}')
tipo_float_str = float('10')
print(f'tipo_float_str: {tipo_float_str:.2f}')

# Notación exponencial (valores positivos o negativos)
tipo_float_positivo = 3e5
print(f'tipo_float_positivo: {tipo_float_positivo:.2f}')
tipo_float_negativo = 3e-5
print(f'tipo_float_negativo: {tipo_float_negativo:.5f}')

# Cualquier cálculo que involucre un float, se convierte en tipo float
calculo_float = 4 + 5.0
print(calculo_float)
print(type(calculo_float))