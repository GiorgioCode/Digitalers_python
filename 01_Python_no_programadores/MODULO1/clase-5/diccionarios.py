# Ejemplo 1: Crear un diccionario y acceder a sus elementos:

# Crear un diccionario con nombres y edades
personas = {'Juan': 25, 'María': 30, 'Pedro': 35}

# Acceder a los elementos del diccionario
print(personas['Juan'])  # Output: 25
print(personas['María'])  # Output: 30

# Ejemplo 2: Agregar y modificar elementos en un diccionario:

# Crear un diccionario vacío
diccionario = {}

# Agregar elementos al diccionario
diccionario['clave1'] = 'valor1'
diccionario['clave2'] = 'valor2'

# Modificar el valor de una clave existente
diccionario['clave1'] = 'nuevo valor'

# Imprimir el diccionario completo
print(diccionario)  # Output: {'clave1': 'nuevo valor', 'clave2': 'valor2'}

# Ejemplo 3: Iterar sobre un diccionario:
# Iterar sobre las claves del diccionario
for clave in personas:
    print(clave, personas[clave])

# Iterar sobre las claves y los valores del diccionario
for clave, valor in personas.items():
    print(clave, valor)

# Ejemplo 4: Comprobar la existencia de una clave en un diccionario:
if 'Juan' in personas:
    print('La clave "Juan" existe en el diccionario')

if 'María' not in personas:
    print('La clave "María" no existe en el diccionario')

# Ejemplo 5: Eliminar elementos de un diccionario:
# Eliminar un elemento por clave
del personas['Pedro']

# Limpiar el diccionario (eliminar todos los elementos)
personas.clear()

# Imprimir el diccionario vacío
print(personas)  # Output: {}


# Ejemplo 2: Combinar dos diccionarios utilizando el método update():
dic1 = {'a': 1, 'b': 2}
dic2 = {'c': 3, 'd': 4}

# Combinar dic2 en dic1
dic1.update(dic2)
print(dic1)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Ejemplo 3: Utilizar diccionarios como una estructura de datos más compleja:
# Crear un diccionario de información de estudiantes
estudiante = {
    'nombre': 'Juan',
    'edad': 20,
    'curso': 'Informática',
    'calificaciones': {
        'matemáticas': 90,
        'historia': 85,
        'ciencias': 95
    }
}

# Acceder a los elementos anidados del diccionario
print(estudiante['nombre'])  # Output: Juan
print(estudiante['calificaciones']['matemáticas'])  # Output: 90

# Ejemplo 5: Utilizar el método pop() para eliminar y obtener el valor de una clave en un diccionario:
diccionario = {'clave1': 'valor1', 'clave2': 'valor2'}

# Eliminar y obtener el valor de 'clave1'
valor = diccionario.pop('clave1')
print(valor)  # Output: valor1
print(diccionario)  # Output: {'clave2': 'valor2'}
