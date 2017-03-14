#!/usr/bin/env python3


class Polinomio(object):
    """Clase para modelar un polinomio usando diccionarios. Implementa
    un constructor que recibe un diccionario, donde cada llave es el
    exponente del polinomio y su valor asociado es el coeficiente.

    También implementa el método __add__ para realizar sumas y __str__
    para la representación de la cadena."""

    def __init__(self, dictionary):
        """Inicializa un el polinomio con dict. Se espera que el
        diccionario describa para cada llave un exponente del
        polinomio y su valor asociado el coeficiente."""
        self.val = dictionary

    def __add__(self, other):
        """Permite realizar la suma de dos polinomios. p1 + p2"""
        if not isinstance(other, Polinomio):
            raise TypeError('No es un polinomio')
        else:
            data = list(self.val.items()) + list(other.val.items())
            d = {}
            for k, v in data:
                d[k] = d.get(k, 0) + v
            return Polinomio(d)

    def __str__(self):
        """Imprime de forma bonita un polinomio. Por ejemplo, dado:
        Polinomio({1: 1, 2: 1, 10: 12, 21: 23}), este se imprime como:
        1x^1 + 1x^2 + 12x^10 + 23x^21"""
        return ' + '.join('{}x^{}'.format(self.val[key], key)
                          for key in sorted(self.val))


p = Polinomio({1: 1, 2: 1, 10: 12, 21: 23})
p1 = Polinomio({3: 9, 10: 11, 21: 33, 34: 12})
print(p + p1)
