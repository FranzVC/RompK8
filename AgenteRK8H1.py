from AgenteRK8 import AgenteRK8


class AgenteRK8H1(AgenteRK8):

    def get_heuristica(self, camino):
        tablero = camino[-1]
        cont = 0
        for i in range(0, len(tablero)):
            for j in range(0, len(tablero[i])):
                if tablero[i][j] != self.estadoMeta[i][j]:
                    cont = cont + 1
        return cont
