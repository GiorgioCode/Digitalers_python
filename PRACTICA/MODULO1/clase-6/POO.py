"""La Programación Orientada a Objetos es un paradigma de programación que se basa en la idea 
de "objetos" y su interacción para resolver problemas. En Python, todo se considera un objeto,
lo que significa que puedes crear y manipular diferentes objetos en tu programa.

Los objetos tienen propiedades y comportamientos asociados. Las propiedades se llaman atributos
y los comportamientos se llaman métodos. Aquí tienes una explicación simple de cada uno:

"""

# Definición de una clase y creación de objetos:
"""
Clase: Una clase es un plano o plantilla para crear objetos. Define las propiedades y 
comportamientos comunes que los objetos de esa clase tendrán. Por ejemplo, si tienes 
una clase "Perro", todos los perros tendrán características y comportamientos similares 
definidos en la clase.
"""


class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def ladrar(self):
        print("¡Guau!")


# Crear objetos de la clase Perro
"""
Objeto: Un objeto es una instancia de una clase. Se crea a partir de una clase específica
y tiene sus propias propiedades y comportamientos. Por ejemplo, si tienes una clase "Perro",
puedes crear varios objetos de esa clase, como "Perro1" y "Perro2", cada uno con sus propias
características y comportamientos únicos.
"""
perro1 = Perro("Fido", 3)
perro2 = Perro("Rex", 5)

# Acceder a los atributos de los objetos
"""
Atributo: Un atributo es una propiedad de un objeto. Puede ser una variable que almacena 
datos específicos de ese objeto. Por ejemplo, un perro puede tener atributos como nombre, 
edad, raza, etc.
"""
print(perro1.nombre)  # Salida: Fido
print(perro2.edad)    # Salida: 5


# Llamar a los métodos de los objetos
"""
Método: Un método es una función definida en una clase que representa un comportamiento del
objeto. Los métodos permiten realizar acciones específicas en los objetos de una clase. Por
ejemplo, un perro puede tener métodos como ladrar(), caminar(), comer(), etc.
"""

perro1.ladrar()  # Salida: ¡Guau!
perro2.ladrar()  # Salida: ¡Guau!


"""
Herencia: La herencia es un concepto que permite crear nuevas clases basadas en una clase 
existente. La clase existente se llama clase padre o superclase, y la nueva clase se llama 
clase hija o subclase. La subclase hereda los atributos y métodos de la superclase y puede 
agregar nuevos atributos y métodos o modificar los existentes.
"""


class Animal1:
    def __init__(self, nombre):  # ACLARACION 1
        self.nombre = nombre

    def saludar(self):
        print("¡Hola! Soy un animal.")


"""
ACLARACION 1: La función __init__() es un método especial en Python que se llama automáticamente
cuando se crea una instancia de una clase. Se utiliza para inicializar los atributos de un objeto
y realizar cualquier configuración necesaria al crearlo.

Al definir la función __init__() en una clase, puedes especificar los parámetros que se 
deben pasar al crear un objeto de esa clase. Estos parámetros se utilizan para establecer 
los valores iniciales de los atributos del objeto.
"""


class Perro(Animal1):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def saludar(self):
        print(
            f"¡Hola! Soy un perro llamado {self.nombre} de raza {self.raza}.")


"""
super() se utiliza en la programación orientada a objetos en Python para llamar a los métodos
de la clase padre (superclase) desde una clase hija (subclase). Proporciona una forma de 
acceder y utilizar los métodos y atributos heredados de la clase padre.

Al utilizar super(), puedes acceder y llamar a los métodos de la superclase en la subclase.
Esto es útil cuando deseas ampliar o modificar el comportamiento de los métodos heredados 
sin tener que volver a escribir todo el código.

super() se utiliza generalmente dentro del método __init__() de la subclase para llamar 
al método __init__() de la superclase y asegurarse de que la inicialización de la superclase
se realice correctamente antes de realizar cualquier otra configuración en la subclase.
"""


# Crear objeto de la clase Perro
perro = Perro("Fido", "Labrador")

# Acceder a los atributos y llamar a los métodos
print(perro.nombre)  # Salida: Fido
print(perro.raza)    # Salida: Labrador
# Salida: ¡Hola! Soy un perro llamado Fido de raza Labrador.
perro.saludar()


"""
Encapsulación: La encapsulación es un concepto que se refiere a agrupar datos y métodos 
relacionados en una sola entidad, la clase. Esto permite ocultar la implementación interna 
de la clase y proporcionar una interfaz externa para interactuar con los objetos. Ayuda a 
mantener la integridad y la seguridad de los datos.
"""


"""
Polimorfismo: El polimorfismo permite que los objetos de diferentes clases respondan de 
manera diferente a la misma llamada de método. Es decir, diferentes clases pueden tener 
métodos con el mismo nombre pero comportamientos diferentes. Esto facilita el uso de diferentes
objetos de manera intercambiable.
"""


class Animal2:
    def hablar(self):
        raise NotImplementedError("Subclase debe implementar este método.")


"""
NotImplementedError es una excepción predefinida en Python que se utiliza para indicar que
un método en una clase abstracta o en una clase base (superclase) debe ser implementado en
las clases hijas (subclases) que heredan de ella.

Cuando una subclase hereda de una superclase que contiene un método marcado con 
NotImplementedError, si la subclase no proporciona su propia implementación de ese 
método, se generará una excepción NotImplementedError cuando se intente llamar a ese método
en la subclase."""


class Perro(Animal2):
    def hablar(self):
        return "¡Guau!"


class Gato(Animal2):
    def hablar(self):
        return "¡Miau!"


# Crear objetos de diferentes clases
perro = Perro()
gato = Gato()

# Llamar al mismo método en diferentes objetos
print(perro.hablar())  # Salida: ¡Guau!
print(gato.hablar())   # Salida: ¡Miau!
