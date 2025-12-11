# El comando "from "nombre_archivo" import "nombre_clase"" sirve para llamar a una clase de otro archivo
from Persona import Persona

print('Creación de objetos'.center(26,'-'))
persona1 = Persona('Karla', 'Gomez', 30)
persona1.mostrar_detalle()

print('Eliminación de objetos'.center(26,'-'))
del persona1

# Comprobar el módulo principal
print(__name__)
