from clases.carrito import Carrito

class Cliente:
    def __init__(self, nombre):
        self._nombre = nombre
        self._carrito = Carrito()

    def agregar_al_carrito(self, producto):
        self._carrito.agregar_producto(producto)

    def ver_total(self):
        return self._carrito.total()

    def ver_carrito(self):
        print(f"Carrito de {self._nombre}:")
        self._carrito.mostrar_productos()