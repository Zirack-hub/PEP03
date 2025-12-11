class MiClase:

    variable_clase = 'Valor variable clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
    
    # El metodo estático no puede acceder ni a los metodos de instancia, ni a las variables de instancia porque no recibe el parametro de self y no tiene información relacionada con la clase
    # Solo puede llamar a la variable de clase, llamando primero a la clase
    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)

    # El metodo de clase es parecido al metodo estático pero, tiene información relacionada con la clase
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)
    
    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variable_instancia)

MiClase.metodo_estatico()

MiClase.metodo_clase()
miObjeto1 = MiClase('Valor variable instancia')
miObjeto1.metodo_clase()
miObjeto1.metodo_instancia()