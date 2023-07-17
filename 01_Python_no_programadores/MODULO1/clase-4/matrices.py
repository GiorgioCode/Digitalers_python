
numero = int(input("Que tabla desea generar?"))

for factor in range(1, 11):
    resultado = numero * factor
    print(f'{numero} X {factor} = {resultado}')
