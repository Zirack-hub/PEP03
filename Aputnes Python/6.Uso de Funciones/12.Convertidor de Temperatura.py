# Funcion que convierte de celsius a fahrenheit
def celsius_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

# Funcion que convierte de fahrenheit a celsius
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

# Calculadora de celsius a fahrenheit
celsius = float(input('Proporciona los grados celsius: '))
resultado = celsius_fahrenheit(celsius)
# En este caso ":0.2f" sirve para decir que del lado izquierdo pueden haber todos los numeros que se quiera, pero del lado derecho solo haya dos
print(f'{celsius} C son: {resultado:0.2f} F')

# Calculadora de fahrenheit a celsius
fahrenheit = float(input('Proporciona los grados fahrenheit: '))
resultado = fahrenheit_celsius(fahrenheit)
print(f'{fahrenheit} F son: {resultado:0.2f} C')