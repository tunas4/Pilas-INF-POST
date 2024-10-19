class pila:
    def __init__(self):
        self.max = 10
        self.pila = [] * self.max
        self.top = -1

    def push(self, value):
        if self.top < self.max - 1:
            self.top += 1
            self.pila[self.top] = value
        else:
            print("Stack Overflow")

    def pop(self):
        if self.top > -1:
            value = self.pila[self.top]
            self.top -= 1
            return value
        else:
            print("Stack Underflow")