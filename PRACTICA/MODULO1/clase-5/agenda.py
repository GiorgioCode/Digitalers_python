agenda = {}


def agregar_contacto(nombre, telefono):
    # Agrega un contacto a la agenda con nombre como clave y teléfono como valor
    agenda[nombre] = telefono
    print(f"Se ha agregado el contacto {nombre} con el número {telefono}.")


def buscar_contacto(nombre):
    if nombre in agenda:  # Verifica si el nombre está presente en la agenda
        # Imprime el número de teléfono del contacto encontrado
        print(f"El número de {nombre} es {agenda[nombre]}.")
    else:
        print(f"No se encontró el contacto {nombre}.")


def eliminar_contacto(nombre):
    if nombre in agenda:  # Verifica si el nombre está presente en la agenda
        del agenda[nombre]  # Elimina el contacto de la agenda
        print(f"Se ha eliminado el contacto {nombre}.")
    else:
        print(f"No se encontró el contacto {nombre}.")


def mostrar_agenda():
    print("Agenda de contactos:")
    for nombre, telefono in agenda.items():  # Itera sobre los elementos clave-valor del diccionario
        # Imprime cada nombre y número de teléfono
        print(f"{nombre}: {telefono}")


def main():
    # Crea un diccionario vacío para almacenar los contactos
    while True:
        print("\n¿Qué deseas hacer?")
        print("1. Agregar un contacto")
        print("2. Buscar un contacto")
        print("3. Eliminar un contacto")
        print("4. Mostrar agenda de contactos")
        print("5. Salir")

        opcion = input("Ingrese el número de opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el número de teléfono: ")
            agregar_contacto(nombre, telefono)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            buscar_contacto(nombre)
        elif opcion == "3":
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            eliminar_contacto(nombre)
        elif opcion == "4":
            mostrar_agenda()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")


main()
