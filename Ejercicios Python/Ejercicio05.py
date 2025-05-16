# Integrador: Adivina el número
# Consigna:
# El programa elige un número secreto entre 1 y 100.
# El usuario debe adivinar el número.
# Después de cada intento, el programa debe decir si el número ingresado es mayor o menor que el
# número secreto.
# El usuario tiene un máximo de 10 intentos.
# Si lo adivina antes, mostrar un mensaje de felicitaciones indicando en qué intento lo logró.
# Si no lo adivina en 10 intentos, mostrar un mensaje diciendo que perdió.



import random  # Importamos el módulo para usar números aleatorios

# Elige un número secreto aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

intentos = 0
max_intentos = 10

print("¡Adivina el número secreto entre 1 y 100!")
print(f"Tenés un máximo de {max_intentos} intentos.\n")

# Bucle de intentos
while intentos < max_intentos:
    intento = int(input(f"Intento {intentos + 1}: Ingresá tu número: "))
    intentos += 1

    if intento == numero_secreto:
        print(f"🎉 ¡Felicitaciones! Adivinaste el número en el intento {intentos}.")
        break
    elif intento < numero_secreto:
        print("🔼 El número secreto es más grande.")
    else:
        print("🔽 El número secreto es más chico.")

# Si se terminó el bucle y no acertó
if intento != numero_secreto:
    print(f"\n😢 ¡Perdiste! El número secreto era {numero_secreto}.")