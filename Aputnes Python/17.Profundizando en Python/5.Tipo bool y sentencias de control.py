# bool contiene los valores de True y False
# Tipos numericos, False para 0, True demás valores
valor = 0
resultado_numerico = bool(valor)
# print(f'Valor {valor}, resultado numerico: {resultado_numerico}')
valor = 15
resultado_numerico = bool(valor)
# print(f'Valor {valor}, resultado numerico: {resultado_numerico}')

# Tipo str, False para '', True demás valores
valor = ''
resultado_str = bool(valor)
print(f'Valor {valor}, resultado str: {resultado_str}')
valor = 'Hola'
resultado_str = bool(valor)
print(f'Valor {valor}, resultado str: {resultado_str}')

# Tipo colecciones, False para colecciones vacias, True para todas las demás colecciones
# Lista
valor = []
resultado_lista = bool(valor)
print(f'Valor {valor}, resultado lista: {resultado_lista}')
valor = [2,3,4]
resultado_lista = bool(valor)
print(f'Valor {valor}, resultado lista: {resultado_lista}')

# Tupla
valor = ()
resultado_tupla = bool(valor)
print(f'Valor {valor}, resultado tupla: {resultado_tupla}')
valor = (2,3,4)
resultado_tupla = bool(valor)
print(f'Valor {valor}, resultado tupla: {resultado_tupla}')

# Diccionario
valor = {}
resultado_diccionario = bool(valor)
print(f'Valor {valor}, resultado diccionario: {resultado_diccionario}')
valor = {'nombre':'Juan', 'apellido':'Perez'}
resultado_diccionario = bool(valor)
print(f'Valor {valor}, resultado diccionario: {resultado_diccionario}')

variable = 10
if bool(variable):
    print('Regresó verdadero')
else:
    print('Regreó falso')

if variable:
    print('Regresó verdadero')
else:
    print('Regresó falso')

while variable:
    print('Ejecución ciclo while')
    break
else:
    print('Fin ciclo while')