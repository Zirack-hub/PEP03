# Una variable de clase se asocia con la clase
class MiClase:

    variable_clase = 'Valor variable clase'

    def __init__(self, variable_instancia):
        # Una variable de instancia se asocia con los objetos
        self.variable_instancia = variable_instancia

print(MiClase.variable_clase)
miClase1 = MiClase('Valor variable instancia')
print(miClase1.variable_instancia)
print(miClase1.variable_clase)

# Se puede asociar variables al vuelo
MiClase.variable_clase2 = 'Valor variable clase 2'

miClase2 = MiClase('Otro valor de variable instancia')
print(miClase2.variable_instancia)
print(miClase2.variable_clase)
print(MiClase.variable_clase2)
print(miClase1.variable_clase2)
print(miClase2.variable_clase2)