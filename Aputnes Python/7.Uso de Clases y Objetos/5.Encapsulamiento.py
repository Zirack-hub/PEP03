class Persona:
    def __init__(self, nombre, apellido, edad):
        # Si se pone "self.__valor" no se podra modificar el valor fuera de la clase
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
    
    # El metodo get sirve para obtener los atributos de una clase
    @property
    def nombre(self):
        return self._nombre

    # El metodo set sirve para modificar los atributos de una clase
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        self._edad = edad
    
    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self.apellido} {self.edad}')

persona1 = Persona('Juan', 'Perez', 28)
persona1.nombre = 'Luis'
print(persona1.nombre)

persona1.apellido = 'Bermejo Lara'
print(persona1.apellido)

persona1.edad = '18'
print(persona1.edad)