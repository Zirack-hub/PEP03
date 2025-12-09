#Crea un diccionario 'persona' que contenga otro diccionario 'direccion' como valor.
#Accede a un elemento del diccionario anidado (por ejemplo, número de la calle).
#Crea un diccionario 'familia' con varios miembros (cada uno con sus propios datos).
#Muestra los datos de cada miembro recorriendo el diccionario
persona = {
    "nombre": "Rizwan",
    "edad": 78,
    "direccion": {
        "calle": "Calle Falsa 123",
        "ciudad": "Springfield",
        "código_postal": "12345"
        }
}
print("Número de la calle:", persona["direccion"]["calle"])
print("Ciudad: ", persona["direccion"]["ciudad"])
familia = {
    "padre": {"nombre": "Rizwan", "edad": 78},
    "madre": {"nombre": "Aisha", "edad": 75},
    "hijo": {"nombre": "Omar", "edad": 50},
    "hija": {"nombre": "Lina", "edad": 45}
}
for miembro, datos in familia.items():
    print(f"{miembro.capitalize()}: Nombre - {datos['nombre']}, Edad - {datos['edad']}")
