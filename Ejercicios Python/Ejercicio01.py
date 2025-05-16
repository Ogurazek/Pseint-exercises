
# Ejercicio 1: Escribir, Leer y Asignar 😎

# Pedir al usuario su nombre y su edad. Mostrar un mensaje que diga: "Hola [nombre], tenés [edad]
# años."

# Input = Escribir | Imprimir en Pseint

nombre = input("Ingrese su nombre: ")

try:
    edad = int(input("Ingrese su edad: "))
    print(f"Hola {nombre}, tenés {edad} años.")

except ValueError:
    print("El valor ingresado no es el correcto, por favor ingresa un número")









