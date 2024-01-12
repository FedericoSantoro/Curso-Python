# Fibonacci

def serie_fibonacci(cantidad):
    numero1 = 0
    numero2 = 1
    fibonacci = [numero1, numero2]
    for _ in range(cantidad - 2):
        siguiente_numero = numero1 + numero2
        fibonacci.append(siguiente_numero)
        numero1 = numero2
        numero2 = siguiente_numero
    return fibonacci

cantidad_numeros = int(input("Ingrese la cantidad de numeros de fibonacci que desea obtener: "))
resultado = serie_fibonacci(cantidad_numeros)
print(resultado)