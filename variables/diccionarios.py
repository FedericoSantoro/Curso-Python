# Creando diccionarios con dict()
diccionario = dict(nombre = "Fede", apellido = "Santoro")

# Se puede usar tuplas y set como clave pero no listas
diccionario = {
    ("Nombe", "Apodo") : "Fede", 
    "apellido" : "Santoro"
    }
diccionario = {
    frozenset(["Nombre", "Apodo"]) : "Fede", 
    "apellido" : "Santoro"
    }

# Crear diccionarios con fromkeys() con datos "None"
diccionario = dict.fromkeys(["Nombre", "Apellido", "Edad"])

# Crear diccionarios con fromkeys() con datos "Nose"
diccionario = dict.fromkeys(["Nombre", "Apellido", "Edad"], "No se")

# Creando diccionarios con fromkeys() llamadas 1, 2, 3, 4 con datos "Algun valor fijo"
diccionario = dict.fromkeys("1234", "Algun valor fijo")