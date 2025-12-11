edad = int(input('Introduce tu edad: '))

#veintes = edad >= 20 and edad < 30
#print('Dentro de los 20\'s:', veintes)
#treintas = edad >= 30 and edad < 40
#print('Dentro de los 30\'s:', treintas)

if (20 <= edad < 30) or (30 <= edad < 40):
    print('Dentro de rango (20\'s) o (30\'s)')
    #if veintes:
        #print('Esta dentro de los 20\'s')
    #elif treintas:
        #print('Esta dentro de los 30\'s')
else:
    print("No esta dentro de los 20's ni 30's")