def infija(expresion):
    operandos = []
    operadores = []
    expresion = expresion.split()
    for x in expresion:
        if x == '*' or x == '/' or x == '-' or x == '+':
            operadores.append(x)
        else:
            operandos.append(x)
    operadores.reverse()
    r = float(operandos[0])
    for i in range(len(operadores)):
        r = operacion(r, float(operandos[i + 1]), operadores[i])
    return r

def operacion(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        return a / b
