def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def fact(n):
    f = lambda n, acc: f(n - 1, n * acc) if n > 1 else acc
    return f(n, 1)


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
