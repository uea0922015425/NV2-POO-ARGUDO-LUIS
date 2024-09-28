import tkinter as tk
from tkinter import ttk

def agregar_evento():
    # Lógica para agregar un nuevo evento
    # ...

ventana = tk.Tk()
ventana.title("Mi Agenda")

# ... Crear los elementos de la interfaz ...

boton_agregar = tk.Button(ventana, text="Agregar Evento", command=agregar_evento)
boton_agregar.pack()

ventana.mainloop()