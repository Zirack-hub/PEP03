# Metodo format
nombre = 'Juan'
edad = 28
sueldo = 3000
mensaje_con_formato = 'Nombre: {}, Edad: {}, Sueldo: {:.2f}€'.format(nombre, edad, sueldo)
print(mensaje_con_formato)

mensaje_con_formato = 'Nombre: {0}, Edad: {1}, Sueldo: {2:.2f}€'.format(nombre, edad, sueldo)
print(mensaje_con_formato)

mensaje_con_formato = 'Sueldo: {2:.2f}€, Nombre: {0}, Edad: {1}'.format(nombre, edad, sueldo)
print(mensaje_con_formato)

mensaje_con_formato = 'Nombre: {n}, Edad: {e}, Sueldo {s:.2f}€'.format(n=nombre, e=edad, s=sueldo)
print(mensaje_con_formato)

# Metodo format usando un diccionario
diccionario = {'nombre':'Ivan', 'edad':35, 'sueldo':8000.00}
mensaje_con_formato = 'Nombre: {dic[nombre]}, Edad: {dic[edad]}, Sueldo: {dic[sueldo]:.2f}€'.format(dic=diccionario)
print(mensaje_con_formato)