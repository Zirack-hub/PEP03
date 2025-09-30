# Programa 02
# Escribe un programa que:
# - Cree una variable que almacene el número entero 6.
# - Muestre por pantalla el tipo del objeto que contiene el número 6, y el tipo del objeto al que apunta la variable.
# - Cree otra variable a la que se asigne la primera variable.
# - Muestre por pantalla el tipo del objeto que contiene el número 6 y el tipo del objeto al que apunta la variable.
# - Utilice los operadores de identidad (is e is not) para comprobar que las dos variables apuntan al mismo objeto.
# - Asigne la cadena "Hola" a la primera variable.
# - Muestre el tipo del objeto que contiene la cadena "Hola" y el tipo del objeto al que apunta la variable.
# - Utilice la función isinstance() para comprobar el tipo de ambas variables.

var1 = 6
print("Valor var1:", var1, "Tipo:", type(var1))

var2 = var1
print("Valor var2:", var2, "Tipo:", type(var2))

print("var1 is var2:", var1 is var2)
print("var1 is not var2:", var1 is not var2)

var1 = "Hola"
print("Valor var1:", var1, "Tipo:", type(var1))
print("Valor var2:", var2, "Tipo:", type(var2))

print("var1 es str?", isinstance(var1, str))
print("var2 es int?", isinstance(var2, int))
