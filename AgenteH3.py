from AgenteRK8 import AgenteRK8
from AgenteH2 import AgenteH2

class AgenteH3(AgenteRK8):

    def get_heuristica1(self,camino):
        tablero = camino[-1]
        cont = 0
        for i in range(0, len(tablero)):
            for j in range(0, len(tablero[i])):
                if tablero[i][j] != self.estadoMeta[i][j]:
                    cont = cont + 1
        return cont
    
    def get_heuristica2(self, camino):
        can = 0
        tablero = camino[-1]
        for x in range(3):
            for y in range(3):
                actual = (self.find_num(tablero,tablero[x][y]))
                esperado = (self.find_num(self.estadoMeta,tablero[x][y]))
                can += self.cant(tablero, actual, esperado)
        return can        

    def get_heuristica(self, camino):
        return self.get_heuristica1(camino) + self.get_heuristica2(camino)