print('Proporcione los siguientes datos del libro:')
nombre = input('Proporciona el nombre: ')
id = int(input('Proporciona el ID: '))
precio = float(input('Proporciona el precio: '))
envioGratuito = input('Indica si el envio es gratuito (True/False): ')

if envioGratuito == 'True':
    envioGratuito = True
elif envioGratuito == 'False':
    envioGratuito = False
else:
    envioGratuito = 'Valor incorrecto, debe escribir True/False'

print(f'''
    Nombre: {nombre}
    Id: {id}
    Precio: {precio}
    Envío Gratuito? {envioGratuito}
''')