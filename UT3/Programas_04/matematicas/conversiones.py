"""
Funciones para convertir números entre distintos formatos.
"""

def a_binario(n):
    """Devuelve la representación binaria de un entero."""
    if not isinstance(n, int):
        return "Error: el valor debe ser un número entero."
    return bin(n)[2:]  # elimina el prefijo '0b'

def a_hexadecimal(n):
    """Devuelve la representación hexadecimal de un entero."""
    if not isinstance(n, int):
        return "Error: el valor debe ser un número entero."
    return hex(n)[2:].upper()  # elimina '0x' y pasa a mayúsculas

def a_entero(texto):
    """Convierte una cadena numérica a entero, controlando errores."""
    try:
        return int(texto)
    except ValueError:
        return "Error: la cadena no es un número entero válido."
