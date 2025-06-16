from clases.producto import Producto

class Campera(Producto):
    def __init__(self, nombre, precio, es_impermeable):
        super().__init__(nombre, precio)
        self._es_impermeable = es_impermeable

    def es_impermeable(self):
        return self._es_impermeable

    def __str__(self):
        estado = "Impermeable" if self._es_impermeable else "No impermeable"
        return f"{super().__str__()} - {estado}"