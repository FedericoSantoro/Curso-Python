numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Creando funcion lambda
multiplicar_por_dos = lambda x : x * 2

print(multiplicar_por_dos(5))

# Creando funcion par
def es_par(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
# Usando filter con funcion comun
numeros_pares = filter(es_par, numeros)
print(list(numeros_pares))

# Creando lo mismo pero con lambda
numeros_pares = filter(lambda numero: numero % 2 == 1, numeros)
print(list(numeros_pares))
