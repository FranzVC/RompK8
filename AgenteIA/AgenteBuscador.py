#################################################################
# Nombre      : Agente Buscador                                 #
# Version     : 0.05.03.2017                                    #
# Autor       : Victor                                          #
# Descripcion : Clase especificacion de Agente, implementa      #
#               algoritmos de busqueda                           #
##################################################################

from time import time
from AgenteIA.Agente import Agente
from copy import deepcopy
import sys



class AgenteBuscador(Agente):

    def __init__(self):
        Agente.__init__(self)
        self.funcionSucesor = []
        self.tecnica = None
        self.estadoInicial = None
        self.estadoMeta = None
        self.acciones = None

    def set_tecnica(self, t):
        self.tecnica = t

    def set_estado_inicial(self, e0):
        self.estadoInicial = e0

    def set_estado_meta(self, ef):
        self.estadoMeta = ef

    def add_funcion_sucesor(self, fun):
        self.funcionSucesor.append(fun)

    def test_objetivo(self, nodo):
        return nodo == self.estadoMeta

    def genera_hijos(self, nodo):
        raise Exception('Se debe implementar generación de hijos')

    def get_costo(self, camino):
        raise Exception('Se debe implementar funcion costo')

    def get_heuristica(self, camino):
        raise Exception('Se debe implementar heuristica')

    def get_funcion_a(self, camino):
        raise Exception('Se debe implementar funcion a estrella')

    def programa(self):
        frontera = [[self.estadoInicial]]
        visitados = []
        cont = 0
        tam = 0
        tiempo = time()
        while frontera:
            tam = max(sys.getsizeof(frontera), tam)
            cont += 1

            if self.tecnica == "profundidad":
                camino = frontera.pop()
            else:
                camino = frontera.pop(0)
            nodo = camino[-1]
            if self.test_objetivo(nodo):
                fin = time() -  tiempo
                print("Tardo: %0.10f segundos." % fin)
                print("Maximo tamaño de frontera: ", tam, " bytes")
                print("Se preciso de ", cont, " iteraciones para encontrar la solucion")
                print("la solución tiene ", len(camino)-1, " pasos")
                self.acciones = camino
                break
            else:
                visitados.append(nodo)
                for hijo in self.genera_hijos(nodo):
                    if hijo != 0 and not (hijo in visitados):
                        aux = deepcopy(camino)
                        aux.append(hijo)
                        frontera.append(aux)
                if self.tecnica == "costouniforme":
                    frontera.sort(key=lambda tup: self.get_costo(tup))
                elif self.tecnica == "codicioso":
                    frontera.sort(key=lambda tup: self.get_heuristica(tup))
                elif self.tecnica == "A*":
                    frontera.sort(key=lambda tup: self.get_funcion_a(tup))
