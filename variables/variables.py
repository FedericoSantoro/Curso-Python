# Se recomienda usar snake_case
nombre_completo = "Fede Santoro"

# Concatenar con +
bienvenida = "Hola " + nombre_completo + " Que tal?"
print(bienvenida)

# Borra variable
del bienvenida 

# Concatenar con f-strings
bienvenida = f"Hola {nombre_completo} Como estas?"
print(bienvenida)

# Pertenencia ( in / not in )
print("Hola" in bienvenida)
print("hola" in bienvenida)
print("Pedro" in bienvenida)
print("Pedro" not in bienvenida)