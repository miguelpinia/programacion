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

    def __busqueda(self, x, raiz):
        if raiz is None:
            return None
        if raiz.valor == x:
            return raiz
        elif x < raiz.valor:
            return self.__busqueda(x, raiz.izquierdo)
        elif x > raiz.valor:
            return self.__busqueda(x, raiz.derecho)

    def busqueda(self, x):
        return self.__busqueda(x, self.raiz)

    def remove(self, x):
        nodo = self.busqueda(x)
        izquierdo = nodo.izquierdo
        derecho = nodo.derecho

    def __remove(self, x, raiz):
        if raiz is not None:
            if raiz.valor == x:
                pass
            elif x < raiz.valor:
                if raiz.izquierdo.valor == x:
                    aEliminar = raiz.izquierdo
                    aEliminarIzquierdo = aEliminar.izquierdo
                    aEliminarDerecho = aEliminar.derecho
                    raiz.izquierdo = aEliminarDerecho
                    minimo = aEliminarDerecho.izquierdo
                    while minimo.izquierdo is not None:
                        minimo = minimo.izquierdo
                    minimo.izquierdo = aEliminarIzquierdo
                else:
                    return self.__remove(x, raiz.izquierdo)
            elif raiz.valor > x:
                pass


def print_arbol(arbol):
    def imprime(raiz, profundidad):
        if raiz is not None:
            imprime(raiz.derecho, profundidad + 1)
            print(('\t' * profundidad) + str(raiz.valor))
            imprime(raiz.izquierdo, profundidad + 1)
    imprime(arbol.raiz, 1)

arbol = ArbolBinario()
arbol.insert(9)
arbol.insert(4)
arbol.insert(2)
arbol.insert(5)
arbol.insert(1)
arbol.insert(3)
arbol.insert(6)
arbol.insert(11)
arbol.insert(10)
arbol.insert(12)
print_arbol(arbol)
