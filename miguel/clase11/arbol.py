#!/usr/bin/python3


class Nodo(object):

    def __init__(self, valor, nodoIzq=None, nodoDer=None):
        self.valor = valor
        self.nodoIzq = nodoIzq
        self.nodoDer = nodoDer

    def __str__(self):
        return 'Nodo({})'.format(self.valor)


class ArbolBinario(object):

    def __init__(self, raiz=None):
        self.raiz = raiz

    def _insert(self, valor, nodo):
        if nodo is None:
            return Nodo(valor)
        if valor < nodo.valor:
            if nodo.nodoIzq is None:
                nodo.nodoIzq = Nodo(valor)
                return nodo
            else:
                nodo.nodoIzq = self._insert(valor, nodo.nodoIzq)
                return nodo
        else:
            if nodo.nodoDer is None:
                nodo.nodoDer = Nodo(valor)
                return nodo
            else:
                nodo.nodoDer = self._insert(valor, nodo.nodoDer)
                return nodo

    def insert(self, valor):
        self.raiz = self._insert(valor, self.raiz)

    def inorden(self, nodo, profundidad):
        if nodo is not None:
            self.inorden(nodo.nodoDer, profundidad + 1)
            print('{}{}'.format(profundidad * '\t', nodo.valor))
            self.inorden(nodo.nodoIzq, profundidad + 1)


a = ArbolBinario()
a.insert(1)
a.insert(2)
a.insert(5)
a.insert(3)
a.insert(7)
a.insert(-2)
a.insert(-1)
a.insert(-3)
a.insert(0)
print('\n')
a.inorden(a.raiz, 0)
