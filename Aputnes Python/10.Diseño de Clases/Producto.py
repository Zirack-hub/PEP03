class Producto:
    contador_productos = 0

    def __init__(self, nombre, precio):
        Producto.contador_productos += 1
        self._id_producto = Producto.contador_productos
        self._nombre = nombre
        self._precio = precio
    
    @property
    def id_producto(self):
        return self._id_producto

    @id_producto.setter
    def id_producto(self, id_producto):
        if self._validar_valor(id_producto):
            self._id_producto = id_producto
        else:
            print(f'Valor erroneo id_producto: {id_producto}')
    
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if self._validar_valor(nombre):
            self._nombre = nombre
        else:
            print(f'Valor erroneo nombre: {nombre}')
    
    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        if self._validar_valor(precio):
            self._precio = precio
        else:
            print(f'Valor erroneo precio: {precio}')

    def __str__(self):
        return f'[Id Producto: {self._id_producto}, Nombre: {self._nombre}, Precio: {self._precio}€]'

if __name__ == '__main__':
    producto1 = Producto('Camiseta', 40.00)
    print(producto1)
    producto2 = Producto('Pantalón', 60.00)
    print(producto2)