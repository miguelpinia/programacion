#!/usr/bin/env python3

from random import randint

################################
# Zona de definición de clases #
################################

#######################
# Pokemon             #
# =================== #
# + nombre            #
# + energia           #
# =================== #
# * resta             #
# * info == __str__   #
# * vivo == __bool__  #
#######################


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

#####################
# Fuego (Pokemon)   #
# ================= #
#                   #
# ================= #
# * lanzallamas     #
# * bola_de_fuego   #
#####################


class Fuego(Pokemon):
    """Define un pokemon de tipo Fuego."""

    def __init__(self, nombre):
        super(Fuego, self).__init__(nombre)

    def lanzallamas(self):
        return randint(0, 10)

    def bola_de_fuego(self):
        return randint(0, 10)

    def ataques(self):
        return "- lanzallamas\n-bola-de-fuego"


class Electrico(Pokemon):

    def __init__(self, nombre):
        super(Electrico, self).__init__(nombre)

    def rayo_electrico(self):
        return randint(0, 10)

    def tacleada(self):
        return randint(0, 10)


class Chispa(Fuego, Electrico):

    def __init__(self, nombre):
        super(Chispa, self).__init__(nombre)

    def chispazo(self):
        return randint(0, 15)

####################
# Jugador          #
# ================ #
# pokemon1         #
# pokemon2         #
# ================ #
####################


class Jugador(object):

    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2


class JugadorNP(Jugador):

    def __init__(self, pokemon1, pokemon2):
        super(JugadorNP, self).__init__(pokemon1, pokemon2)

    def ataque(self):
        pass


class Menu(object):

    def __init__(self):
        self.lista_pokemon = []

    def bienvenida(self):
        print('Pokemon Python 3\n')
        print('Este es un juego de consola experimental\n')
        print('Por favor se paciente con su uso\n')

    def menu_inicial(self):
        pass


def genera_pokemon():
    l_nombres = [
        'bulbasaur',
        'charizard',
        'charmander',
        'squirtle',
        'pikachu',
        'raichu']
    l_pokemons = [Fuego, Electrico, Chispa]
    i_nombre = randint(0, len(l_nombres) - 1)
    i_pokemon = randint(0, len(l_pokemons) - 1)
    p = l_pokemons[i_pokemon]
    return p(l_nombres[i_nombre])


def genera_pokemon_fuego():
    nombres = ['charmander', 'charmeleon', 'charizard']
    i_nombre = randint(0, len(nombres) - 1)
    return Fuego(nombres[i_nombre])

for i in range(10):
    p = genera_pokemon_fuego()
    print(p, type(p))

for i in range(10):
    p = genera_pokemon()
    print(p, type(p))


########################################################
# Zona de pruebas de código. Esta sección desaparecerá #
# cuando se implemente el main.                        #
########################################################


def esta_vivo(pokemon):
    """Regresa verdadero (True) si el pokemon tiene 1 o más de
    energía. Falso en otro caso."""
    return bool(pokemon)

bulbasaur = Pokemon('bulbasaur')
print(bulbasaur)

charizard = Fuego('Charizard')
print(charizard)

print(esta_vivo(bulbasaur))
print(esta_vivo(charizard))

raichu = Chispa('raichu')
