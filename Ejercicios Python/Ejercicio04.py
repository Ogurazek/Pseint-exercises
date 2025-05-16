# Ejercicio 4: Bucle Para (for)
# Consigna:
# Pedir al usuario un número N y mostrar la tabla de multiplicar del 1 al 10 de ese número


numero = int(input("Ingrese un número: "))

print(f"Tabla de multiplicar del {numero}:")


for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")


