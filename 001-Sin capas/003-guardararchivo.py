import tkinter as tk

def guarda():
    print("ahora voy a guardar")
    print("el texto que he atrapado es:"+cadena.get())

raiz = tk.Tk()

cadena = tk.StringVar()

entrada = tk.Entry(raiz,textvariable = cadena)
entrada.pack()
boton = tk.Button(text="Guarda",command=guarda)
boton.pack()

raiz.mainloop()
