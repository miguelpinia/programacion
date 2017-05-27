#!/usr/bin/python3

##########################################################
# Código de ejemplo para la implementación del árbol AVL #
# Sin comentarios, el total de lineas de código son 125  #
# lineas incluyendo funciones de prueba                  #
#                                                        #
# Autor: Miguel Angel Piña Avelino                       #
# RUN: $ python3 arbolAVL.py                             #
##########################################################


class Nodo(object):

    def __init__(self, valor, izquierdo=None, derecho=None):
        self.izquierdo = izquierdo
        self.derecho = derecho
        self.valor = valor
        self.altura = 0


def altura(t):
    return -1 if t is None else t.altura


def rotateWithLeftChild(k2):
    k1 = k2.izquierdo
    k2.izquierdo = k1.derecho
    k1.derecho = k2
    k2.altura = max(altura(k2.izquierdo), altura(k2.derecho)) + 1
    k1.altura = max(altura(k1.izquierdo), k2.altura) + 1
    return k1


def rotateWithRightChild(k1):
    k2 = k1.derecho
    k1.derecho = k2.izquierdo
    k2.izquierdo = k1
    k1.altura = max(altura(k1.izquierdo), altura(k1.derecho)) + 1
    k2.altura = max(altura(k2.derecho), k1.altura) + 1
    return k2


def doubleWithLeftChild(k3):
    k3.izquierdo = rotateWithRightChild(k3.izquierdo)
    return rotateWithLeftChild(k3)


def doubleWithRightChild(k1):
    k1.derecho = rotateWithLeftChild(k1.derecho)
    return rotateWithRightChild(k1)


def balance(t):
    if t is None:
        return t
    if altura(t.izquierdo) - altura(t.derecho) > 1:
        if altura(t.izquierdo.izquierdo) >= altura(t.izquierdo.derecho):
            t = rotateWithLeftChild(t)
        else:
            t = doubleWithLeftChild(t)
    else:
        if altura(t.derecho) - altura(t.izquierdo) > 1:
            if altura(t.derecho.derecho) >= altura(t.derecho.izquierdo):
                t = rotateWithRightChild(t)
            else:
                t = doubleWithRightChild(t)
    t.altura = max(altura(t.izquierdo), altura(t.derecho)) + 1
    return t


class ArbolAVL(object):

    def __init__(self, raiz=None):
        self.raiz = raiz

    def is_empty(self):
        return self.raiz is None

    def busqueda(self, x):
        return self.__busqueda(x, self.raiz)

    def __busqueda(self, x, raiz):
        if raiz is None:
            return False
        if raiz.valor == x:
            return True
        elif x < raiz.valor:
            return self.__busqueda(x, raiz.izquierdo)
        elif x > raiz.valor:
            return self.__busqueda(x, raiz.derecho)

    def insert(self, x):
        self.raiz = self.__insert(x, self.raiz)

    def __insert(self, x, t):
        if t is None:
            return Nodo(x)
        if x < t.valor:
            t.izquierdo = self.__insert(x, t.izquierdo)
        elif x > t.valor:
            t.derecho = self.__insert(x, t.derecho)
        elif x == t.valor:
            pass  # No hacemos nada
        return balance(t)

    def minimo(self, nodo):
        if nodo.izquierdo is None:
            return nodo
        else:
            return self.minimo(nodo.izquierdo)

    def remove(self, x):
        self.raiz = self.__remove(x, self.raiz)

    def __remove(self, x, t):
        if t is None:
            return t
        if x < t.valor:
            t.izquierdo = self.__remove(x, t.izquierdo)
        elif x > t.valor:
            t.derecho = self.__remove(x, t.derecho)
        elif t.izquierdo is not None and t.derecho is not None:
            t.valor = self.minimo(t.derecho).valor
            t.derecho = self.__remove(t.valor, t.derecho)
        else:
            t = t.izquierdo if t.izquierdo is not None else t.derecho
        return balance(t)


def print_arbol(arbol):
    def imprime(raiz, profundidad):
        if raiz is not None:
            imprime(raiz.derecho, profundidad + 1)
            print(('\t' * profundidad) + str(raiz.valor))
            imprime(raiz.izquierdo, profundidad + 1)
    imprime(arbol.raiz, 0)

arbol = ArbolAVL()
for i in range(100):
    arbol.insert(i)
print_arbol(arbol)
