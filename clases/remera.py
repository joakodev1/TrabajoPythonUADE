from clases.producto import Producto

class Remera(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self._talla = talla

    def get_talla(self):
        return self._talla

    def __str__(self):
        return f"{super().__str__()} - Talla: {self._talla}"