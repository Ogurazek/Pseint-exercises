

# Ejercicio 3: Bucle Mientras (while)
# Consigna:
# Crear un programa que pida al usuario una contraseña.
# Mientras la contraseña ingresada no sea "1234", debe seguir pidiéndola.
# Cuando el usuario ingrese la contraseña correcta, mostrar un mensaje de acceso concedido.

contraseña = ""
while contraseña != "1234":
    contraseña = input("Ingrese la contraseña: ")

print("Acceso concedido.")