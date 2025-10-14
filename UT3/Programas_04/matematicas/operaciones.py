"""
operaciones.py
---------------
Módulo que contiene funciones básicas de operaciones matemáticas:
- suma(a, b)
- resta(a, b)
- multiplicacion(a, b)
- division(a, b)
"""

def suma(a, b):
    """Devuelve la suma de dos números."""
    return a + b


def resta(a, b):
    """Devuelve la resta de dos números."""
    return a - b


def multiplicacion(a, b):
    """Devuelve la multiplicación de dos números."""
    return a * b


def division(a, b):
    """Devuelve la división de dos números. Controla la división entre cero."""
    if b == 0:
        return "Error: no se puede dividir entre cero."
    return a / b