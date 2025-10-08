# Escribe un programa donde crees varias funciones y pruebes el ámbito de las variables
# en Python (globales, no locales y locales).

x = 10

def funcion_local():
    x_local = 5
    print(f"[funcion_local] x_local = {x_local}")

def funcion_global():
    global x
    print(f"[funcion_global] Antes: x = {x}")
    x += 20
    print(f"[funcion_global] Después: x = {x}")

def funcion_nonlocal():
    y = 100

    def interna():
        nonlocal y
        print(f"[interna] y antes = {y}")
        y += 50
        print(f"[interna] y después = {y}")

    interna()
    print(f"[funcion_nonlocal] y final = {y}")

print(f"[main] x global inicial = {x}")
funcion_local()
funcion_global()
funcion_nonlocal()
print(f"[main] x global final = {x}")
