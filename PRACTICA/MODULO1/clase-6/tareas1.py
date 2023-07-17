import tkinter as tk


def agregar_tarea():
    # Obtiene el texto ingresado en la entrada de texto
    tarea = entrada.get()
    if tarea:
        # Inserta la tarea en la lista de tareas
        lista_tareas.insert(tk.END, tarea)
        # Borra el contenido de la entrada de texto
        entrada.delete(0, tk.END)


def completar_tarea():
    # Obtiene el índice de la tarea seleccionada en la lista de tareas
    seleccion = lista_tareas.curselection()
    if seleccion:
        indice = seleccion[0]
        # Cambia el color del texto de la tarea a gris
        lista_tareas.itemconfig(indice, fg="gray")
        # Desmarca la tarea seleccionada
        lista_tareas.selection_clear(0, tk.END)


def eliminar_tarea():
    # Obtiene el índice de la tarea seleccionada en la lista de tareas
    seleccion = lista_tareas.curselection()
    if seleccion:
        indice = seleccion[0]
        # Elimina la tarea de la lista de tareas
        lista_tareas.delete(indice)


# Crear la ventana
ventana = tk.Tk()
ventana.title("Lista de Tareas")

# Crear una entrada de texto para ingresar tareas
entrada = tk.Entry(ventana, width=50)
entrada.pack(pady=10)

# Crear un botón para agregar tareas
boton_agregar = tk.Button(ventana, text="Agregar tarea", command=agregar_tarea)
boton_agregar.pack()

# Crear una lista de tareas
lista_tareas = tk.Listbox(ventana, width=50)
lista_tareas.pack(pady=10)

# Crear un botón para marcar tareas como completadas
boton_completar = tk.Button(
    ventana, text="Marcar como completada", command=completar_tarea)
boton_completar.pack()

# Crear un botón para eliminar tareas
boton_eliminar = tk.Button(
    ventana, text="Eliminar tarea", command=eliminar_tarea)
boton_eliminar.pack()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
