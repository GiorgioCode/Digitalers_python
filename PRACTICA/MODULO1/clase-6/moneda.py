import tkinter as tk

# funciones


def convertir_a_dolares():
    try:
        peso_argentino = float(entrada_peso.get())
        tipo_cambio = float(entrada_tipo_cambio.get())
        dolares = peso_argentino / tipo_cambio
        resultado.set(f'${dolares:.2f}')

    except ValueError:
        resultado.set("Error de entrada")


def convertir_a_pesos():
    try:
        dolares = float(entrada_dolares.get())
        tipo_cambio = float(entrada_tipo_cambio.get())
        pesos_argentinos = dolares*tipo_cambio
        resultado.set(f'${pesos_argentinos:.2f}')

    except ValueError:
        resultado.set("Error de entrada")


# grafica
ventana = tk.Tk()

ventana.title("Conversor de monedas")
ventana.geometry("300x300")

etiqueta_peso = tk.Label(ventana, text="Peso argentino:")
etiqueta_peso.pack()
entrada_peso = tk.Entry(ventana)
entrada_peso.pack()

etiqueta_dolares = tk.Label(ventana, text="Dolares:")
etiqueta_dolares.pack()
entrada_dolares = tk.Entry(ventana)
entrada_dolares.pack()

etiqueta_tipo_cambio = tk.Label(ventana, text="Cuantos pesos vale un dolar:")
etiqueta_tipo_cambio.pack()
entrada_tipo_cambio = tk.Entry(ventana)
entrada_tipo_cambio.pack()

boton_a_dolares = tk.Button(
    ventana, text="Convertir a dolares", command=convertir_a_dolares)
boton_a_dolares.pack()

boton_a_pesos = tk.Button(
    ventana, text="Convertir a pesos", command=convertir_a_pesos)
boton_a_pesos.pack()

resultado = tk.StringVar()
etiqueta_resultado = tk.Label(ventana, textvariable=resultado)
etiqueta_resultado.pack()

# loop
ventana.mainloop()
