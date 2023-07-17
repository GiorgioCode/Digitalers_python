# FIZZBUZZ
"""DESARROLLAR UN PROGRAMA QUE GENERE UNA SUCESION DE NUMEROS, 
DESDE 0 HASTA UN NUMERO N.
SE DEBE REEMPLAZAR EN LA SUCESION SEGÚN LAS SIGUIENTES CONDICIONES:
LOS NUMEROS MULTIPLOS DE 3 DEBEN REEMPLAZARSE POR LA PALABRA FIZZ
LOS NUMEROS MULTIPLOS DE 5 DEBEN REEMPLAZARSE POR LA PALABRA BUZZ
LOS NUMEROS MULTIPLOS DE 3 Y DE 5 DEBEN REEMPLAZARSE POR LA PALABRA
FIZZBUZZ"""

# EJEMPLO: 0,1,2,FIZZ,4,BUZZ,FIZZ,7,…..

lista = []
n = int(input("Cuantos terminos desea generar?"))

for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        lista.append("FizzBuzz")
    elif i % 3 == 0:
        lista.append("Fizz")
    elif i % 5 == 0:
        lista.append("Buzz")
    else:
        lista.append(i)

print(lista)
