class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    def get_nombre(self):
        return self._nombre

    def get_precio(self):
        return self._precio

    def __str__(self):
        return f"{self._nombre} - ${self._precio}"