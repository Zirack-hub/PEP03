"""
Programa principal que utiliza el paquete 'matematicas' para realizar:
- Operaciones básicas.
- Cálculo de áreas geométricas.
"""


from matematicas import (
    suma, resta, multiplicacion, division,
    area_rectangulo, area_triangulo, area_circulo
)

def menu_operaciones():
    print("\n--- Operaciones Matemáticas ---")
    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))

    print(f"Suma: {suma(a, b)}")
    print(f"Resta: {resta(a, b)}")
    print(f"Multiplicación: {multiplicacion(a, b)}")
    print(f"División: {division(a, b)}")

def menu_areas():
    print("\n--- Cálculo de Áreas ---")
    print("1. Rectángulo")
    print("2. Triángulo")
    print("3. Círculo")
    opcion = input("Elige una figura (1-3): ")

    if opcion == "1":
        base = float(input("Base: "))
        altura = float(input("Altura: "))
        print(f"Área del rectángulo: {area_rectangulo(base, altura):.2f}")
    elif opcion == "2":
        base = float(input("Base: "))
        altura = float(input("Altura: "))
        print(f"Área del triángulo: {area_triangulo(base, altura):.2f}")
    elif opcion == "3":
        radio = float(input("Radio: "))
        print(f"Área del círculo: {area_circulo(radio):.2f}")
    else:
        print("Opción no válida.")

def main():
    """Función principal del programa"""
    print("=== MENÚ PRINCIPAL ===")
    print("1. Operaciones matemáticas")
    print("2. Cálculo de áreas geométricas")
    opcion = input("Elige una opción (1-2): ")

    if opcion == "1":
        menu_operaciones()
    elif opcion == "2":
        menu_areas()
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
