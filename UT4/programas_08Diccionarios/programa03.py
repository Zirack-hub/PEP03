#Crea un diccionario llamado 'agenda' donde las claves sean nombres de personas
#y los valores sus números de teléfono.
#Permite añadir, modificar y eliminar contactos.
#Muestra la agenda completa de forma ordenada (por nombre).
#Implementa la búsqueda de un contacto mostrando su número o un mensaje si no
#existe.


def main():
    agenda={ "Samuel": 123456789,
         "Charlie":987654321,
         "Alvaro":555555555
        }
    flag=True
    while flag:
        print("\n--- MENÚ ---")
        print("1. Añadir")
        print("2. Eliminar")
        print("3. Buscar")
        print("4. Mostrar")
        print("5. Modificar")
        print("6. Salir")

        opcion = int(input("Elige una opción: "))

        match opcion:

            case 1:  # AÑADIR
                añadir(agenda)
                print("El numero se ha insertado correctamente")

            case 2:  # ELIMINAR
                eliminar(agenda)
                print("El contacto se ha borrado")

            case 3:  # BUSCAR
                buscar(agenda)
                

            case 4:  # Mostrar
                mostrar(agenda)
            case 5:  # Modificar
                modificar(agenda)
                flag=False
            
            case 6:  # Salir
                flag=False

            case _:  # OPCIÓN INVÁLIDA
                print("Opción no válida.")



def añadir (agenda):
    nombre = str(input("Introduce el nombre: "))
    numero = int(input("Introduce el nombre: "))

    agenda[nombre] = numero

def eliminar (agenda):
    nombre = str(input("Introduce el nombre a eliminar: "))
    if nombre in agenda:
        del agenda[nombre]
    else:
        print("El contacto que intenta eliminar no existe")

def buscar (agenda):
    nombre = str(input("Introduce el nombre: "))
    if nombre in agenda:
        print(f"El usuario {nombre} tiene el contanto: {agenda[nombre]}")


def modificar (agenda):
    nombre = str(input("Introduce el nombre: "))
    numero = int(input("Introduce el nombre: "))

    agenda[nombre] = numero

def mostrar (agenda):
    agenda_ordenada = sorted(agenda)
    print(agenda_ordenada)



if __name__ == "__main__":
    main()