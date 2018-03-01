#!/usr/bin/python3

import time

class Manecilla(object):

    def __init__(self, valor_maximo, valor_actual):
        self.valor_maximo = valor_maximo
        self.valor_actual = valor_actual

    def setValorActual(self, valor):
        self.valor_actual = valor

    def getValorActual(self):
        return self.valor_actual

    def getValorMaximo(self):
        return self.valor_maximo

class Reloj(object):

    def __init__(self, horas, minutos, segundos):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos

    def dameHora(self):
        return "{}:{}:{}".format(self.horas.getValorActual(),
                                 self.minutos.getValorActual(),
                                 self.segundos.getValorActual())

    def actualiza(self):
        seg_actual = self.segundos.getValorActual()
        seg_actual += 1
        if seg_actual == self.segundos.getValorMaximo():
            self.segundos.setValorActual(0)
            min_actual = self.minutos.getValorActual()
            min_actual += 1
            if min_actual == self.minutos.getValorMaximo():
                self.minutos.setValorActual(0)
                hora_actual = self.horas.getValorActual()
                hora_actual += 1
                if hora_actual == self.horas.getValorMaximo():
                    self.horas.setValorActual(0)
                else:
                    self.horas.setValorActual(hora_actual)
            else:
                self.minutos.setValorActual(min_actual)
        else:
            self.segundos.setValorActual(seg_actual)



def main():
    segundos = Manecilla(60, 12)
    minutos = Manecilla(60, 20)
    horas = Manecilla(24, 10)
    reloj = Reloj(horas, minutos, segundos)
    print(reloj.dameHora())
    while True:
        reloj.actualiza()
        print(reloj.dameHora())
        time.sleep(1)

if __name__ == '__main__':
    main()
