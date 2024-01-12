diccionario = {
    "nombre" : "Federico",
    "apellido" : "Santoro",
    "edad" : 21
}

for key in diccionario:
    print(f"La clave '{key}' tiene el valor '{diccionario[key]}'")

# items() devuelve una dupla que desempaqueto
for key, valor in diccionario.items():
    print(f"La clave '{key}' tiene el valor '{valor}'")