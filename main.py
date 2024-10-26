import tkinter as tk
from views import views as v

root = tk.Tk()
root.geometry("200x200")

button1 = tk.Button(root, text="Introducir expresion", command=v.introducir_expresion)
button1.pack(pady=10)

button2 = tk.Button(root, text="Mostrar", command=v.mostrar)
button2.pack(pady=10)

button3 = tk.Button(root, text="Creditos", command=v.creditos)
button3.pack(pady=10)

button4 = tk.Button(root, text="Salir", command=root.destroy)
button4.pack(pady=10)

root.mainloop()