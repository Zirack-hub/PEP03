# Un objeto es un elemento que tiene varios valores distintos
class Persona:
    # El metodo "__init__" es el metodo iniciador
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        # Agregar los atributos
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos
    
    # Agregar los metodos
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')

# Nombrar los atributos de un objeto
persona1 = Persona('Juan', 'Perez', 28, '1', '2', '3', m='manzana', p='pera')
persona1.mostrar_detalle()
# persona1.telefono = '555227552'
# print(persona1.telefono)

# Acceder a los atributos de un objeto
print(f'Objeto Persona 1: {persona1.nombre} {persona1.apellido} tiene {persona1.edad} años')

# Modificar los valores de un objeto
# persona1.nombre = 'Juan Carlos'
# persona1.apellido = 'Juarez'
# persona1.edad = 25
# print(f'Objeto Persona 1: {persona1.nombre} {persona1.apellido} tiene {persona1.edad} años')

# Nombrar los atributos de un objeto
persona2 = Persona('Karla', 'Gomez', 30)
persona2.mostrar_detalle()

# Acceder a los atributos de un objeto
print(f'Objeto Persona 2: {persona2.nombre} {persona2.apellido} tiene {persona2.edad} años')

# Modificar los valores de un objeto
# persona2.nombre = 'Laura'
# persona2.apellido = 'Gonzalez'
# persona2.edad = 23
# print(f'Objeto Persona 2: {persona2.nombre} {persona2.apellido} tiene {persona2.edad} años')