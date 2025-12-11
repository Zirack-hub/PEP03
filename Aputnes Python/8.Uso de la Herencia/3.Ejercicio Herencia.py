# Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Coche y Bicicleta, las cuales heredan de la clase Padre Vehiculo.
# La clase padre debe tener los siguientes atributos y métodos

# Vehiculo (Clase Padre):
# -Atributos (color, ruedas)
# -Métodos ( __init__() y __str__ )

class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return f'Vehiculo: [Color: {self.color}, Ruedas: {self.ruedas}]'

# Coche  (Clase Hija de Vehículo) (Además de los atributos y métodos heradados de Vehículo):
# -Atributos ( velocidad (km/hr) )
# -Métodos ( __init__() y __str__() )

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
    
    def __str__(self):
        return f'Coche: [Velocidad: {self.velocidad} km/h] {super().__str__()}'

# Bicicleta  (Clase Hija de Vehículo) (Además de los atributos y métodos heradados de Vehículo):
# -Atributos ( tipo (urbana/montaña/etc )
# -Métodos ( __init__() y __str__() )

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return f'Bicicleta: [Tipo: {self.tipo}] {super().__str__()}'

# Creamos un objeto de la clase Vehiculo

colorVehiculo = input('Proporciona el color del vehiculo: ')
ruedasVehiculo = int(input('Proporciona las ruedas del vehiculo: '))

vehiculo1 = Vehiculo(colorVehiculo, ruedasVehiculo)
print(vehiculo1)

# Creamos un objeto de la clase Coche

colorCoche = input('Proporciona el color del coche: ')
ruedasCoche = int(input('Proporciona las ruedas del coche: '))
velocidadCoche = int(input('Proporciona la velocidad del coche: '))

coche1 = Coche(colorCoche, ruedasCoche, velocidadCoche)
print(coche1)

# Creamos un objeto de la clase Bicicleta

colorBicicleta = input('Proporciona el color de la bicicleta: ')
ruedasBicicleta = int(input('Proporciona las ruedas de la bicicleta: '))
tipoBicicleta = input('Proporciona el tipo de bicicleta: ')

bicicleta1 = Bicicleta(colorBicicleta, ruedasBicicleta, tipoBicicleta)
print(bicicleta1)