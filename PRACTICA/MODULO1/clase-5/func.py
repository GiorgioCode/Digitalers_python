import math

radio = int(input('QUE RADIO TIENE EL CIRCULO? :'))


def area_circulo(radio):
    return math.pi * radio ** 2


print(
    f'El area de un circulo de radio {radio} es {area_circulo(radio).__round__(2)}')
