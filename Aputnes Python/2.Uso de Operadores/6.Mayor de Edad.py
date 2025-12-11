edadAdulto = 18
edadPersona = int(input('Proporciona tu edad: '))

if edadPersona >= edadAdulto:
    print(f'La persona con edad {edadPersona} es mayor de edad')
else:
    print(f'La persona con edad {edadPersona} es menor de edad')