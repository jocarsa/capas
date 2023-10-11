import tkinter as tk

def guarda():
    print("ahora voy a guardar")

raiz = tk.Tk()



entrada = tk.Entry(raiz)
entrada.pack()
boton = tk.Button(text="Guarda",command=guarda)
boton.pack()

raiz.mainloop()
