class Polinomio(object):
    def __init__(self, diccionario):
        self.poli = diccionario

    def __add__(self, d):
        otro = d.poli
        suma = {}
        r = len(self.poli) + len(otro)
        
        for k in range(r):
            s = self.poli.get(k, 0) + otro.get(k, 0) #Si el polinomio no tiene terminos de grado k, regresa 0
            if s != 0:
                suma[k] = s
        return Polinomio(suma) #Construye un nuevo polinomio con la suma

    def __str__(self):
        return "".join(("{:+}x^{}" if e else "{}").format(c, e)
                       for e, c in sorted(self.poli.items()) if c)

x = Polinomio({0:1, 1:-1})
y = Polinomio({1:1, 4:-6, 5:-1, 3:2})
print(x)
print(y)
print(x+y)


