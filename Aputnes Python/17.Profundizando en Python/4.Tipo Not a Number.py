import math
from decimal import Decimal

# NaN - Not a Number
# NaN no es sensible a mayúsculas o minúsculas
# NaN es un tipo de dato númerico indefinido
Not_a_Number = float('NaN')
print(f'Not_a_Number: {Not_a_Number}')
print(f'Es NaN (Not a Number)? {math.isnan(Not_a_Number)}')

Not_a_Number_Decimal = Decimal('NaN')
print(f'Not_a_Number_Decimal: {Not_a_Number_Decimal}')
print(f'Es NaN (Not a Number)? {math.isnan(Not_a_Number_Decimal)}')