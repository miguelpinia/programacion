#!/usr/bin/env python3

from random import randint
from datos import Fuego, Chispa, Electrico


def esta_vivo(pokemon):
    """Regresa verdadero (True) si el pokemon tiene 1 o más de
    energía. Falso en otro caso."""
    return bool(pokemon)


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

# Probando los imports

p = genera_pokemon()
print(esta_vivo(p))
print(p)
print(type(p))
print(dir(p))
