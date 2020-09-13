from AgenteRK8 import AgenteRK8


class AgenteH2(AgenteRK8):
    # Heuristica: distancia manhatan
    def get_heuristica(self, camino):
        can = 0
        tablero = camino[-1]
        for x in range(3):
            for y in range(3):
                actual = (self.find_num(tablero,tablero[x][y]))
                esperado = (self.find_num(self.estadoMeta,tablero[x][y]))
                can += self.cant(tablero, actual, esperado)
        return can