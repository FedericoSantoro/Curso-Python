def frase(nombre, apellido, adjetivo):
    return f"Hola {nombre} {apellido}, sos un {adjetivo}"

frase_resultante = frase(apellido = "Santoro", adjetivo = "capo", nombre = "Fede")
print(frase_resultante)

# Funcion con parametro opcional ( adjetivo )
def frase(nombre, apellido, adjetivo = "tonto"):
    return f"Hola {nombre} {apellido}, sos un {adjetivo}"

frase_resultante = frase("Federico", "Santoro")
print(frase_resultante)