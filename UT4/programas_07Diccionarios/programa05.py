#Crea un diccionario con varios pares clave-valor.
#Recorre las claves con un bucle for.
#Recorre los valores con un bucle for.
#Recorre las claves y valores a la vez usando items().
diccionario_frutas = {"manzana": 5,
                      "banana": 10,
                      "cereza": 20}
print("Recorriendo claves:")
for fruta in diccionario_frutas:
    print(fruta)
print("Recorriendo valores:")

for cantidad in diccionario_frutas.values():
    print(cantidad)
print("Recorriendo claves y valores:")

for clave, valor in diccionario_frutas.items():
    print(clave, "->", valor)

