"""
Versión mejorada del programa principal siguiendo la estructura recomendada:
- Imports organizados (estándar, terceros, propios)
- Definición de la función main()
- Bloque de protección if __name__ == "__main__"
"""

import sys

import operaciones as op


def main():
    """Función principal del programa"""
    print("Operaciones básicas con dos números")
    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))

    print(f"Suma: {op.suma(a, b)}")
    print(f"Resta: {op.resta(a, b)}")
    print(f"Multiplicación: {op.multiplicacion(a, b)}")
    print(f"División: {op.division(a, b)}")


if __name__ == "__main__":
    main()
