
# Ejercicio 3: Diccionario de estudiante


# Diccionario del estudiante
estudiante = {
    "nombre": "Ana",
    "edad": 20,
    "materias": ["Matemática", "Historia"]
}

# 1. Mostrar el nombre y la edad
print("Nombre:", estudiante["nombre"])
print("Edad:", estudiante["edad"])

# 2. Agregar una materia nueva a la lista materias
estudiante["materias"].append("Biología")

# 3. Mostrar cuántas materias cursa con len()
cantidad_materias = len(estudiante["materias"])
print("Cantidad de materias:", cantidad_materias)

# 4. Usar get() para obtener la clave “promedio” con valor por defecto 0
promedio = estudiante.get("promedio", 0)
print("Promedio:", promedio)