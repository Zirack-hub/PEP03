edad = int(input('Proporciona tu edad: '))
etapa = None

if (edad >= 0) and (edad <= 10):
    etapa = 'Niño'
elif (edad >= 10) and (edad <= 20) :
    etapa = 'Adolescente'
elif (edad >= 20) and (edad <= 70):
    etapa = 'Adulto'
elif (edad >= 70) and (edad <= 100):
    etapa = 'Anciano'
else:
    etapa = 'Mentiroso'
print(f'Tu edad es: {edad}, Eres un: {etapa}')