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

        if c == '(':
            pila.push(c)
        elif c == ')':
            t = pila.pop()
            while t != '(':
                EP.append(t)
                t = pila.pop()
        elif c in '+-*/^': 
            while pila.peek() != '$' and precedencia(pila.peek()) >= precedencia(c):
                EP.append(pila.pop())
            pila.push(c)
        else:
            EP.append(c)

    # Vaciamos la pila
    while pila.peek() != '$':
        EP.append(pila.pop())
    
    expresion_postfija = ''.join(EP)
    return expresion_postfija
