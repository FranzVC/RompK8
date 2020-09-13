from AgenteRK8 import AgenteRK8


class AgenteH2(AgenteRK8):

    def find_num(self,camino,num):
        for i in range(3):
            for j in range(3):
                if camino[i][j] == num:
                    return ((i,j))

    def cant(self, camino, actual, esperado):
        print(camino[actual[0]][actual[1]])
        print(self.estadoMeta[esperado[0]][esperado[1]])
        if camino[actual[0]][actual[1]] != self.estadoMeta[esperado[0]][esperado[1]]:
            print("*******************")
            if sum(actual) > sum(esperado):
                return actual- esperado
            else:
                return esperado - actual
        else:
            return 0

    # Heuristica: distancia manhatan
    def get_heuristica(self, camino):
        can = 0
        tablero = camino[-1]
        for x in range(3):
            for y in range(3):
                #print(self.find_num(tablero,3))
                #can += self.cant(tablero, self.find_num(tablero,tablero[x][y]), self.find_num(self.estadoMeta,tablero[x][y]) )
                print(self.cant(tablero, self.find_num(tablero,tablero[x][y]), self.find_num(self.estadoMeta,tablero[x][y])))
        return can