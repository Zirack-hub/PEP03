# codigos1 = [1, 2, 3, 4]
# codigos2 = [1, 4, 6]

# for codigo in codigos1:
#     if codigo in codigos2:
#         print(f'Números encontrados: {codigo}')
    
print('Rango de 1 a 1000')
lista = []
a = int(input('Proporciona un numero: '))
b = int(input('Proporciona un numero: '))

for i in range(a,b):
    lista.append(i)
    if a > 0 and b < 1001:
        print('El rango es valido')
    else:
        print('El rango no es valido')
    break