import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Tareas")

# Crear una lista para almacenar las tareas
tareas = []

# Función para agregar una tarea
def agregar_tarea():
    nueva_tarea = entrada_tarea.get()
    tareas.append(nueva_tarea)
    actualizar_lista()
    entrada_tarea.delete(0, tk.END)

# Función para marcar una tarea como completada
def marcar_como_completada(indice):
    # ... Implementar la lógica para marcar la tarea como completada
    actualizar_lista()

# Función para eliminar una tarea
def eliminar_tarea(indice):
    # ... Implementar la lógica para eliminar la tarea
    actualizar_lista()

# Función para actualizar la lista de tareas en la interfaz
def actualizar_lista():
    # ... Implementar la lógica para actualizar la lista visualmente

# Crear los elementos de la interfaz
entrada_tarea = tk.Entry(ventana)
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_tarea)
lista_tareas = tk.Listbox(ventana)

# ... Colocar los elementos en la ventana usando pack() o grid()

# Asignar atajos de teclado
ventana.bind("<Return>", lambda event: agregar_tarea())  # Enter para agregar
lista_tareas.bind("<Double-1>", lambda event: marcar_como_completada(lista_tareas.curselection()))  # Doble clic para marcar como completada
# ... Agregar más atajos para eliminar, etc.

ventana.mainloop()