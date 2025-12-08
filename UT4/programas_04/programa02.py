#Escribe un programa en Python que guarde la temperatura mínima y máxima de 5 días en
#una lista de dos dimensiones y a continuación muestre.
#• La temperatura media de cada día.
#• Los días con menos temperatura.
#• Se lea una temperatura por teclado y se muestran los días cuya temperatura
#    máxima coincide con ella. Si no existe ningún día se muestra un mensaje
#    de .información

temperaturasMaximas = [15.5, 16.8, 20, 11, 10]
temperaturasMinimas = [2.5, 1.2, 5, -2, -3.5]
temperaturasTotales = [temperaturasMinimas,temperaturasMaximas]
temperaturasMedias =[]
diafrio = min(temperaturasTotales[0])
diacaliente = max(temperaturasTotales[1])

for i in range(5):
    print(f"Día {i+1}: máxima = {temperaturasTotales[1][i]} °C, mínima = {temperaturasTotales[0][i]} °C")
for i in range(5):
    mediaDiaria = (temperaturasTotales[0][i]+temperaturasTotales[1][i])/2
    temperaturasMedias.append(mediaDiaria)

for i in range (len(temperaturasMedias)):
    print(f"Día {i+1}: Media: {temperaturasMedias[i]}")

print (f"La temperatura mas fria es de: {diafrio}")
print (f"La temperatura mas caliente es de: {diacaliente}")

diaIntro = num = float(input("Introduce una temperatura: "))
if diaIntro in temperaturasTotales[1]:
    print(f"El dia que has introducido es {temperaturasTotales[1].index(diaIntro)+1}")
else:
    print("No hay ningun dia con la temperatura introducida")



    