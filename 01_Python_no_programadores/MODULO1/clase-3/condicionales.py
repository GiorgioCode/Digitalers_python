a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))
sel = int(
    input("MENU: \n---------\n1. SUMA\n2. RESTA\n3. MULTIPLICACION\n4. DIVISION\n"))

if sel == 1:
    operacion = a + b
    print(f'La suma de {a} mas {b} es {operacion}')
elif sel == 2:
    operacion = a - b
    print(f'La resta de {a} menos {b} es {operacion}')
elif sel == 3:
    operacion = a * b
    print(f'La multiplicacion de {a} por {b} es {operacion}')
elif sel == 4:
    operacion = a / b
    print(f'La division de {a} dividido {b} es {operacion}')
else:
    mensaje_error = f'Por favor, selecciones una opcion valida. \n Programa finalizado. '
    print(mensaje_error)
    print(type(mensaje_error))
