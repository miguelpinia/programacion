#!/usr/bin/env python3

from random import randint


class Pokemon(object):
    """Define un pokemon."""

    def __init__(self, nombre, energia=100):
        self.nombre = nombre
        self.energia = energia

    def resta(self, valor):
        assert 0 <= valor <= 15, "el valor pasado no es menor o igual a 15"
        self.energia -= valor

    def __str__(self):
        return 'Nombre: {}, energia: {}'.format(self.nombre, self.energia)

    def __bool__(self):
        return self.energia > 0

    def __dir__(self):
        return []


class Fuego(Pokemon):
    """Define un pokemon de tipo Fuego."""

    def __init__(self, nombre):
        super(Fuego, self).__init__(nombre)

    def lanzallamas(self):
        return randint(0, 10)

    def bola_de_fuego(self):
        return randint(0, 10)

    def __dir__(self):
        l = super(Fuego, self).__dir__()
        l.extend(['lanzallamas', 'bola_de_fuego'])
        return l


class Electrico(Pokemon):

    def __init__(self, nombre):
        super(Electrico, self).__init__(nombre)

    def rayo_electrico(self):
        return randint(0, 10)

    def tacleada(self):
        return randint(0, 10)

    def __dir__(self):
        l = super(Electrico, self).__dir__()
        l.extend(['rayo_electrico', 'tacleada'])
        return l


class Chispa(Fuego, Electrico):

    def __init__(self, nombre):
        super(Chispa, self).__init__(nombre)

    def chispazo(self):
        return randint(0, 15)

    def __dir__(self):
        l = super(Chispa, self).__dir__()
        l.extend(['chispazo'])
        return l


class Jugador(object):

    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2


class JugadorNP(Jugador):

    def __init__(self, pokemon1, pokemon2):
        super(JugadorNP, self).__init__(pokemon1, pokemon2)

    def ataque(self):
        pass
