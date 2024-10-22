from myclass.pila import Pila 

def precedencia(op):

    if op == '+' or op == '-':
        return 1

    if op == '*' or op == '/':
        return 2

    if op == '^':
        return 3
    return 0

def infijatoPostfija(EI):


    N = len(EI)
    pila = Pila()
    EP = [] 
    pila.push('$') 

   
    for i in range(N):
        c = EI[i]

        if c =='(':
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
    return ''.join(EP)

expresion_infija = "a+b"
expresion_postfija = infijatoPostfija(expresion_infija)

print(expresion_postfija)



