#!/usr/bin/python3


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
        return self.__remove(x, self.raiz)

    def minimo(self, nodo):
        if nodo.izquierdo is None:
            return nodo
        else:
            return self.minimo(nodo.izquierdo)

    def __remove(self, x, raiz):
        if raiz is None:
            return raiz
        if x < raiz.valor:
            raiz.izquierdo = self.__remove(x, raiz.izquierdo)
            return raiz
        elif x > raiz.valor:
            raiz.derecho = self.__remove(x, raiz.derecho)
            return raiz
        elif raiz.izquierdo is not None and raiz.derecho is not None:
            raiz.valor = self.minimo(raiz.derecho).valor  # Implementar mínimo
            raiz.derecho = self.__remove(raiz.valor, raiz.derecho)
            return raiz
        else:
            if raiz.izquierdo is not None:
                raiz = raiz.izquierdo
                return raiz
            else:
                raiz = raiz.derecho
                return raiz
        return raiz


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

# Ordenamiento

lista = [6, 3, 2, 1, 10, 19, 22, 5, 4, 8, 7, 18, 20]
a = ArbolBinario()

for i, e in enumerate(lista):
    print('Iteración ' + str(i) + '\n\n')
    a.insert(e)
    print_arbol(a)
    print('\n\n')


def print_ordenamiento(arbol):
    def imprime(raiz):
        if raiz is not None:
            imprime(raiz.izquierdo)
            print(raiz.valor)
            imprime(raiz.derecho)
    imprime(arbol.raiz)

print_ordenamiento(a)


def ordenamiento(arbol):
    lista = []

    def orden(raiz, lista=[]):
        if raiz is not None:
            orden(raiz.izquierdo, lista)
            lista.append(raiz.valor)
            orden(raiz.derecho, lista)
    orden(arbol.raiz, lista)
    return lista

l = ordenamiento(a)
