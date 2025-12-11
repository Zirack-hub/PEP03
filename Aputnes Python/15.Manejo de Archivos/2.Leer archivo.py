archivo = open('c:\\Users\\Neil\\Desktop\\Cursos de Python\\15.Manejo de Archivos\\prueba.txt', 'r', encoding='utf8')
# Leer el archivo
# print(archivo.read())

# Leer algunos caracteres
# print(archivo.read(5))

# Leer lineas completas
# print(archivo.readline())

# Repetir el archivo
# for linea in archivo:
#     print(linea)

# Leer líneas
# print(archivo.readlines())

# Acceder a una linea de la lista
# print(archivo.readlines()[0])

# Abrimos un nuevo archivo
# a - anexar información
archivo2 = open('c:\\Users\\Neil\\Desktop\\Cursos de Python\\15.Manejo de Archivos\\copia.txt', 'a', encoding='utf8')
archivo2.write(archivo.read())

archivo.close
archivo2.close
print('Se ha terminado el proceso de leer y copiar')