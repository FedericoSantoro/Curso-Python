def suma(a,b):
    return a + b

resultado = suma(2, 3)

# Parametro args ( * ), convierte lo que recibe en una lista
def mejor_suma(nombre, *numeros):
    return f"{nombre}, la suma de los numeros es: {sum(numeros)}"

resultado = mejor_suma("Fede", 2,6,8,4,32,45)
print(resultado)

# Otra forma util tambien para llenar lo de una lista con otra es
def mejor_suma(numeros):
    return sum([*numeros])

resultado = mejor_suma([2,6,8,4,32,45])
print(resultado)