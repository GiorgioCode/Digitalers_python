import random

numero_secreto = random.randint(1, 10)
intentos = 0
adivinado = False

while not adivinado:
    intentos += 1
    adivina = int(input("Adivine el número (entre 1 y 10): "))

    if adivina == numero_secreto:
        adivinado = True
    elif adivina < numero_secreto:
        print("Demasiado bajo. Intente nuevamente.")
    else:
        print("Demasiado alto. Intente nuevamente.")

print("¡Felicitaciones! Adivinó el número en ",
      intentos, " intentos. El numero era el ", adivina)
