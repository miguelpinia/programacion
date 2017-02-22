#!/usr/bin/env python3

"""Construyendo estructuras de datos a partir de listas"""


class Pila(object):
    """Clase que representa una pila.

    Una pila es una estructura de tipo LIFO: Last In, First Out. Sólo
    tiene dos operaciones básicas: pop y push."""

    def __init__(self):
        self.lista = []

    def pop(self):
        """Extrae un elemento de la pila."""
        if self.lista:
            return self.lista.pop()
        return None

    def push(self, x):
        """Inserta un elemento a la pila."""
        self.lista.append(x)


class Cola(object):
    """Clase que representa una cola.

    Una cola es una estructura de tipo FIFO: First In, First Out. Sólo
    tiene dos operaciones básicas: Insert y Pop."""

    def __init__(self):
        self.lista = []

    def insert(self, x):
        """Inserta un elemento a la cola."""
        self.lista.append(x)

    def pop(self):
        """Extrae un elemento de la cola."""
        if self.lista:
            longitud = len(self.lista)
            return self.lista.pop(longitud - 1)
        return None
