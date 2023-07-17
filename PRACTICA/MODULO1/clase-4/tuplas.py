tupla = (1, 2, 3, 4, 5, 6, 7)
print(tupla)
print("Ahora tupla es:", type(tupla))
tupla = list(tupla)
print("Ahora tupla es:", type(tupla))
tupla.append(5)
print(tupla)
tupla = tuple(tupla)
print("Ahora tupla es:", type(tupla))
print(tupla)
print(tupla[4])

for numero in tupla:
    print(numero)
