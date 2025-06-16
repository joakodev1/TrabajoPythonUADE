from clases.remera import Remera
from clases.pantalon import Pantalon
from clases.campera import Campera
from clases.cliente import Cliente

cliente = Cliente("Franco")

remera = Remera("Remera oversize", 12000, "L")
pantalon = Pantalon("Jogger", 18000, "32")
campera = Campera("Campera rompeviento", 25000, True)

cliente.agregar_al_carrito(remera)
cliente.agregar_al_carrito(pantalon)
cliente.agregar_al_carrito(campera)

cliente.ver_carrito()
print("Total de la compra:", cliente.ver_total())