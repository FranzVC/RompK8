from AgenteIA.AgenteBuscador import AgenteBuscador
from copy import deepcopy


class AgenteRK8(AgenteBuscador):

    def __init__(self):
        AgenteBuscador.__init__(self)
        self.funcionSucesor = [self.izquierda, self.derecha, self.subir, self.bajar]

    @staticmethod
    def get_vacio(tablero):
        for x in range(len(tablero)):
            for y in range(len(tablero)):
                if tablero[x][y] == 0:
                    return x, y

    def izquierda(self, tablero):
        pos_x, pos_y = self.get_vacio(tablero)
        if pos_y >= 1:
            tablero[pos_x][pos_y] = tablero[pos_x][pos_y - 1]
            tablero[pos_x][pos_y - 1] = 0
            return tablero
        else:
            return [[-1, 0, 0], [0, 0, 0], [0, 0, 0]]

    def derecha(self, tablero):
        pos_x, pos_y = self.get_vacio(tablero)
        if pos_y <= 1:
            tablero[pos_x][pos_y] = tablero[pos_x][pos_y + 1]
            tablero[pos_x][pos_y + 1] = 0
            return tablero
        else:
            return [[-1, 0, 0], [0, 0, 0], [0, 0, 0]]

    def subir(self, tablero):
        pos_x, pos_y = self.get_vacio(tablero)
        if pos_x >= 1:
            tablero[pos_x][pos_y] = tablero[pos_x - 1][pos_y]
            tablero[pos_x - 1][pos_y] = 0
            return tablero
        else:
            return [[-1, 0, 0], [0, 0, 0], [0, 0, 0]]

    def bajar(self, tablero):
        pos_x, pos_y = self.get_vacio(tablero)
        if pos_x <= 1:
            tablero[pos_x][pos_y] = tablero[pos_x + 1][pos_y]
            tablero[pos_x + 1][pos_y] = 0
            return tablero
        else:
            return [[-1, 0, 0], [0, 0, 0], [0, 0, 0]]

    def test_objetivo(self, tablero):
        if tablero == self.estadoMeta:
            return True
        return False

    @staticmethod
    def es_valido(tablero):
        for i in range(0, len(tablero)):
            for j in range(0, len(tablero[i])):
                if tablero[i][j] == -1:
                    return False
        return True

    def genera_hijos(self, nodo):
        resul = []

        for f in self.funcionSucesor:
            aux = deepcopy(nodo)
            n = f(aux)
            if self.es_valido(n):
                resul.append(n)
        return resul

    def get_costo(self, camino):
        return len(camino)

    # h1: numero de fichas fuera de lugar
    def get_heuristica(self, camino):
        pass

    # h2: Sumatoria de las distancias manhatan de cada ficha, desde donde sen encuntra
    #     hasta donde debería estar
    # h3: Formular heuristica que supere el rendimiento de las anteriores,
    #

    def get_funcion_a(self, camino):
        return self.get_costo(camino) + self.get_heuristica(camino)
