numeros = [4, 7, 1, 42, 15]

# Encontrando numero mayor de lista
numero_mas_alto = max(numeros)
print(numero_mas_alto)

# Encontrando numero menor de la lista
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

# Redondear con decimales round(numero, cantDecimales)
numero_redondeado = round(12.35678966421, 10)
print(numero_redondeado)

# Retorna False sii se le pasa 0, vacio, False, None
resultado_bool = bool(False)
print(resultado_bool)

# Retorna True sii todos los valores son verdadero
resultado_all = all([234, "hola", True, (2,3)])
print(resultado_all)

# Suma todos los valores de iterable
resultado_sum = sum(numeros)
print(resultado_sum)