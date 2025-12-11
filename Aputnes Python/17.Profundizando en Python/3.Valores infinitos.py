# Manejo de valores infinitos
import math
from decimal import Decimal

# La sintaxis de "inf" significa infinito
# En este caso el infinito es positivo
infinito_positivo = float('inf')
print(f'Infinito positivo: {infinito_positivo}')
# Esta sintaxis sirve para saber si el valor es infinito
print(f'Es infinito? {math.isinf(infinito_positivo)}')

# En este caso el infinito es negativo
infinito_negativo = float('-inf')
print(f'Infinito negativo: {infinito_negativo}')
print(f'Es infinito? {math.isinf(infinito_negativo)}')

# Uso de modulo math:
# Este es otro modo de sacar el infinito positivo
infinito_positivo = math.inf
print(f'Infinito positivo: {infinito_positivo}')
print(f'Es infinito? {math.isinf(infinito_positivo)}')

# Este es otro modo de sacar el infinito negativo
infinito_negativo = -math.inf
print(f'Infinito negativo: {infinito_negativo}')
print(f'Es infinito? {math.isinf(infinito_negativo)}')

# Uso de modulo decimal:
# Este es otro modo de sacar el infinito positivo
infinito_positivo = Decimal('Infinity')
print(f'Infinito positivo: {infinito_positivo}')
print(f'Es infinito? {math.isinf(infinito_positivo)}')

# Este es otro modo de sacar el infinito negativo
infinito_negativo = Decimal('-Infinity')
print(f'Infinito negativo: {infinito_negativo}')
print(f'Es infinito? {math.isinf(infinito_negativo)}')