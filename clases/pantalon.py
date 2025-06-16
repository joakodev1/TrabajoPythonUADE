from clases.producto import Producto

class Pantalon(Producto):
    def __init__(self, nombre, precio, talle):
        super().__init__(nombre, precio)
        self._talle = talle

    def get_talle(self):
        return self._talle

    def __str__(self):
        return f"{super().__str__()} - Talle: {self._talle}"