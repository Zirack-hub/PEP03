# Se puede crear clases para el manejo de excepciones
class NumerosIdenticosException(Exception):
    
    def __init__(self, mensaje):
        self.message = mensaje