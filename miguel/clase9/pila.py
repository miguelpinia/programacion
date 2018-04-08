#!/usr/bin/python3

from operator import add, sub, mul, truediv

class Pila(object):

    def __init__(self):
        """
        Constructor de la pila. Utiliza una lista
        para construir la pila. Construye una nueva pila vacía. No
        necesita parámetros y regresa una pila vacía.
        """
        self.pila = []

    def push(self, x):
        """
        Agrega un nuevo elemento en el tope de la pila. Necesita el
        elemento y no regresa nada.
        """
        self.pila.append(x)

    def pop(self):
        """
        Elimina el elemento que esta en el tope de la pila. No
        necesita parámetros y devuelve el elemento que se eliminó.
        """
        return self.pila.pop()

    def peek(self):
        """
        Regresa el elemento que se encuentra en la parte superior
        de la pila pero no lo elimina. No necesita parámetros, no
        modifica la pila.
        """
        return self.pila[-1]

    def is_empty(self):
        """
        Verifica si la pila está vacía. No necesita parámetros y
        regresa un valor booleano.
        """
        return bool(self.pila)

    def size(self):
        """
        Regresa el número de elementos en la pila. No necesita parámetros y
        regresa un entero.
        """
        return len(self.pila)

def valida_expr_mal(expresion):
    ops = {'+':add, '-':sub,'*':mul,'/':truediv}
    p = Pila()
    a = None
    b = None
    for elem in expresion.split():
        if elem in ['*', '-', '+', '/']:
            p.push(elem)
        else:
            if not a:
                a = float(elem)
            else:
                b = float(elem)
                a = ops[p.pop()](a, b)
    return a
