animales = ["pez", "gato", "perro", "loro", "cocodrilo"]
numeros = [10, 54, 36, 87, 5]

for animal in animales:
    print(f"Ahora la variable item es igual a {animal}")

suma = 0

for numero in numeros:
    suma = suma + numero

print(suma)

# Iterar mas de una lista (del mismo tamaño) juntas
for numero, animal in zip(animales, numeros):
    print(f"El {numero} es un {animal}")

# Iterar entre tantos rangos (5 a 10)
for numero in range(5,10):
    print(numero)
    
# Iterar entre tantos rangos (0 a 10)
for numero in range(10):
    print(numero)
    
for numero in enumerate(numeros):
    indice = numero[0]
    valor = numero[1]
    #print(f"Este es el elemento : {numero}")
    print(f"Este es el indice : {indice}")
    print(f"Este es el valor : {valor}")

# Otra forma
for numero, index in enumerate(numeros):
    #print(f"Este es el elemento : {numero}")
    print(f"Este es el indice : {index}")
    print(f"Este es el valor : {numero}")
    
# Usando el else (se ejecuta siempre al final del bucle)
for numero in numeros:
    print(f"Valor actual: {numero}")
# else:
#     print("El bucle termino")
    