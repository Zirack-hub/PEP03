# ============================================================
# RESUMEN PYTHON: U4, U5 y U6
# ============================================================
# >>=============== Modificar Cadenas ==============>
titulo = "Ark Survival Evolved"
print(f"Titulo en Minuscula y sin espacios: \n{titulo.replace(" ", "").lower()}")
print("\n")
# >>=============== Listas, Tuplas y Diccionarios ==============>
lista = [1, 2, 3, 4]
tupla = (5, 6, 7) #Inmutable
conjunto = {1, 2, 3, 3, 3, 2, 4} # Omite datos repetidos
diccionario = {"nombre": "Ana", "edad": 20} # Array Asociativo
print("Primer elemento de lista:", lista[0])
print("Tupla :", tupla)
print(f"Ultimo Índice de Tupla: {tupla[len(tupla) - 1]}")
print("Conjunto :", conjunto)
print("Diccionario:", diccionario["nombre"])
print("\n")
#>>================= Rangos =======================>
print('Rango de 0 a 4 con numeros divisibles entre 2')
for i in range(5):
    if i % 2 == 0:
        print(i,end=", ")
print("\n")
print('Rango de 2 a 4')
for i in range(2,5):
    print(i,end=", ")
print("\n")
print('Rango de 3 a 7 incrementando de 2 en 2')
for i in range(3,8,2):
    print(i,end=", ")
print("\n")
#>>================= Gestionar Archivos (txt) =======================>
# r => Lectura
# w => Escribir (borra contenido anterior)
# a => Añadir (se situal al final del fichero)
# r+ => Leer y actualizar (mantiene contenido anterior)
# w+ => Escribir y actualizar (borra contenido anterior)
try:
    # fichero_txt = open("nombres.txt", "r")
    # fichero_txt.close()
    with open("nombres.txt","w+") as fichero_txt:
        # lee el fichero en una variable
        hola = fichero_txt.read()
        print(hola)
        # mueve el puntero del fichero a una posicion (en este caso lo mueve al inicio, posicion "0")
        fichero_txt.seek(0)
        # escribe texto en el fichero
        fichero_txt.write("Escribo Linea")
        fichero_txt.seek(0)
        hola = fichero_txt.read()
        print(hola)
except Exception as ex:
    print("No se puede abrir el archivo:", ex)
print("\n")
#>>================= Accesso a BD MySQL =======================>
# Entorno Virtual:
#       python3 -m venv .venv
#       source .venv/bin/activate
#       pip list
#       deactivate
# Instalar Conector a BD:
#       pip install mysql-connector-python
#>>================= Programación Orientada a Objetos  =======================>
# ------------ Decorador ---------------------------
def decorador(f):
    def funcion_nueva():
        print("Funcionalidad extra")
        f() #funcion que a la que se le va a añadir funcionalidad extra
    return funcion_nueva
@decorador
def funcion_inicial():
    print("Funcionalidad inicial")
funcion_inicial()
print("\n")
# ------------ Metodo de Clase ---------------------------
class Rectangulo:
    lados = 4 # Atributo de clase
    rectangulos = 0 # Atributo de clase para contar instancias
    def __init__(self, base, altura): #constructor ("self" es obligatorio)
        self.base = base # Atributo de instancia
        self.altura = altura # Atributo de instancia
        Rectangulo.rectangulos += 1 # Incrementar el contador de instancias
    def area(self):
        return self.base * self.altura
    @classmethod # Indica que es un metodo de la clase
    def contar_rectangulos(cls):
        return cls.rectangulos
    # Crear una instancia de Rectangulo
    @staticmethod #Metodo estatico de la clase
    def es_mayor_de_edad(edad):
        return edad >= 18
rectangulo1 = Rectangulo(5, 10)
rectangulo2 = Rectangulo(3, 6)
rectangulo3 = Rectangulo(4, 8)
print(f"Hay {Rectangulo.contar_rectangulos()} rectángulos creados.\n")
print(Rectangulo.es_mayor_de_edad(17)) # Salida: False
print(Rectangulo.es_mayor_de_edad(20)) # Salida: True
print("\n")
#>>================= Programación Orientada a Objetos  =======================>
# ------------ Dunder ---------------------------
# __lt__(), __le__(), __gt__(), __ge__(), __eq__(), __ne__()
# ( <, <=, >, >=, ==, !=)
# ----------------- Iteradores -------------------------
class Contador:
    def __init__(self, inicio, fin):
        self.actual = inicio
        self.fin = fin
    def __iter__(self):
        return self
    def __next__(self):
        if self.actual <= self.fin:
            valor = self.actual
            self.actual += 1
            return valor
        else:
            raise StopIteration
for num in Contador(1, 5):
    print(num)
#>>================= Programación Orientada a Objetos  =======================>
#>>================= Programación Orientada a Objetos  =======================>
#>>================= Programación Orientada a Objetos  =======================>
