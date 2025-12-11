class Aritmetica:
    # Clase Aritmética para realizar las operaciones de sumar, restar, etc
    
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB
    
    def restar(self):
        return self.operandoA - self.operandoB
    
    def multiplicar(self):
        return self.operandoA * self.operandoB
    
    def dividir(self):
        return self.operandoA / self.operandoB

operandoA = int(input('Proporciona el numero 1: '))
operandoB = int(input('Proporciona el numero 2: '))
aritmetica1 = Aritmetica(operandoA, operandoB)
print(f'Suma: {aritmetica1.sumar()}')
print(f'Resta: {aritmetica1.restar()}')
print(f'Multiplicación: {aritmetica1.multiplicar()}')
print(f'División: {aritmetica1.dividir():.2f}')