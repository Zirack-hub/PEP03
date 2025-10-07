try:
    num = int(input("Introduce un número entre 1 y 10: "))
    if num < 1 or num > 10:
        raise ValueError("El número debe estar entre 1 y 10.")
    print(f"Has introducido el número {num}.")
    print(num)
except ValueError as e:
    print("Error:", e)
