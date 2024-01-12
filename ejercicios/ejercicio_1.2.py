# promedio = 2 palabras por seg
# dalto = 2.6 palabras por seg 
texto = input("Texto a evaluar: ")

texto_dividido = texto.split(" ")
tiempo_tardado = len(texto_dividido) / 2
print(f"Se tardaria en decir esta frase {tiempo_tardado} segundos")
print(f"Y se dijeron {len(texto_dividido)} palabras")

if tiempo_tardado > 60:
    print("Para flaco tampoco te pedi un testamento")

tiempo_dalto = len(texto_dividido) * 100 // 2.6 / 100
print(f"Dalto tardaria {tiempo_dalto} segundos en decirlo")