#El programa calculará la media de notas de alumnos/as.
#El programa irá pidiendo nombres de alumnos y su calificación
#Los nombres son ingresados en cualquier orden.
#Si un alumno tiene varias notas se pedirá varias veces su nombre y su calificación.
#Cuando se introduzca un nombre vacío se dejaran de pedir datos y se mostrara los
#nombre de los alumnos y el promedio de la calificación de cada uno

flag = True
alumnos ={}
while flag:
    scannerNombre =str(input("introduce el nombre del alumno (vacio para terminar): "))
    if scannerNombre == "":
        flag = False
    else:
        scannerNota =float(input("introduce la nota del almuno: "))
        if scannerNombre in alumnos:
            alumnos[scannerNombre] = alumnos[scannerNombre]+(scannerNota,)
        else:
            alumnos[scannerNombre]=(scannerNota,)
print(alumnos)
for alumno, nota in alumnos.items():
    print(f"El alumno {alumno} ha sacado una media de {sum(nota)/len(nota)}")

