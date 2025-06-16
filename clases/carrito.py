class Carrito:
    def __init__(self):
        self._productos = []

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def total(self):
        return sum([p.get_precio() for p in self._productos])

    def mostrar_productos(self):
        for producto in self._productos:
            print(producto)