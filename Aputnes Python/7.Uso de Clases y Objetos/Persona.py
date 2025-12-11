class Persona:
    def __init__(self, nombre, apellido, edad):
        # Si se pone "self.__valor" no se podra modificar el valor fuera de la clase
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
    
    # El metodo get sirve para obtener los atributos de una clase
    @property
    def nombre(self):
        # print('Llamando método get nombre')
        return self._nombre

    # El metodo set sirve para modificar los atributos de una clase
    @nombre.setter
    def nombre(self, nombre):
        # print('Llamando método set nombre')
        self._nombre = nombre
    
    @property
    def apellido(self):
        # print('Llamando método get apellido')
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido):
        # print('Llamando método set apellido')
        self._apellido = apellido
    
    @property
    def edad(self):
        # print('Llamando método get edad')
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        # print('Llamando método set edad')
        self._edad = edad
    
    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')
    
    def __del__(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')

if __name__ == '__main__':
    persona1 = Persona('Juan', 'Perez', 28)
    persona1.nombre = 'Luis'
    persona1.apellido = 'Bermejo Lara'
    persona1.edad = '18'
    persona1.mostrar_detalle()

    print(__name__)