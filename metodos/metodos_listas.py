# Crea una lista
lista = list(["Hola", "Dalto", 34])

# Cuenta cantidad elementos
print(len(lista))

# Agrega elemento a lista
lista.append("JAJAJAJA")
print(lista)

# Agrega elemento a lista en el indice especificado
lista.insert(2, "Que copado")
print(lista)

# Agrega varios elementos a la lista
lista.extend([False, 2030])
print(lista)

# Elimina un elemento de la lista por indice y lo devuelve
print(lista.pop(2)) # Con numeros negativos elimina desde el ultimo

# Elimina un elemento de la lista por valor
lista.remove("JAJAJAJA")
lista.remove("Hola")
lista.remove("Dalto")
print(lista)

# Ordena una lista de forma ascendente a descendente ( No funciona si hay cadenas de texto)
lista.sort()
print(lista)

# Invierte elementos de una lista
lista.reverse()
print(lista)
 
# Elimina todos los elementos de una lista
lista.clear()
print(lista)