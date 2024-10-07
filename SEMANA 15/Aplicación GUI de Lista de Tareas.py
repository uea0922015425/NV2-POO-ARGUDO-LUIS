import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")

# Crear los elementos de la interfaz
entrada_tarea = tk.Entry(ventana)
boton_agregar = tk.Button(ventana, text="Agregar")
lista_tareas = tk.Listbox(ventana)

# Función para agregar una tarea
def agregar_tarea():
    nueva_tarea = entrada_tarea.get()
    lista_tareas.insert(tk.END, nueva_tarea)
    entrada_tarea.delete(0, tk.END)

# Función para eliminar una tarea
def eliminar_tarea():
    indice_seleccionado = lista_tareas.curselection()
    if indice_seleccionado:
        lista_tareas.delete(indice_seleccionado)

# Asociar funciones a los botones
boton_agregar.config(command=agregar_tarea)
# ... (configurar el botón de eliminar de forma similar)

# Empaquetar los elementos en la ventana
entrada_tarea.pack()
boton_agregar.pack()
lista_tareas.pack()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()