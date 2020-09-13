from Tablero import Tablero
from AgenteRK8H1 import AgenteRK8H1
from AgenteH2 import AgenteH2

juego = Tablero()

bus = AgenteH2()
bus.set_estado_inicial([[2, 0, 4], [1, 3, 6], [7, 8, 5]])
bus.set_estado_meta([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

# bus.set_tecnica("costouniforme")
# bus.set_tecnica("codicioso")
bus.set_tecnica("A*")
juego.insertar_objeto(bus)
juego.run()

