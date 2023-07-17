import tkinter as tk  # Importar el módulo tkinter y asignarlo al alias tk

# Definir la función para convertir a dólares


def convertir_a_dolares():
    try:
        # Obtener el valor ingresado en el campo de entrada para el peso argentino y convertirlo a un número de punto flotante
        peso_argentino = float(entrada_peso.get())
        # Obtener el valor ingresado en el campo de entrada para el tipo de cambio y convertirlo a un número de punto flotante
        tipo_cambio = float(entrada_tipo_cambio.get())
        # Realizar la conversión de pesos argentinos a dólares
        dolares = peso_argentino / tipo_cambio
        # Establecer el resultado en el formato "$X.XX"
        resultado.set(f"${dolares:.2f}")
    except ValueError:  # Capturar una excepción si ocurre un error de valor al convertir las entradas a números
        # Establecer un mensaje de error en el resultado
        resultado.set("¡Error de entrada!")

# Definir la función para convertir a pesos argentinos


def convertir_a_pesos():
    try:
        # Obtener el valor ingresado en el campo de entrada para los dólares y convertirlo a un número de punto flotante
        dolares = float(entrada_dolares.get())
        # Obtener el valor ingresado en el campo de entrada para el tipo de cambio y convertirlo a un número de punto flotante
        tipo_cambio = float(entrada_tipo_cambio.get())
        # Realizar la conversión de dólares a pesos argentinos
        pesos_argentinos = dolares * tipo_cambio
        # Establecer el resultado en el formato "$X.XX"
        resultado.set(f"${pesos_argentinos:.2f}")
    except ValueError:  # Capturar una excepción si ocurre un error de valor al convertir las entradas a números
        # Establecer un mensaje de error en el resultado
        resultado.set("¡Error de entrada!")


# Crear la ventana principal
ventana = tk.Tk()  # Crear una instancia de la clase Tk para representar la ventana principal
ventana.title("Conversor de moneda")  # Establecer el título de la ventana
ventana.geometry("300x300")  # Establecer las dimensiones de la ventana

# Etiqueta y campo de entrada para el peso argentino
# Crear una etiqueta con el texto "Peso Argentino"
etiqueta_peso = tk.Label(ventana, text="Peso Argentino:")
etiqueta_peso.pack()  # Mostrar la etiqueta en la ventana
# Crear un campo de entrada para ingresar el peso argentino
entrada_peso = tk.Entry(ventana)
entrada_peso.pack()  # Mostrar el campo de entrada en la ventana

# Etiqueta y campo de entrada para el dólar
# Crear una etiqueta con el texto "Dólares"
etiqueta_dolares = tk.Label(ventana, text="Dólares:")
etiqueta_dolares.pack()  # Mostrar la etiqueta en la ventana
# Crear un campo de entrada para ingresar los dólares
entrada_dolares = tk.Entry(ventana)
entrada_dolares.pack()  # Mostrar el campo de entrada en la ventana

# Etiqueta y campo de entrada para el tipo de cambio
# Crear una etiqueta con el texto "Cuantos pesos vale un dolar?"
etiqueta_tipo_cambio = tk.Label(ventana, text="Cuantos pesos vale un dolar?:")
etiqueta_tipo_cambio.pack()  # Mostrar la etiqueta en la ventana
# Crear un campo de entrada para ingresar el tipo de cambio
entrada_tipo_cambio = tk.Entry(ventana)
entrada_tipo_cambio.pack()  # Mostrar el campo de entrada en la ventana

# Botones de conversión
boton_a_dolares = tk.Button(
    ventana, text="Convertir a Dólares", command=convertir_a_dolares)  # Crear un botón con el texto "Convertir a Dólares" que llama a la función convertir_a_dolares cuando se presiona
boton_a_dolares.pack()  # Mostrar el botón en la ventana
boton_a_pesos = tk.Button(
    ventana, text="Convertir a Pesos", command=convertir_a_pesos)  # Crear un botón con el texto "Convertir a Pesos" que llama a la función convertir_a_pesos cuando se presiona
boton_a_pesos.pack()  # Mostrar el botón en la ventana

# Resultado de la conversión
# Crear una variable de control para almacenar el resultado de la conversión
resultado = tk.StringVar()
# Crear una etiqueta que muestra el valor almacenado en la variable de control
etiqueta_resultado = tk.Label(ventana, textvariable=resultado)
etiqueta_resultado.pack()  # Mostrar la etiqueta en la ventana

# Iniciar el bucle principal de la ventana
# Ejecutar el bucle principal que muestra la ventana y permite la interacción con ella
ventana.mainloop()
