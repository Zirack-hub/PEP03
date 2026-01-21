def main():
    inventario =crear_inventario()
    agregar_producto(inventario, "P001", "Portatil", 1200)
    agregar_producto(inventario, "P001", "Portatil", 1200)
    agregar_producto(inventario, "P002", "Teclado", 50)
    actualizar_precio(inventario, "P001", 1150.50)
    actualizar_precio(inventario, "P002", 16.00)
    obtener_producto(inventario, "P001")

def crear_inventario():
    inventario = {}
    return inventario
    
def obtener_producto(inventario, codigo):
    if codigo in inventario:
        producto = inventario[codigo]
        return producto
        
    else:
        raise ValueError("EL CODIGO NO ESTA EN EL INVENTARIO")

def agregar_producto(inventario, codigo, nombre, precio_inicial):
    if codigo not in inventario:
        inventario[codigo]= (nombre, [precio_inicial,])
        return True
    else:
        return False

def actualizar_precio(inventario, codigo, nuevo_precio):
    if codigo in inventario:
        inventario[codigo][1].append(nuevo_precio)
        return True
    else:
        return False

def obtener_producto(inventario, codigo):
    if codigo in inventario:
        print(f"Ha seleccionado el producto: {inventario[codigo][0]}, con un precio de {inventario[codigo][1][-1]}")
        return True
    else:
        return False
if __name__ == "__main__":
    main()