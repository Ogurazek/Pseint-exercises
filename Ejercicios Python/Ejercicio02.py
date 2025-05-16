



# Ejercicio 2: Condicional Si
# Consigna:
# Pedir un número al usuario. Mostrar un mensaje que diga si el número es positivo, negativo o cero.

# Pedir un número al usuario
numero = float(input("Ingrese un número: "))

# Verificar si es positivo, negativo o cero
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")