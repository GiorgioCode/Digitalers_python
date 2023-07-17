import math


def suma(a, b):
    return a + b


# Llamada a la función
resultado = suma(3, 5)
print(resultado)  # Output: 8

# Ejemplo 2: Función para calcular el área de un círculo:


def calcular_area_circulo(radio):
    return math.pi * radio ** 2


# Llamada a la función
radio = 2
area = calcular_area_circulo(radio)
print(area)  # Output: 12.566370614359172

# Ejemplo 3: Función para verificar si un número es par:


def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


num = 4
if es_par(num):
    print("El número es par.")
else:
    print("El número es impar.")


# Ejemplo 4: Función para contar la cantidad de elementos en una lista:

def contar_elementos(lista):
    return len(lista)


mi_lista = [1, 2, 3, 4, 5]

cantidad = contar_elementos(mi_lista)
print(cantidad)  # Output: 5

# Ejemplo 1: Función para sumar una cantidad variable de números utilizando *args:


def suma_variable(*args):
    suma = 0
    for num in args:
        suma += num
    return suma


resultado = suma_variable(1, 2, 3, 4, 5)
print(resultado)  # Output: 15


# Ejemplo 2: Función que acepta argumentos posicionales y argumentos con nombre utilizando *args y **kwargs:
def funcion_variable(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(key, ":", value)


# Llamada a la función
funcion_variable("Hola", 123, nombre="Juan", edad=25)
# Output:
# Hola
# 123
# nombre : Juan
# edad : 25

# Ejemplo 3: Función que combina dos diccionarios utilizando **kwargs:


def combinar_diccionarios(dic1, dic2, **kwargs):
    dic_combinado = {**dic1, **dic2, **kwargs}
    return dic_combinado


# Llamada a la función
diccionario1 = {'a': 1, 'b': 2}
diccionario2 = {'c': 3, 'd': 4}
diccionario_combinado = combinar_diccionarios(
    diccionario1, diccionario2, e=5, f=6)
print(diccionario_combinado)
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# jemplo 4: Función que calcula el promedio de una lista de números utilizando *args:


def calcular_promedio(*args):
    total = sum(args)
    promedio = total / len(args)
    return promedio


# Llamada a la función
promedio = calcular_promedio(1, 2, 3, 4, 5)
print(promedio)  # Output: 3.0
