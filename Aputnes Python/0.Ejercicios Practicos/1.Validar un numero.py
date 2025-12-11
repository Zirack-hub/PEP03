def validar_numero():
    while True:
        valor = input('Proporciona un valor: ')

        if valor.isdigit():
            valor = int(valor)
            if valor % 2 == 0:
                print(f'El valor {valor} es número par')
            else:
                print(f'El valor {valor} es número impar')
            return f'El valor es numero entero'
                
        print(f'El valor proporcionado no es valido')

numero = validar_numero()
print(numero)