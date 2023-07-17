import tkinter as tk


def mostrar_mensaje():
    etiqueta.config(text="Se ha presionado el boton!!!")


# Crear la ventana
ventana = tk.Tk()
ventana.title("Ejemplo de Tkinter")

# Crear una etiqueta
etiqueta = tk.Label(ventana, text="Presiona el botón para mostrar un mensaje")
etiqueta.pack(pady=10)

# Crear un botón
boton = tk.Button(ventana, text="Mostrar mensaje", command=mostrar_mensaje)
boton.pack(pady=5)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
