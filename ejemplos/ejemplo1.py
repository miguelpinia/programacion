import sys

# Tener una función que lea desde el archivo
# Crear el diccionario desde el archivo
# Crear la clase traductora
# Método que limpie la cadena de entrada
# Implementar dentro la clase un método traductor
# Crear un main, que invoque al método que hace la traducción

# s = 'AATCGTCTA'
s = 'CCATATTDDA'
# ex = '([ACGT]{3})+'

if len(s) % 3 != 0:

    print('La cadena no tiene el tamaño esperado')
    sys.exit(0)

l = []
for i in range(int(len(s) / 3)):
    l.append(s[i * 3:(i * 3 + 3)])

d = {'AAT': 'Asparigine',
     'CGT': 'Arginina',
     'CTA': 'Leucine'}

for a in l:
    print(a)
    if a in d:
        print(d[a])
    else:
        print('no está el aminoacido')
