from myclass.pila import Pila

# Variables globales para almacenar la expresión infija y postfija
expresion_infija = ""
expresion_postfija = ""

def precedencia(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

def infijatoPostfija(EI):
    global expresion_infija, expresion_postfija
    expresion_infija = EI
    N = len(EI)
    pila = Pila()
    EP = []

    pila.push('$')
    for i in range(N):
        c = EI[i]
        # Si el caracter es un paréntesis de apertura
        if c == '(':
            pila.push(c)
        # Si el caracter es un paréntesis de cierre
        elif c == ')':
            t = pila.pop()
            while t != '(':
                EP.append(t)
                t = pila.pop()
        # Si es un operador
        elif c in '+-*/^':
            while pila.peek() != '$' and precedencia(pila.peek()) >= precedencia(c):
                EP.append(pila.pop())
            pila.push(c)
        # Si es un operando, lo añadimos a la lista EP
        else:
            EP.append(c)

    # Vaciamos la pila para añadir los elementos restantes
    while pila.peek() != '$':
        EP.append(pila.pop())

    # Convertimos la lista EP en una cadena
    expresion_postfija = ''.join(EP)
    # Prueba con la expresión dada
    return expresion_postfija


