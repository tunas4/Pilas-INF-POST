import tkinter as tk
import convertidor as c

def introducir_expresion():
    root = tk.Tk()
    root.geometry("300x200")

    label = tk.Label(root, text="Introduzca la expresión")
    label.pack(pady=10)

    def limite_caracteres(texto):
        return len(texto) <= 50

    validar = root.register(limite_caracteres)
    entry = tk.Entry(root, validate="key", validatecommand=(validar, "%P"))
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