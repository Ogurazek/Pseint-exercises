# Ejercicio 1: Gestión de una lista de compras

# Crear una lista vacía
lista_compras = []

# 1. Agregar 3 productos usando .append()
lista_compras.append("Leche")
lista_compras.append("Pan")
lista_compras.append("Huevos")

# 2. Mostrar cuántos productos hay con len()
print("Cantidad de productos:", len(lista_compras))

# 3. Eliminar el último producto con .pop()
producto_eliminado = lista_compras.pop(0)
print("Producto eliminado:", producto_eliminado)

# 4. Mostrar la lista actualizada
print("Lista actualizada:", lista_compras)
