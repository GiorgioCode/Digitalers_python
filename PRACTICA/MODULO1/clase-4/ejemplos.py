# Generador de tablas de multiplicar

def generar_tabla_multiplicar(numero):
    """
    Genera la tabla de multiplicar de un número hasta un límite dado.
    """
    tabla = []
    for i in range(1, 11):
        resultado = numero * i
        tabla.append((numero, i, resultado))
    return tabla


# Pedir al usuario el número y límite
numero = int(input("Ingrese un número: "))

# Generar y mostrar la tabla de multiplicar
tabla_multiplicar = generar_tabla_multiplicar(numero)
for entrada in tabla_multiplicar:
    num, factor, resultado = entrada
    print(f"{num} x {factor} = {resultado}")
