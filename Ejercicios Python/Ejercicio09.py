# ------------------------------------------------------------------------------
# Realizá un programa en Python que permita al usuario ingresar 10 números enteros. El programa debe:

# Almacenar los números ingresados en una lista.

# Calcular la suma de todos los números pares.

# Contar cuántos números impares se ingresaron.

# Mostrar por pantalla:

# La lista completa de números ingresados.

# La cantidad de los números pares.

# La cantidad de números impares

numeros = [2]

cantidad_pares = 0
cantidad_impares = 0

for i in range(10):
    num = int(input("Ingrese un número"))
    numeros.append(num)

for n in numeros :
    if n % 2 == 0:
        cantidad_pares = cantidad_pares + 1
    else: 
      cantidad_impares = cantidad_impares + 1  


print("La lista es:", numeros)
print("La cantidad de números pares que hay es:", cantidad_pares)
print("La cantidad de números impares que hay es:", cantidad_impares)