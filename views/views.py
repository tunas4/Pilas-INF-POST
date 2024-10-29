import tkinter as tk
import convertidor as c
import re

def introducir_expresion():
    root = tk.Tk()
    root.geometry("300x200")
    label = tk.Label(root, text="Introduzca la expresión")
    label.pack(pady=10)
    
    def limite_caracteres(texto):
        patron = r'^[a-zA-Z0-9*^+\-/()]*$'
        if len(texto) > 50 or not re.match(patron, texto):
            return False
        if re.search(r'[\+\-\*/\^]{2,}', texto):
            return False
        
        balance = 0
        for char in texto:
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1
            if balance < 0:
                return False
        
        return True

    def validar_expresion(event):
        texto = entry.get() + event.char
        if not limite_caracteres(texto):
            return "break"

    entry = tk.Entry(root, validate="key")
    entry.bind("<Key>", validar_expresion)
    entry.pack(pady=10)
    
    def calcular():
        try:
            resultado = c.infijatoPostfija(entry.get())
            resultado_label.config(text="La expresión en notación postfija es: " + resultado)
        except Exception as e:
            resultado_label.config(text=f"Error: {e}")
    
    button = tk.Button(root, text="Calcular", command=calcular)
    button.pack(pady=10)
    
    resultado_label = tk.Label(root, text="")
    resultado_label.pack(pady=10)
    
    root.mainloop()


def mostrar():
    root = tk.Tk()
    root.geometry("400x200")

    label = tk.Label(root, text="Expresion infofija: " + c.expresion_infija)
    label.pack(pady=10)

    label = tk.Label(root, text="Expresion postfija: " + c.expresion_postfija)
    label.pack(pady=10)

    root.mainloop()

def creditos():
    root = tk.Tk()
    root.geometry("400x200")

    label = tk.Label(root, text="Creditos")
    labelMateria = tk.Label(root, text="Estructura de datos Aplicadas")
    labelJonathan = tk.Label(root, text="Jonathan Ivan Castro Saenz | 23170035")
    labelNoe = tk.Label(root, text="Noé Abel Vargas López | 23170106")
    label.pack(pady=10)
    labelMateria.pack(pady=10)
    labelJonathan.pack(pady=10)
    labelNoe.pack(pady=10)

    root.mainloop()