class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print("Hola! soy un animal!!")

    def traslado(self):
        raise NotImplementedError("Metodo definido solo en subclases")


class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def saludar(self):
        print(f'Hola, soy un perro llamado {self.nombre} de raza {self.raza}')

    def traslado(self):
        print("Soy un perro y me traslado caminando")


class Pajaro(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.color = color

    def saludar(self):
        print(
            f'Hola, soy un Pajaro llamado {self.nombre} de color {self.color}')

    def traslado(self):
        print("Soy un pajaro y me traslado volando")


animal1 = Animal("Caballo")
perro1 = Perro("Fido", 4)
pajaro1 = Pajaro("Colobri", "multicolor")

animal1.saludar()
perro1.saludar()
perro1.traslado()
pajaro1.saludar()
pajaro1.traslado()
