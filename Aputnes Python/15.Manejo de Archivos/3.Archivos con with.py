from ManejoArchivos import ManejoArchivos

# El comando "with" es como el comando "try" pero más simplificado
with ManejoArchivos('c:\\Users\\Neil\\Desktop\\Cursos de Python\\15.Manejo de Archivos\\prueba.txt') as archivo:
    print(archivo.read())