#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from copy import deepcopy

# definição das cores dos vértices
# cores são usadas nas pesquisas
WHITE = 0
GREY = 1
BLACK = 2


class grafo():

    def __init__(self):
        self.V = []
        self.E = dict()
        self.dist = dict()
        self.cor = dict()
        self.tf = dict()  # usado no DFS

    @property
    def num_vertices(self):
        """
            :return número total de vertices no grafo |V|
        """
        return len(self.V)

    @property
    def num_arestas(self):
        """
            :return número total de aresta no grafo |E|
        """
        return sum(len(self.E[v]) for v in self.V)

    def acresc_vertice(self, v):
        """ acrescenta um vertice v ao grafo
            normalmente esta funcao nao é necessária pois acresc_aresta adiciona um vertice não existente
        """
        if v not in self.V:
            self.V.append(v)
            self.cor[v] = WHITE
            self.dist[v] = float('inf')

    def _add(self, u, v):
        if u not in self.E:
            self.E[u] = []
        self.E[u].append(v)

    def acresc_aresta(self, u, v, direcionada=False):
        """
            :param direcionada: por default cria um grafo nao direcionado
        """
        self.acresc_vertice(u)
        self.acresc_vertice(v)
        self._add(u, v)
        if not direcionada:
            self._add(v, u)

    def __str__(self, s=None):
        _str = ''
        V1 = deepcopy(self.V)  # V1 keeps track of the visited vertices
        while len(V1) > 0:
            if s is None:
                s = V1[0]
            V = [s]
            while len(V) > 0:
                v = V.pop(0)
                V1.remove(v)
                _str += "{}: {}\n".format(v, [u for u in self.E[v]])
                V.extend([u for u in self.E[v] if u in V1 and u not in V])
            s = None
        return _str


if __name__ == '__main__':
    G = grafo()
    G.acresc_aresta('a', 'b')
    G.acresc_aresta('a', 's')
    G.acresc_aresta('s', 'b')
    G.acresc_aresta('s', 'c')
    G.acresc_aresta('s', 'e')
    G.acresc_aresta('f', 'e')
    G.acresc_aresta('f', 'c')
    G.acresc_aresta('f', 'd')
    G.acresc_aresta('e', 'g')
    G.acresc_aresta('e', 'd')
    G.acresc_aresta('d', 'g')
    G.acresc_aresta('d', 'c')

    print("numero de vértices", G.num_vertices)
    print("numero de arestas", G.num_arestas)
    print(G)
