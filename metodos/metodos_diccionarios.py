diccionario = {
    "nombre" : "Fede",
    "apellido" : "Santoro",
    "edad": 21
}

# Devuelve las claves
print(diccionario.keys())

# Devuelve valor de una clave
print(diccionario.get("nombre"))

# Elimina un elemento
diccionario.pop("edad", "nombre")
print(diccionario)

# Para iterar el diccionario
print(diccionario.items())

# Elimina todos los elementos
diccionario.clear()
print(diccionario)