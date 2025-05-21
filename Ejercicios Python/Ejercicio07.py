# Ejercicio 2: Contar apariciones


# Lista de colores
colores = ["rojo", "azul", "verde", "rojo", "azul", "rojo"]

# 1. Mostrar cuántas veces aparece “rojo” usando .count()
cantidad_rojo = colores.count("rojo")
print("Cantidad de veces que aparece 'rojo':", cantidad_rojo)

# 2. Reemplazar el primer “verde” por “amarillo”
indice_verde = colores.index("verde") # buscar el índice de "verde"
colores[indice_verde] = "amarillo"     # reemplazar por "amarillo"

# 3. Mostrar la lista final
print("Lista final:", colores)