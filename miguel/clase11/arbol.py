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

    def is_empty(self):
        return self.raiz is None

    def _contains(self, x, raiz):
        if raiz is None:
            return False
        if x == raiz.valor:
            return True
        elif x < raiz.valor:
            return self._contains(x, raiz.nodoIzq)
        else:
            return self._contains(x, raiz.nodoDer)
        return False

    def contains(self, x):
        return self._contains(x, self.raiz)

    def _remove(self, x, raiz):
        if raiz is None:
            return None
        if x > raiz.valor:
            raiz.nodoDer = self._remove(x, raiz.nodoDer)
        elif x < raiz.valor:
            raiz.nodoIzq = self._remove(x, raiz.nodoIzq)
        else:
            if raiz.nodoIzq is None:
                return raiz.nodoDer
            elif raiz.nodoDer is None:
                return raiz.nodoIzq
            chiquitoDer = self._findMin(raiz.nodoDer)

    def _findMin(self, raiz):
        if raiz.nodoIzq is None:
            return raiz
        else:
            return self._findMin(raiz.nodoIzq)

    def remove(self, x):
        if self.contains(x):


a = ArbolBinario()
print('El arbol es vacio?: {}'.format(a.is_empty()))
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
print('El arbol es vacio?: {}'.format(a.is_empty()))
print('El valor -3 está en el arbol: {}'.format(a.contains(-3)))
print('El valor 10 está en el arbol: {}'.format(a.contains(10)))
