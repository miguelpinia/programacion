#!/usr/bin/python
from random import randint, randrange

class Pokemon:
    """
    Clase Pokemon, aquí debería ir una descripción interesante.
    """

    def __init__(self, nombre):
        """
        Recibe como parámetro el nombre del pokemon. Establece a
        100 los puntos vida y no tiene ataques definidos.
        """
        self.nombre = nombre
        self.hp = 100
        self.ataques = {}

    def resta(self, puntos):
        """
        Restamos puntos a los puntos de vida, los puntos pueden
        estar entre 0 y 15. En caso de que no se cumpla esta
        condición, se lanza una condición de error. En caso de que el
        valor restado a los puntos de vida, deje el estado en un valor
        menor a cero, se establece como valor final cero de vida.
        """
        assert 0 <= puntos <= 15, \
            "Los puntos no pueden estar fuera del rango de 0 a 15"
        if self.hp - puntos < 0:
            self.hp = 0
        else:
            self.hp -= puntos

    def __bool__(self):
        """
        Si tiene puntos de vida mayor a cero, entonces el pokemon
        esta vivo (True)
        """
        return self.hp > 0

    def estaVivo(self):
        """Regresa verdadero si el pokemon está vivo."""
        return bool(self)


class Electrico(Pokemon):

    def __init__(self, nombre):
        super(Electrico, self).__init__(nombre)
        self.ataques = {'impactTrueno':self.impactTrueno
                        , 'rayo':self.rayo}

    def impactTrueno(self):
        return randint(0, 11)

    def rayo(self):
        return randint(0, 11)


class Agua(Pokemon):

    def __init__(self, nombre):
        super(Agua, self).__init__(nombre)
        self.ataques = {'chorro':self.chorro
                        , 'salpicar':self.salpicar}

    def chorro(self):
        return randint(0, 11)

    def salpicar(self):
        return randint(0, 11)

class AguaElectrico(Agua, Electrico):

    def __init__(self, nombre):
        super(AguaElectrico, self).__init__(nombre)
        self.ataques = {}
        for c in AguaElectrico.__bases__:
            self.ataques.update(c(self).ataques)
        self.ataques['aquaRayo'] = self.aquaRayo

    def aquaRayo(self):
        return randint(0, 16)


def imprimeAtaque(pokemon):
    l = []
    for i, k in enumerate(pokemon.ataques):
        print('{}), {}'.format(i + 1, k))
        l.append(k)
    index = int(input('Selecciona un ataque\n'))
    assert 0 < index < len(pokemon.ataques), 'Valor erróneo'
    return l[index - 1]


class Jugador(object):

    def __init__(self, nombre, pokemon1, pokemon2):
        self.nombre = nombre
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def hayPokemons(self):
        return self.pokemon1.estaVivo() or self.pokemon2.estaVivo()


class JugadorNPC(Jugador):
    def __init__(self, nombre, pokemon1, pokemon2):
        super(JugadorNPC, self).__init__(nombre, pokemon1, pokemon2)


def todaviaHayConQueJugar(jugador1, jugador2):
    return jugador1.hayPokemons() and jugador2.hayPokemons()

def batalla():
    p = Agua('Squirtle')
    p2 = Electrico('Pikachu')
    jugador = Jugador('Red', p, p2)
    p3 = Agua('Foo')
    p4 = Agua('Vaporeon')
    jugadorNPC = JugadorNPC('Bot', p3, p4)
    mi_turno = bool(randrange(2))
    while todaviaHayConQueJugar(jugador, jugadorNPC):
        if mi_turno:
            if jugador.pokemon1.estaVivo():
                print('Hola pokemon 1')
            else:
                print('ataco con el otro')
        else:
            print('Jugador no controlable')
        mi_turno = not mi_turno
