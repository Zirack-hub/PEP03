#Declara una cadena " Hola Mundo ".
#Aplica y muestra los resultados de: upper(), lower(), capitalize(),title().
#Elimina espacios con strip().
#Sustituye "Mundo" por "Python" con replace().
#Divide la cadena en palabras con split().
#Une una lista de palabras con join().
cadena = " Hola Mundo "
print("Cadena original:", repr(cadena))
print("Mayúsculas:", cadena.upper())
print("Minúsculas:", cadena.lower())
print("Primera letra mayúscula:", cadena.capitalize())
print("Título:", cadena.title())
cadena_sin_espacios = cadena.strip()
print("Sin espacios:", repr(cadena_sin_espacios))
cadena_reemplazada = cadena.replace("Mundo", "Python")
print("Cadena reemplazada:", repr(cadena_reemplazada))
palabras = cadena.strip().split()
print("Cadena dividida en palabras:", palabras)
cadena_unida = "-".join(palabras)
print("Cadena unida con '-':", cadena_unida)