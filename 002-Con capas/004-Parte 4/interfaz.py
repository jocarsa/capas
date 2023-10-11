import tkinter as tk
import subprocess

raiz = tk.Tk()

def envia():
    script = "controlador.py"
    parametro = cadena.get()
    comando = ["python", script, parametro]

    # Use subprocess.Popen to capture the output of the command
    process = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Wait for the process to complete
    stdout, stderr = process.communicate()

    # Display the output in a new window
    output_window = tk.Toplevel(raiz)
    output_window.title("Command Output")
    output_text = tk.Text(output_window)
    output_text.insert("1.0", stdout.decode('utf-8'))
    output_text.pack()

cadena = tk.StringVar()
tk.Entry(raiz, textvariable=cadena).pack()
tk.Button(text="Guarda", command=envia).pack()

raiz.mainloop()
