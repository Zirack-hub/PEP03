"""
Paquete matematicas
-------------------
Contiene módulos con funciones de operaciones básicas, figuras geométricas y conversiones.
"""

from .operaciones import suma, resta, multiplicacion, division
from .figuras import area_rectangulo, area_triangulo, area_circulo
from .conversiones import a_binario, a_hexadecimal, a_entero

__all__ = [
    "suma", "resta", "multiplicacion", "division",
    "area_rectangulo", "area_triangulo", "area_circulo",
    "a_binario", "a_hexadecimal", "a_entero"
]
