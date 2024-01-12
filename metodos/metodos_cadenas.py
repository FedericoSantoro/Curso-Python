cadena1 = "Hola soy Fede"
cadena2 = "Como estas?"

# Funcion que devuelve los metodos que se pueden aplicar al objeto
print(dir(cadena1))

# Convierte a mayuscula
print(cadena1.upper())

# Convierte a minuscula
print(cadena1.lower())

# Convierte todo en minuscula y la primera letra en mayuscula
print(cadena1.capitalize())

# Encuentra la primera aparicion si no devuelve -1
print(cadena1.find("s"))

# Encuentra la primera aparicion si no devuelve excepcion
print(cadena1.index("s"))

# Devuelve true si es numerico
print(cadena1.isnumeric())

# Devuelve true si es alfa numerico
print(cadena1.isalpha())

# Devuelve el numero de ocurrencias de subcadena en la cadena
print(cadena1.count('o'))

# Devuelve cantidad de caracteres
print(len(cadena1))

# Verifica que una cadena comienza con otra cadena
print(cadena1.startswith("Ho"))

# Verifica que una cadena termina con otra cadena
print(cadena1.endswith("de"))

# Reemplaza un valor por otro
print(cadena1.replace("Hola", "Me presento"))

# Separa por el parametro dado
print(cadena1.split(" "))
