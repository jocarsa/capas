import tkinter as tk
import subprocess

raiz = tk.Tk()

def envia():
    script = "controlador.py"
    parametros = [cadena.get()]
    comando = ["python", script] + parametros
    subprocess.call(comando)

cadena = tk.StringVar()
tk.Entry(raiz,textvariable = cadena).pack()
tk.Button(text="Guarda",command=envia).pack()

raiz.mainloop()
