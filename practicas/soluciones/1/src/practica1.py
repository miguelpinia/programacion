#!/usr/bin/env python3


class Pila(object):

    def __init__(self):
        self.lista = []

    def push(self, value):
        self.lista.append(value)

    def pop(self):
        return self.lista.pop()

    def peek(self):
        return self.lista[-1]

    def __bool__(self):
        return bool(self.lista)

    def __len__(self):
        return len(self.lista)

    def __str__(self):
        return str(self.lista)


class Analizador(object):

    def __init__(self):
        self.p = None

    def analiza_cadena(self, cadena):
        self.p = Pila()
        for par in cadena:
            if par == '(':
                self.p.push(par)
            elif par == ')':
                if not self.p:
                    return "Cadena no valida: {}".format(cadena)
                self.p.pop()
        if self.p:
            return "Los paréntesis no se encuentra bien formados: {}".format(
                cadena)
        else:
            return "La cadena está bien formada"


class Menu(object):

    def __init__(self):
        self.analizador = Analizador()

    def menu(self):
        while True:
            print("Analizador de paréntesis bien formados\n\n")
            cadena = input("Dame la cadena a validar: ")
            print(self.analizador.analiza_cadena(cadena))
            salida = input('Salir? s/n: ')
            if salida == 's':
                break

if __name__ == '__main__':
    menu = Menu()
    menu.menu()
