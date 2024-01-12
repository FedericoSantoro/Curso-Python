frutas = ["banana", "manzana", "ciruela", "pera", "naranja", "granada", "durazno"]
cadena = "Hola Dalto"
numeros = [10, 52, 2, 65]

# Evitando un caso
for fruta in frutas:
    if fruta == "granada":
        continue
    print(f"Voy a comer una {fruta}")
else:
    print("Termine de comer las frutas")
    
# Evitar que se siga ejecutando
for fruta in frutas:
    print(f"Voy a comer una {fruta}")
    if fruta == "manzana":
        break
else:
    print("Comi todas las frutas")
    
# Recorrer cadena de texto
for letra in cadena:
    print(letra)
    
# for en una sola linea de codigo
numeros_duplicados = [numero*2 for numero in numeros]