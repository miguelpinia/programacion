#!/usr/bin/python3

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)


# def fact(n):
#     f = lambda n, acc: f(n - 1, n * acc) if n > 1 else acc
#     return f(n, 1)


class Nodo(object):

    def __init__(self, valor, izquierdo=None, derecho=None):
        self.izquierdo = izquierdo
        self.derecho = derecho
        self.valor = valor


class ArbolBinario(object):

    def __init__(self, raiz=None):
        self.raiz = raiz

    def is_empty(self):
        return self.raiz is None

    def contains(self, x):
        return self.__contains(x, self.raiz)

    def __contains(self, x, raiz):
        if raiz is None:
            return False
        if raiz.valor == x:
            return True
        elif x < raiz.valor:
            return self.__contains(x, raiz.izquierdo)
        elif x > raiz.valor:
            return self.__contains(x, raiz.derecho)

    def insert(self, x):
        self.raiz = self.__insert(x, self.raiz)

    def __insert(self, x, raiz):
        if raiz is None:
            return Nodo(x)
        elif x < raiz.valor:
            raiz.izquierdo = self.__insert(x, raiz.izquierdo)
            return raiz
        elif x > raiz.valor:
            raiz.derecho = self.__insert(x, raiz.derecho)
            return raiz


def print_arbol(arbol):
    def imprime(raiz, profundidad):
        if raiz is not None:
            imprime(raiz.derecho, profundidad + 1)
            print(('\t' * profundidad) + str(raiz.valor))
            imprime(raiz.izquierdo, profundidad + 1)
    imprime(arbol.raiz, 1)
