def es_primo(numero):
    for i in range(2, numero):
        if numero % i == 0 : return False
    return True

def numeros_primos_hasta(numero):
    numeros_primos = []
    for i in range(1, numero + 1):
        if es_primo(i) : numeros_primos.append(i)
    return numeros_primos
        
        
resultados = numeros_primos_hasta(13)
print(resultados)